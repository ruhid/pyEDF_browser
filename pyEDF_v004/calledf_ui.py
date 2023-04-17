import datetime
import sys
import pyfirmata
from PyQt5.QtCore import QAbstractTableModel, QVariant, Qt, QTimer
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
import os


class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonPlot.clicked.connect(self.show_edf_plot_window)
        self.ui.pushButtonFile.clicked.connect(self.load_edf)
        self.ui.pushButtonOpenCsv.clicked.connect(self.load_csv)
        self.ui.pushButtonSaveRtToFile.clicked.connect(self.save_rt_to_file)
        self.pg = pg
        self.new_values = []
        self.DialogAnalog = QtWidgets.QDialog()
        self.ui_edf = Ui_DialogAnalog()
        self.ui_edf.setupUi(self.DialogAnalog)
        self.color_effect = QGraphicsColorizeEffect()
        self.ui_edf.checkBoxFilt.clicked.connect(self.update_rt_plot)
        self.ui_edf.pushButtonOrig.clicked.connect(self.read_original)
        self.ui_edf.horizontalSliderRtOnset.valueChanged.connect(self.update_rt_plot)
        self.ui_edf.checkBoxTKEO.clicked.connect(self.update_rt_plot)
        self.ui_edf.checkBoxRect.clicked.connect(self.update_rt_plot)
        self.ui_edf.checkBoxTKEORect.clicked.connect(self.update_rt_plot)
        self.ui_edf.pushButtonForward.clicked.connect(self.channel_forw)
        self.ui_edf.pushButtonBackward.clicked.connect(self.channel_backw)
        self.ui_edf.pushButtonSaveRT.clicked.connect(self.save_rt)
        self.ui_edf.spinBoxSyncAnalogEDF.valueChanged.connect(self.sync_analog_edf)
        self.ui_edf.pushButtonNoRT.clicked.connect(self.no_rt)
        self.p1 = self.ui_edf.graphicsView.addPlot(row=0, col=0)
        self.p2 = self.ui_edf.graphicsView.addPlot(row=1, col=0)
        self.current_ch_index = 0
        self.sample_rate = 100000
        self.need_to_filter=True
        self.rts_dct = {}
        self.options = QFileDialog.Options()
        # self.ui_edf.graphicsView.sigMouseReleased.connect(self.mouse_clicked)
        self.show()

    def load_edf(self):
        try:
            self.fileNameEDF, OK = QFileDialog.getOpenFileName(self, 'Open file', ".\\", "EDF files (*.edf)",options=self.options)
            if OK:
                self.default_dir=os.path.dirname(self.fileNameEDF)
                self.ui.labelEDFFile.setText(self.fileNameEDF)
                self.read_original()
        except Exception as e:
            print(f"Error during settings save: {e}")

    def load_csv(self):
        try:
            self.fileNameCSV, OK = QFileDialog.getOpenFileName(self, 'Open file', "", "EDF files (*.csv)",options=self.options)
            if OK:
                self.ui.labelEDFFile.setText(self.fileNameCSV)
                self.ad_fsr_button_data_to_df()
        except Exception as e:
            print(f"Error during settings save: {e}")

    def ad_fsr_button_data_to_df(self):
        self.csv_df = pd.read_csv(self.fileNameCSV)
        self.csv_dct = {i: data for i, data in self.csv_df.groupby("id")}

    def read_original(self):
        self.edf_raw = mne.io.read_raw_edf(self.fileNameEDF, preload=True)
        self.edf_df_original = self.edf_raw.to_data_frame()
        self.current_ch = self.edf_raw.ch_names[self.current_ch_index]
        self.update_rt_plot()

    def signal_pipeline(self):
        if self.ui_edf.checkBoxFilt.isChecked() and self.need_to_filter:
            l_freq = self.ui_edf.spinBoxFiltLc.value()
            h_freq = self.ui_edf.spinBoxFiltHc.value()
            self.edf_raw.filter(l_freq, h_freq)
            self.need_to_filter=False

        output_y = self.edf_raw[self.current_ch][0].T.reshape(-1)
        output_x = self.edf_raw[self.current_ch][1]


        if self.ui_edf.checkBoxRect.isChecked():
            output_y = np.abs(output_y)
        if self.ui_edf.checkBoxTKEO.isChecked():
            output_y = self.TKO(output_y)
            if self.ui_edf.checkBoxTKEORect.isChecked():
                output_y = np.abs(output_y)

        self.output = {}
        self.output["x"] = output_x
        self.output["y"] = output_y

    def update_rt_plot(self):

        original = self.edf_df_original[self.current_ch]

        x = original.index
        y = original

        self.signal_pipeline()
        x2 = self.output["x"]
        y2 = self.output["y"]

        self.ui_edf.horizontalSliderRtOnset.setMaximum(int(x2.max() * self.sample_rate))
        self.ui_edf.horizontalSliderRtOnset.setMinimum(int(x2.min() * self.sample_rate))

        rtonset = self.ui_edf.horizontalSliderRtOnset.value() / self.sample_rate


        # plot origininal trace
        self.p1.plot(x2, y, pen=(255, 0, 0), name="Green curve", clear=True)
        self.p1.plot([rtonset, rtonset], [0, y.max()], pen=pg.mkPen('m', width=2))
        text = pg.TextItem(
            html=f'<div style="text-align: center"><span style="color: #FFF;font-size: 16pt;">{self.current_ch}</span></div>',
            anchor=(0.5, 0.5))
        self.p1.addItem(text)

        # plot output trace
        self.p2.plot(x2, y2, pen=(0, 255, 0), name="Gr curve", clear=True)
        self.p2.plot([rtonset, rtonset], [0, y2.max()], pen=pg.mkPen('m', width=2))

        # plot fsr trace on the output trace
        sync = self.ui_edf.spinBoxSyncAnalogEDF.value()
        analog_trace = self.csv_dct[self.current_ch_index + sync]
        analog_trace = analog_trace[analog_trace.time < 1]
        x_fsr = analog_trace.time.values
        y_fsr = analog_trace.fsr.values
        y_fsr = y_fsr * y2.max()  # normalize
        self.p2.plot(x_fsr, y_fsr, pen=(0, 50, 200))

        # plot button trace on the output trace
        sync = self.ui_edf.spinBoxSyncAnalogEDF.value()
        x_button = analog_trace.time.values
        y_button = analog_trace.button.values
        y_button = y_button * y2.max()  # normalize
        self.p2.plot(x_button, y_button, pen=(200, 50, 100))

    def sync_analog_edf(self):
        self.update_rt_plot()

    def save_rt(self):
        self.rts_dct[self.current_ch] = [self.ui_edf.spinBoxRtOnset.value(), ]
        self.rts_df = pd.DataFrame(self.rts_dct)
        self.rts_df=self.rts_df.transpose()
        self.model = PandasModel(self.rts_df)
        self.ui_edf.tableViewRTS_plot_window.setModel(self.model)
        self.ui.tableView.setModel(self.model)
        #self.ui_edf.tableViewRTS_plot_window.verticalScrollBar().setValue(self.ui_edf.tableViewRTS_plot_window.verticalScrollBar().maximum())
        self.backup_rt_to_file()
        QTimer.singleShot(100, lambda: self.ui_edf.tableViewRTS_plot_window.scrollToBottom())

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
        self.edf_Sr = self.TKO(self.edf_Sr)
        self.update_rt_plot()

    def mne_filter(self):
        self.update_rt_plot()

    def channel_forw(self):
        if self.current_ch_index < len(self.edf_raw.ch_names):
            self.current_ch = self.edf_raw.ch_names[self.current_ch_index]
            self.current_ch_index += 1
        else:
            self.current_ch_index = 0

        print(self.current_ch_index)

        self.update_rt_plot()
        self.need_to_filter=True
        if self.current_ch in self.rts_df.index:
            self.ui_edf.spinBoxRtOnset.setValue(self.rts_df.loc[self.current_ch,0])
            print(self.ui_edf.spinBoxRtOnset.value())
        self.autoscale()

    def channel_backw(self):
        if self.current_ch_index >= 0:
            self.current_ch = self.edf_raw.ch_names[self.current_ch_index]
            self.current_ch_index -= 1
        else:
            self.current_ch_index = len(self.edf_raw.ch_names) - 1

        print(self.current_ch_index)
        self.update_rt_plot()
        self.need_to_filter = True
        if self.current_ch in self.rts_df.index:
            self.ui_edf.spinBoxRtOnset.setValue(self.rts_df.loc[self.current_ch,0])
        self.autoscale()

    def no_rt(self):
        self.ui_edf.spinBoxRtOnset.setValue(0)
        self.ui_edf.horizontalSliderRtOnset.setValue(0)

    def show_edf_plot_window(self):
        self.DialogAnalog.show()
        self.signal_pipeline()
        self.update_rt_plot()

    def mouse_clicked(self, event):
        print("knöknk")
        print(f"{event.pos().x}  {event.pos().y}")

    def df_to_sr(self):
        self.current_ch = self.edf_raw.ch_names[self.current_ch_index]
        self.edf_Sr = self.edf_df[self.current_ch]
        self.edf_Sr_original = self.edf_Sr
        self.ui_edf.horizontalSliderRtOnset.setMaximum(self.edf_Sr.index.max())
        self.ui_edf.horizontalSliderRtOnset.setMinimum(self.edf_Sr.index.min())

    def backup_rt_to_file(self):
        pathname=os.path.dirname(self.fileNameCSV)
        backup_path=os.path.join(pathname,"backup")
        if not os.path.exists(backup_path):
            try:
                os.mkdir(backup_path)
            except Exception as e:
                print(e)

        now=datetime.datetime.now().strftime("%Y%m%d_%H")
        bk_file_base=f"bk_{now}_"+os.path.basename(self.fileNameCSV)
        bk_file_path=os.path.join(backup_path,bk_file_base)
        print(bk_file_path)
        self.rts_df.to_csv(bk_file_path)

    def save_rt_to_file(self):

        #options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(None, "Save File", "", "CSV Files (*.csv);;All Files (*)",options=self.options)
        if fileName:
            print(fileName)
            try:
                self.rts_df.to_csv(fileName)
            except Exception as e:
                print("file save error : ")

    def autoscale(self):
        self.p1.autoRange()
        self.p2.autoRange()




# table view

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    pg.SignalProxy(w.p2.scene().sigMouseClicked, rateLimit=60, slot=w.mouse_clicked)
    w.show()
    sys.exit(app.exec_())
