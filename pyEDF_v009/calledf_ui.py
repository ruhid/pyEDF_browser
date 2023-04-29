import datetime
import sys

import PyQt5
import pyfirmata
from PyQt5.QtCore import QAbstractTableModel, QVariant, Qt, QTimer, QModelIndex, QItemSelectionModel
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem, QFileDialog, QMainWindow, QMessageBox, QLabel, \
    QGraphicsColorizeEffect, QAbstractItemView, QHeaderView
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
import traceback
os.environ["QT_MAC_WANTS_LAYER"] = "1"
#


class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonPlot.clicked.connect(self.show_edf_plot_window)
        self.ui.pushButtonFile.clicked.connect(self.load_edf)
        self.ui.pushButtonOpenCsv.clicked.connect(self.load_csv)
        self.ui.pushButtonSaveRtToFile.clicked.connect(self.save_rt_to_file)
        self.ui.pushButtonLoadRTcsv.clicked.connect(self.load_rts_csv)
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
        self.ui_edf.pushButtonDetectRT.clicked.connect(self.rt_trshold_onset_detect)
        self.ui_edf.checkBoxAutoDetect.clicked.connect(self.set_auto_rt)
        self.p1 = self.ui_edf.graphicsView.addPlot(row=0, col=0)
        self.p2 = self.ui_edf.graphicsView.addPlot(row=1, col=0)
        self.current_ch_index = 0
        self.sample_rate = 100000
        self.need_to_filter = True
        self.rts_dct = {}
        self.options = QFileDialog.Options()
        # self.ui_edf.graphicsView.sigMouseReleased.connect(self.mouse_clicked)
        self.show()

    def load_edf(self):
        try:
            self.fileNameEDF, OK = QFileDialog.getOpenFileName(self, 'Open file', "", "EDF files (*.edf)",
                                                               options=self.options)
            if OK:
                self.default_dir = os.path.dirname(self.fileNameEDF)
                self.ui.labelEDFFile.setText(self.fileNameEDF)
                self.read_original()
        except Exception as e:
            # display a message box with the error information
            error_message = f"An error occurred: {str(e)}\n\nTraceback:\n{traceback.format_exc()}"
            QMessageBox.critical(None, "Error", error_message)

    def read_original(self):
        self.edf_raw = mne.io.read_raw_edf(self.fileNameEDF, preload=True)
        self.edf_df_original = self.edf_raw.to_data_frame()

        # create rts dataframe
        data = {"trace": self.edf_raw.ch_names,
                "rt": np.zeros(len(self.edf_raw.ch_names)),
                "color": ["r" for i in range(len(self.edf_raw.ch_names))],
                "button": np.zeros(len(self.edf_raw.ch_names)),
                "fsr": np.zeros(len(self.edf_raw.ch_names)),
                "note": ["" for i in range(len(self.edf_raw.ch_names))],
                "auto_rt":np.zeros(len(self.edf_raw.ch_names))}
        self.rts_df = pd.DataFrame(data, columns=["trace", "rt", "color", "button", "fsr", "note"])
        self.rts_df.set_index("trace", inplace=True)

        self.current_ch = self.edf_raw.ch_names[self.current_ch_index]
        self.update_rt_plot()

    def load_csv(self):
        try:
            self.fileNameCSV, OK = QFileDialog.getOpenFileName(self, 'Open file', "", "EDF files (*.csv)",
                                                               options=self.options)
            if OK:
                self.ui.labelEDFFile.setText(self.fileNameCSV)
                self.ad_fsr_button_data_to_df()
        except Exception as e:
            # display a message box with the error information
            error_message = f"An error occurred: {str(e)}\n\nTraceback:\n{traceback.format_exc()}"
            QMessageBox.critical(None, "Error", error_message)

    def load_rts_csv(self):

        try:
            self.RT_fileNameCSV, OK = QFileDialog.getOpenFileName(self, 'Open file', "", "EDF files (*.csv)",
                                                                  options=self.options)
            if OK:
                c = pd.read_csv(self.RT_fileNameCSV)
                c.set_index("trace", inplace=True)
                self.ui.labelEDFFile.setText(self.RT_fileNameCSV)
                for i in c.columns:
                    self.rts_df[i] = c[i]

        except Exception as e:
            # display a message box with the error information
            error_message = f"An error occurred: {str(e)}\n\nTraceback:\n{traceback.format_exc()}"
            QMessageBox.critical(None, "Error", error_message)

    def ad_fsr_button_data_to_df(self):
        self.csv_df = pd.read_csv(self.fileNameCSV)
        self.csv_dct = {i: data for i, data in self.csv_df.groupby("id")}

    def signal_pipeline(self):
        if self.ui_edf.checkBoxFilt.isChecked() and self.need_to_filter:
            l_freq = self.ui_edf.spinBoxFiltLc.value()
            h_freq = self.ui_edf.spinBoxFiltHc.value()
            self.edf_raw.filter(l_freq, h_freq)
            self.need_to_filter = False

        output_y = self.edf_raw[self.current_ch][0].T.reshape(-1)
        output_x = self.edf_raw[self.current_ch][1]

        if self.ui_edf.checkBoxRect.isChecked():
            output_y = np.abs(output_y)
        if self.ui_edf.checkBoxTKEO.isChecked():
            output_y = TKO(output_y)
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
        self.current_color = analog_trace.color.values[30]

        # detect button press onset
        if len(analog_trace[analog_trace.button > 0.1]):
            self.current_button_pres = analog_trace[analog_trace.button > 0.1].time.iloc[0]
        else:
            self.current_button_pres = 0

        # ad text
        text = pg.TextItem(
            html=f'<div style="text-align: right"><span style="color: #FFF;font-size: 16pt;">{self.current_ch} {self.current_color}</span></div>',
            anchor=(0.5, 0.5))
        self.p2.addItem(text)

        if self.ui_edf.checkBoxAutoDetect.isChecked():
            self.rt_trshold_onset_detect()

    def rt_trshold_onset_detect(self):
        reshapeY=self.ui_edf.spinBoxReshapeY.value()
        self.ui_edf.labelReshapeX.setText("")
        mov_avg_wind=self.ui_edf.spinBoxMwAvgWind.value()
        window_prct=self.ui_edf.doubleSpinBoxWindPrct.value()
        anlz_start=self.ui_edf.spinBoxAnzRTStart.value()
        anlz_end=self.ui_edf.spinBoxAnzRtEnd.value()
        times_std=self.ui_edf.spinBoxTimesStd.value()

        signal=self.output["y"]

        treshold=std_trshld(signal,
                            self.sample_rate,
                            pre_rt_time=[anlz_start,anlz_end],
                            times_std=times_std
                            )["treshold"]

        detect_start=self.ui_edf.spinBoxTrsDctStart.value()*self.sample_rate//1000
        onset=detect_trsh_rt(signal=signal[detect_start:],
                             treshold=treshold,
                             reshape=reshapeY,
                             mov_avg_window=mov_avg_wind,
                             mov_avg_window_prcnt=window_prct)

        onset=(onset+detect_start)/self.sample_rate
        print("detected onsert :" ,onset)
        try:
            self.p2.removeItem(self.trs_plot)
            self.p2.removeItem(self.auto_rt_plot)
            self.p2.removeItem(self.fill)

        except Exception as e:
            print("no plt item  ",e)
            pass


        self.trs_plot=self.p2.plot([self.ui_edf.spinBoxAnzRTStart.value()/1000,self.ui_edf.spinBoxAnzRtEnd.value()/1000],
                                   [treshold, treshold],
                                   pen=pg.mkPen(color=(255,255,0,50),
                                                width=2,
                                                style=QtCore.Qt.DashLine))

        baseline=self.p2.plot([self.ui_edf.spinBoxAnzRTStart.value()/1000,self.ui_edf.spinBoxAnzRtEnd.value()/1000],
                                   [0, 0],
                                   pen=pg.mkPen(color=(255,255,0,50),
                                                width=2,
                                                style=QtCore.Qt.DashLine))



        self.fill=pg.FillBetweenItem(self.trs_plot, baseline, brush=(255, 255, 0, 100))
        self.p2.addItem(self.fill)




        self.trs_plot_aft=self.p2.plot([self.ui_edf.spinBoxTrsDctStart.value()/1000,onset],
                                   [treshold, treshold],
                                   pen=pg.mkPen(color=(255,255,0,50),
                                                width=2,
                                                style=QtCore.Qt.DashLine))

        baseline_aft=self.p2.plot([self.ui_edf.spinBoxTrsDctStart.value()/1000,onset],
                                   [0, 0],
                                   pen=pg.mkPen(color=(255,255,0,50),
                                                width=2,
                                                style=QtCore.Qt.DashLine))


        self.fill_aft=pg.FillBetweenItem(self.trs_plot_aft, baseline_aft, brush=(255, 255, 0, 100))
        self.p2.addItem(self.fill_aft)

        self.auto_rt_plot=self.p2.plot([onset, onset],
                                       [0, signal.max()],
                                       pen=pg.mkPen('y', width=2))
        self.auto_rt=onset


    def set_auto_rt(self):
        if not self.ui_edf.checkBoxAutoDetect.isChecked():
            self.auto_rt=0

    def sync_analog_edf(self):
        self.update_rt_plot()

    def save_rt(self):
        self.rts_df.loc[self.current_ch, "rt"] = self.ui_edf.spinBoxRtOnset.value()
        self.rts_df.loc[self.current_ch, "color"] = self.current_color
        self.rts_df.loc[self.current_ch, "button"] = self.current_button_pres
        self.rts_df.loc[self.current_ch, "note"] = self.ui_edf.plainTextEditNote.toPlainText()
        self.rts_df.loc[self.current_ch, "auto_rt"]=self.auto_rt

        self.model = PandasModel(self.rts_df)
        self.ui_edf.tableViewRTS_plot_window.setModel(self.model)
        self.ui_edf.tableViewRTS_plot_window.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui_edf.tableViewRTS_plot_window.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui_edf.tableViewRTS_plot_window.setSelectionMode(QAbstractItemView.SingleSelection)
        # self.ui_edf.tableViewRTS_plot_window.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.ui.tableViewEdf_UI.setModel(self.model)
        # self.ui_edf.tableViewRTS_plot_window.verticalScrollBar().setValue(self.ui_edf.tableViewRTS_plot_window.verticalScrollBar().maximum())
        self.backup_rt_to_file()
        index = self.model.index(self.current_ch_index, 0, QModelIndex())
        self.ui_edf.tableViewRTS_plot_window.selectionModel().select(index, QItemSelectionModel.Select)
        self.ui_edf.tableViewRTS_plot_window.scrollTo(index, QAbstractItemView.PositionAtCenter)
        self.ui_edf.pushButtonForward.setFocus()
        QTimer.singleShot(100,
                          lambda: self.ui_edf.tableViewRTS_plot_window.scrollTo(index,
                                                                                QAbstractItemView.PositionAtCenter))

    def TKO_convert(self):
        self.edf_Sr = TKO(self.edf_Sr)
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
        self.need_to_filter = True


        if (self.current_ch in self.rts_df.index) and (self.rts_df.rt[self.current_ch]>0):
            self.ui_edf.spinBoxRtOnset.setValue(int(self.rts_df.loc[self.current_ch, "rt"]))
            print(self.ui_edf.spinBoxRtOnset.value())
        else:
            print("auto rt", self.auto_rt)
            if self.ui_edf.checkBoxAutoSet.isChecked():
                self.ui_edf.spinBoxRtOnset.setValue(int(self.auto_rt*self.sample_rate))
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

        if (self.current_ch in self.rts_df.index) and (self.rts_df.rt[self.current_ch] > 0):
            self.ui_edf.spinBoxRtOnset.setValue(int(self.rts_df.loc[self.current_ch, "rt"]))
            print(self.ui_edf.spinBoxRtOnset.value())
        else:
            print("auto rt", self.auto_rt)
            if self.ui_edf.checkBoxAutoSet.isChecked():
                self.ui_edf.spinBoxRtOnset.setValue(int(self.auto_rt * self.sample_rate))

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
        pathname = os.path.dirname(self.fileNameCSV)
        backup_path = os.path.join(pathname, "backup")
        if not os.path.exists(backup_path):
            try:
                os.mkdir(backup_path)
            except Exception as e:
                print(e)

        now = datetime.datetime.now().strftime("%Y%m%d_%H")
        bk_file_base = f"bk_{now}_" + os.path.basename(self.fileNameCSV)
        bk_file_path = os.path.join(backup_path, bk_file_base)
        print(bk_file_path)
        self.rts_df.to_csv(bk_file_path)

    def save_rt_to_file(self):

        # options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(None, "Save File", "", "CSV Files (*.csv);;All Files (*)",
                                                  options=self.options)
        if fileName:
            print(fileName)
            try:
                self.rts_df.to_csv(fileName)
            except Exception as e:
                # display a message box with the error information
                error_message = f"An error occurred: {str(e)}\n\nTraceback:\n{traceback.format_exc()}"
                QMessageBox.critical(None, "Error", error_message)

    def autoscale(self):
        self.p1.autoRange()
        self.p2.autoRange()


# general signal modifying functions

# TKO
def TKO(signal):
    windows = np.lib.stride_tricks.sliding_window_view(signal, 3)
    TKO = windows[:, 1] ** 2 - windows[:, 0] * windows[:, 2]
    try:
        return pd.Series(np.concatenate([np.zeros(1), TKO, np.zeros(1)]), index=signal.index)

    except Exception as E:
        print(E)
        print("returnin without index")
        return np.concatenate([np.zeros(1), TKO, np.zeros(1)])
# threshold rt onset detect

def detect_trsh_rt(signal, treshold, reshape, mov_avg_window=10, mov_avg_window_prcnt=0.3):
    rt_mov_avg_window_prcnt = (mov_avg_window_prcnt * mov_avg_window) // 1
    signal_reshape = signal.reshape(-1,reshape)
    signal_resample=signal_reshape.mean(axis=1)
    signal_resample_map = signal_resample > treshold
    signal_mov_avg = np.lib.stride_tricks.sliding_window_view(signal_resample_map, mov_avg_window)
    rt = (signal_mov_avg.sum(axis=1) > rt_mov_avg_window_prcnt).argmax()
    print("function rt:", rt, " shape", signal_reshape.shape, "shape avg: " ,signal_resample.shape)
    return rt * signal_reshape.shape[1]

# threshold calculating
def std_trshld(array, sample_rate, pre_rt_time=[0,100], times_std=10):
    sample_n_start = sample_rate * pre_rt_time[0] // 1000
    sample_n_end = sample_rate * pre_rt_time[1] // 1000
    c = array[sample_n_start:sample_n_end]
    c_abs = np.abs(c)
    c_abs_mean = np.abs(c_abs).mean()
    c_std = np.std(c)
    dct = {"pre_rt_array": c,
           "c_abs": c_abs,
           "c_abs_mena": c_abs_mean,
           "c_std": c_std,
           "treshold": c_abs_mean + times_std * c_std}
    return dct


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
