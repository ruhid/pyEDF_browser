import sys
import pyfirmata
from PyQt5.QtCore import QAbstractTableModel, QVariant, Qt
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem, QFileDialog, QMainWindow, QMessageBox, QLabel, \
    QGraphicsColorizeEffect
from edf import *
from plot_edf import *
import math
import serial
from serial.tools import list_ports
import random
import time
import numpy as np
import mne
import pandas as pd
import pyqtgraph as pg

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonPlot.clicked.connect(self.show_edf_plot_window)
        self.ui.pushButtonFile.clicked.connect(self.load_edf)
        self.pg=pg
        self.new_values=[]
        self.DialogAnalog = QtWidgets.QDialog()
        self.ui_edf = Ui_DialogAnalog()
        self.ui_edf.setupUi(self.DialogAnalog)
        self.color_effect = QGraphicsColorizeEffect()
        self.ui_edf.pushButtonFilt.clicked.connect(self.mne_filter)
        self.ui_edf.pushButtonOrig.clicked.connect(self.read_original)
        self.ui_edf.horizontalSliderRtOnset.valueChanged.connect(self.update_rt_plot)
        self.ui_edf.pushButtonTKEO.clicked.connect(self.TKO_convert)
        self.ui_edf.pushButtonForward.clicked.connect(self.channel_forw)
        self.ui_edf.pushButtonBackward.clicked.connect(self.channel_backw)
        self.ui_edf.checkBoxRect.clicked.connect(self.rectify)
        self.ui_edf.pushButtonSaveRT.clicked.connect(self.save_rt)
        self.p1 = self.ui_edf.graphicsView.addPlot(row=0, col=0)
        self.p2 = self.ui_edf.graphicsView.addPlot(row=1, col=0)
        self.current_ch_index=0

        self.rts_dct={}
        #self.ui_edf.graphicsView.sigMouseReleased.connect(self.mouse_clicked)
        self.show()


    def save_rt(self):
        self.rts_dct[self.current_ch]=[self.ui_edf.spinBoxRtOnset.value(),]
        self.rts_df = pd.DataFrame(self.rts_dct)
        self.model=PandasModel(self.rts_df.transpose())
        self.ui_edf.tableViewRTS_plot_window.setModel(self.model)

    def TKO(self, signal):
        windows = np.lib.stride_tricks.sliding_window_view(signal, 3)
        TKO = windows[:, 1] ** 2 - windows[:, 0] * windows[:, 2]
        try:
            return pd.Series(np.concatenate([np.zeros(1), TKO, np.zeros(1)]), index=signal.index)
        except Exception as E:
            print(E)
            print("returnin without index")
            return np.concatenate([np.zeros(1), TKO, np.zeros(1)])

    def TKO_convert(self):
        self.edf_Sr=self.TKO(self.edf_Sr)
        self.update_rt_plot()

    def rectify(self):
        if self.ui_edf.checkBoxRect.isChecked():
            self.edf_Sr=self.edf_Sr_original.abs()
            self.update_rt_plot()


    def mne_filter(self):
        l_freq=self.ui_edf.spinBoxFiltLc.value()
        h_freq=self.ui_edf.spinBoxFiltHc.value()
        self.edf_raw.filter(l_freq,h_freq)
        self.edf_df = self.edf_raw.to_data_frame()
        self.df_to_sr()
        self.update_rt_plot()

    def channel_forw(self):
        if self.current_ch_index<len(self.edf_raw.ch_names):
            self.current_ch=self.edf_raw.ch_names[self.current_ch_index]
            self.current_ch_index += 1
        else:
            self.current_ch_index=0

        print(self.current_ch_index)

        self.read_original()

    def channel_backw(self):
        if self.current_ch_index>=0:
            self.current_ch=self.edf_raw.ch_names[self.current_ch_index]
            self.current_ch_index -= 1
        else:
            self.current_ch_index=len(self.edf_raw.ch_names)-1

        print(self.current_ch_index)
        self.read_original()


    def show_edf_plot_window(self):
        self.DialogAnalog.show()
        self.df_to_sr()
        self.update_rt_plot()

    def mouse_clicked(self, event):
        print("knöknk")
        print(f"{event.pos().x}  {event.pos().y}")

    def read_original(self):
        self.edf_raw = mne.io.read_raw_edf(self.fileNameEDF, preload=True)
        self.edf_df_original = self.edf_raw.to_data_frame()
        self.df_to_sr()
        self.update_rt_plot()

    def df_to_sr(self):
        self.current_ch=self.edf_raw.ch_names[self.current_ch_index]
        self.edf_Sr=self.edf_df[self.current_ch]
        self.edf_Sr_original=self.edf_Sr
        self.ui_edf.horizontalSliderRtOnset.setMaximum(self.edf_Sr.index.max())
        self.ui_edf.horizontalSliderRtOnset.setMinimum(self.edf_Sr.index.min())

    def load_edf(self):
        try:
            self.fileNameEDF, OK = QFileDialog.getOpenFileName(self, 'Open file', ".\\", "EDF files (*.edf)")
            if OK:
                self.ui.labelEDFFile.setText(self.fileNameEDF)
                self.read_original()
        except Exception as e:
            print(f"Error during settings save: {e}")


    def plot_window_scroll(self):
        window = self.ui_edf.spinBoxWindowSize.value()

    def update_rt_plot(self):
        rtonset=self.ui_edf.horizontalSliderRtOnset.value()
        x2=self.edf_df_original[self.current_ch]
        y2 = self.edf_Sr
        x=self.edf_Sr_original.index
        y=self.edf_Sr_original
        #self.p2.setLimits(xMin=0, xMax=1, yMin=-1000, yMax=-1000)
        self.p1.plot(x, y, pen=(255, 0, 0), name="Green curve", clear=True)
        self.p1.plot([rtonset, rtonset], [0, y.max()], pen=pg.mkPen('m', width=2))
        self.p2.plot(x2, y2, pen=(0, 255, 0), name="Gr curve", clear=True)
        self.p2.plot([rtonset, rtonset], [0, y2.max()], pen=pg.mkPen('m', width=2))
        text = pg.TextItem(
            html=f'<div style="text-align: center"><span style="color: #FFF;font-size: 16pt;">{self.current_ch}</span></div>',
            anchor=(0.5, 0.5))
        self.p1.addItem(text)




#table view

class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return QVariant()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return str(self._data.columns[section])
        elif orientation == Qt.Vertical:
            return str(self._data.index[section])
        return None



if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    pg.SignalProxy(w.p2.scene().sigMouseClicked, rateLimit=60, slot=w.mouse_clicked)
    w.show()
    sys.exit(app.exec_())

