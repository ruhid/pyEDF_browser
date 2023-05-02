# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot_edf.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogAnalog(object):
    def setupUi(self, DialogAnalog):
        DialogAnalog.setObjectName("DialogAnalog")
        DialogAnalog.resize(1125, 751)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        DialogAnalog.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(DialogAnalog)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.splitter.setFont(font)
        self.splitter.setLineWidth(2)
        self.splitter.setMidLineWidth(2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(10)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.graphicsView = GraphicsLayoutWidget(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.graphicsView.setFont(font)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_4.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.horizontalSliderRtOnset = QtWidgets.QSlider(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.horizontalSliderRtOnset.setFont(font)
        self.horizontalSliderRtOnset.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderRtOnset.setObjectName("horizontalSliderRtOnset")
        self.gridLayout_4.addWidget(self.horizontalSliderRtOnset, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonBackward = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonBackward.setFont(font)
        self.pushButtonBackward.setObjectName("pushButtonBackward")
        self.horizontalLayout.addWidget(self.pushButtonBackward)
        self.spinBoxRtOnset = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.spinBoxRtOnset.setFont(font)
        self.spinBoxRtOnset.setMinimum(0)
        self.spinBoxRtOnset.setMaximum(100000)
        self.spinBoxRtOnset.setSingleStep(100)
        self.spinBoxRtOnset.setProperty("value", 0)
        self.spinBoxRtOnset.setObjectName("spinBoxRtOnset")
        self.horizontalLayout.addWidget(self.spinBoxRtOnset)
        self.pushButtonSaveRT = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSaveRT.setFont(font)
        self.pushButtonSaveRT.setFlat(False)
        self.pushButtonSaveRT.setObjectName("pushButtonSaveRT")
        self.horizontalLayout.addWidget(self.pushButtonSaveRT)
        self.pushButtonNoRT = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonNoRT.setFont(font)
        self.pushButtonNoRT.setObjectName("pushButtonNoRT")
        self.horizontalLayout.addWidget(self.pushButtonNoRT)
        self.pushButtonForward = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonForward.setFont(font)
        self.pushButtonForward.setObjectName("pushButtonForward")
        self.horizontalLayout.addWidget(self.pushButtonForward)
        self.gridLayout_4.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.tableViewRTS_plot_window = QtWidgets.QTableView(self.splitter)
        self.tableViewRTS_plot_window.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableViewRTS_plot_window.setFont(font)
        self.tableViewRTS_plot_window.setObjectName("tableViewRTS_plot_window")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_7 = QtWidgets.QLabel(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 0, 7, 4, 1)
        self.spinBoxFiltHc = QtWidgets.QSpinBox(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.spinBoxFiltHc.setFont(font)
        self.spinBoxFiltHc.setMinimum(100)
        self.spinBoxFiltHc.setMaximum(50000)
        self.spinBoxFiltHc.setSingleStep(10)
        self.spinBoxFiltHc.setProperty("value", 1000)
        self.spinBoxFiltHc.setObjectName("spinBoxFiltHc")
        self.gridLayout_3.addWidget(self.spinBoxFiltHc, 2, 9, 1, 1)
        self.checkBoxFilt = QtWidgets.QCheckBox(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBoxFilt.setFont(font)
        self.checkBoxFilt.setObjectName("checkBoxFilt")
        self.gridLayout_3.addWidget(self.checkBoxFilt, 0, 9, 1, 1)
        self.spinBoxReshapeY = QtWidgets.QSpinBox(DialogAnalog)
        self.spinBoxReshapeY.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.spinBoxReshapeY.setFont(font)
        self.spinBoxReshapeY.setMaximum(10000)
        self.spinBoxReshapeY.setProperty("value", 100)
        self.spinBoxReshapeY.setObjectName("spinBoxReshapeY")
        self.gridLayout_3.addWidget(self.spinBoxReshapeY, 0, 2, 1, 1)
        self.spinBoxMwAvgWind = QtWidgets.QSpinBox(DialogAnalog)
        self.spinBoxMwAvgWind.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.spinBoxMwAvgWind.setFont(font)
        self.spinBoxMwAvgWind.setProperty("value", 10)
        self.spinBoxMwAvgWind.setObjectName("spinBoxMwAvgWind")
        self.gridLayout_3.addWidget(self.spinBoxMwAvgWind, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 2, 8, 1, 1)
        self.spinBoxTrsDctStart = QtWidgets.QSpinBox(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.spinBoxTrsDctStart.setFont(font)
        self.spinBoxTrsDctStart.setMaximum(10000)
        self.spinBoxTrsDctStart.setProperty("value", 200)
        self.spinBoxTrsDctStart.setObjectName("spinBoxTrsDctStart")
        self.gridLayout_3.addWidget(self.spinBoxTrsDctStart, 3, 2, 1, 1)
        self.pushButtonOrig = QtWidgets.QPushButton(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonOrig.setFont(font)
        self.pushButtonOrig.setObjectName("pushButtonOrig")
        self.gridLayout_3.addWidget(self.pushButtonOrig, 3, 8, 1, 1)
        self.checkBoxTKEO = QtWidgets.QCheckBox(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBoxTKEO.setFont(font)
        self.checkBoxTKEO.setChecked(True)
        self.checkBoxTKEO.setObjectName("checkBoxTKEO")
        self.gridLayout_3.addWidget(self.checkBoxTKEO, 2, 6, 1, 1)
        self.label_3 = QtWidgets.QLabel(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 3, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 0, 5, 4, 1)
        self.label = QtWidgets.QLabel(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 8, 1, 1)
        self.label_4 = QtWidgets.QLabel(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 1, 1, 1)
        self.spinBoxAnzRTStart = QtWidgets.QSpinBox(DialogAnalog)
        self.spinBoxAnzRTStart.setMinimumSize(QtCore.QSize(100, 0))
        self.spinBoxAnzRTStart.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.spinBoxAnzRTStart.setFont(font)
        self.spinBoxAnzRTStart.setObjectName("spinBoxAnzRTStart")
        self.gridLayout_3.addWidget(self.spinBoxAnzRTStart, 2, 0, 1, 1)
        self.spinBoxSyncAnalogEDF = QtWidgets.QSpinBox(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.spinBoxSyncAnalogEDF.setFont(font)
        self.spinBoxSyncAnalogEDF.setMinimum(-3)
        self.spinBoxSyncAnalogEDF.setMaximum(3)
        self.spinBoxSyncAnalogEDF.setObjectName("spinBoxSyncAnalogEDF")
        self.gridLayout_3.addWidget(self.spinBoxSyncAnalogEDF, 3, 9, 1, 1)
        self.spinBoxAnzRtEnd = QtWidgets.QSpinBox(DialogAnalog)
        self.spinBoxAnzRtEnd.setMinimumSize(QtCore.QSize(100, 0))
        self.spinBoxAnzRtEnd.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.spinBoxAnzRtEnd.setFont(font)
        self.spinBoxAnzRtEnd.setMaximum(300)
        self.spinBoxAnzRtEnd.setProperty("value", 100)
        self.spinBoxAnzRtEnd.setObjectName("spinBoxAnzRtEnd")
        self.gridLayout_3.addWidget(self.spinBoxAnzRtEnd, 2, 2, 1, 1)
        self.checkBoxRect = QtWidgets.QCheckBox(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBoxRect.setFont(font)
        self.checkBoxRect.setChecked(True)
        self.checkBoxRect.setTristate(False)
        self.checkBoxRect.setObjectName("checkBoxRect")
        self.gridLayout_3.addWidget(self.checkBoxRect, 1, 6, 1, 1)
        self.checkBoxTKEORect = QtWidgets.QCheckBox(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBoxTKEORect.setFont(font)
        self.checkBoxTKEORect.setChecked(True)
        self.checkBoxTKEORect.setObjectName("checkBoxTKEORect")
        self.gridLayout_3.addWidget(self.checkBoxTKEORect, 3, 6, 1, 1)
        self.plainTextEditNote = QtWidgets.QTextEdit(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEditNote.setFont(font)
        self.plainTextEditNote.setObjectName("plainTextEditNote")
        self.gridLayout_3.addWidget(self.plainTextEditNote, 0, 11, 4, 1)
        self.spinBoxFiltLc = QtWidgets.QSpinBox(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.spinBoxFiltLc.setFont(font)
        self.spinBoxFiltLc.setMinimum(0)
        self.spinBoxFiltLc.setMaximum(50000)
        self.spinBoxFiltLc.setProperty("value", 100)
        self.spinBoxFiltLc.setObjectName("spinBoxFiltLc")
        self.gridLayout_3.addWidget(self.spinBoxFiltLc, 1, 9, 1, 1)
        self.line = QtWidgets.QFrame(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 0, 10, 4, 1)
        self.label_5 = QtWidgets.QLabel(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 1, 1, 1)
        self.labelReshapeX = QtWidgets.QLabel(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelReshapeX.setFont(font)
        self.labelReshapeX.setObjectName("labelReshapeX")
        self.gridLayout_3.addWidget(self.labelReshapeX, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 3, 1, 1)
        self.doubleSpinBoxWindPrct = QtWidgets.QDoubleSpinBox(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.doubleSpinBoxWindPrct.setFont(font)
        self.doubleSpinBoxWindPrct.setMaximum(1.0)
        self.doubleSpinBoxWindPrct.setSingleStep(0.01)
        self.doubleSpinBoxWindPrct.setProperty("value", 0.3)
        self.doubleSpinBoxWindPrct.setObjectName("doubleSpinBoxWindPrct")
        self.gridLayout_3.addWidget(self.doubleSpinBoxWindPrct, 0, 4, 1, 1)
        self.labelStd = QtWidgets.QLabel(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelStd.setFont(font)
        self.labelStd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelStd.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelStd.setObjectName("labelStd")
        self.gridLayout_3.addWidget(self.labelStd, 1, 3, 1, 1)
        self.spinBoxTimesStd = QtWidgets.QSpinBox(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.spinBoxTimesStd.setFont(font)
        self.spinBoxTimesStd.setProperty("value", 5)
        self.spinBoxTimesStd.setObjectName("spinBoxTimesStd")
        self.gridLayout_3.addWidget(self.spinBoxTimesStd, 1, 4, 1, 1)
        self.pushButtonDetectRT = QtWidgets.QPushButton(DialogAnalog)
        self.pushButtonDetectRT.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButtonDetectRT.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonDetectRT.setFont(font)
        self.pushButtonDetectRT.setObjectName("pushButtonDetectRT")
        self.gridLayout_3.addWidget(self.pushButtonDetectRT, 2, 3, 1, 1)
        self.checkBoxAutoDetect = QtWidgets.QCheckBox(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBoxAutoDetect.setFont(font)
        self.checkBoxAutoDetect.setObjectName("checkBoxAutoDetect")
        self.gridLayout_3.addWidget(self.checkBoxAutoDetect, 2, 4, 1, 1)
        self.checkBoxAutoSet = QtWidgets.QCheckBox(DialogAnalog)
        self.checkBoxAutoSet.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBoxAutoSet.setFont(font)
        self.checkBoxAutoSet.setObjectName("checkBoxAutoSet")
        self.gridLayout_3.addWidget(self.checkBoxAutoSet, 3, 4, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 10)

        self.retranslateUi(DialogAnalog)
        self.horizontalSliderRtOnset.sliderMoved['int'].connect(self.spinBoxRtOnset.setValue) # type: ignore
        self.spinBoxRtOnset.valueChanged['int'].connect(self.horizontalSliderRtOnset.setValue) # type: ignore
        self.checkBoxAutoDetect.clicked['bool'].connect(self.checkBoxAutoSet.setEnabled) # type: ignore
        self.checkBoxAutoDetect.clicked['bool'].connect(self.checkBoxAutoSet.setChecked) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DialogAnalog)

    def retranslateUi(self, DialogAnalog):
        _translate = QtCore.QCoreApplication.translate
        DialogAnalog.setWindowTitle(_translate("DialogAnalog", "Dialog"))
        self.pushButtonBackward.setText(_translate("DialogAnalog", "<<"))
        self.pushButtonBackward.setShortcut(_translate("DialogAnalog", "Left"))
        self.pushButtonSaveRT.setText(_translate("DialogAnalog", "SAVE RT"))
        self.pushButtonSaveRT.setShortcut(_translate("DialogAnalog", "Return"))
        self.pushButtonNoRT.setText(_translate("DialogAnalog", "NO RT"))
        self.pushButtonNoRT.setShortcut(_translate("DialogAnalog", "N"))
        self.pushButtonForward.setText(_translate("DialogAnalog", ">>"))
        self.pushButtonForward.setShortcut(_translate("DialogAnalog", "Ctrl+S"))
        self.label_7.setText(_translate("DialogAnalog", "Moving Avarage Window :"))
        self.checkBoxFilt.setText(_translate("DialogAnalog", "Filt"))
        self.label_2.setText(_translate("DialogAnalog", "High cut"))
        self.pushButtonOrig.setText(_translate("DialogAnalog", "ORIGINAL"))
        self.checkBoxTKEO.setText(_translate("DialogAnalog", "TKEO"))
        self.label_3.setText(_translate("DialogAnalog", "Treshold Detect Start"))
        self.label.setText(_translate("DialogAnalog", "Low Cut"))
        self.label_4.setText(_translate("DialogAnalog", "<< Analyze Epoch (ms) >>"))
        self.checkBoxRect.setText(_translate("DialogAnalog", "RECT"))
        self.checkBoxTKEORect.setText(_translate("DialogAnalog", "TKO RECT"))
        self.label_5.setText(_translate("DialogAnalog", "< X Reshape Y >"))
        self.labelReshapeX.setText(_translate("DialogAnalog", "0"))
        self.label_8.setText(_translate("DialogAnalog", "Window Percent :"))
        self.labelStd.setText(_translate("DialogAnalog", "Std *"))
        self.pushButtonDetectRT.setText(_translate("DialogAnalog", "DETECT RT"))
        self.checkBoxAutoDetect.setText(_translate("DialogAnalog", "Auto Detect"))
        self.checkBoxAutoSet.setText(_translate("DialogAnalog", "Auto Set"))
from pyqtgraph import GraphicsLayoutWidget
