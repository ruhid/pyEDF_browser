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
        DialogAnalog.resize(802, 751)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        DialogAnalog.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(DialogAnalog)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_2 = QtWidgets.QSplitter(DialogAnalog)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.widget = QtWidgets.QWidget(self.splitter_2)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graphicsView = GraphicsLayoutWidget(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.graphicsView.setFont(font)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.horizontalSliderRtOnset = QtWidgets.QSlider(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.horizontalSliderRtOnset.setFont(font)
        self.horizontalSliderRtOnset.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderRtOnset.setObjectName("horizontalSliderRtOnset")
        self.verticalLayout_2.addWidget(self.horizontalSliderRtOnset)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonBackward = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonBackward.setFont(font)
        self.pushButtonBackward.setObjectName("pushButtonBackward")
        self.horizontalLayout.addWidget(self.pushButtonBackward)
        self.spinBoxRtOnset = QtWidgets.QSpinBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.spinBoxRtOnset.setFont(font)
        self.spinBoxRtOnset.setMinimum(0)
        self.spinBoxRtOnset.setMaximum(100000)
        self.spinBoxRtOnset.setSingleStep(100)
        self.spinBoxRtOnset.setProperty("value", 0)
        self.spinBoxRtOnset.setObjectName("spinBoxRtOnset")
        self.horizontalLayout.addWidget(self.spinBoxRtOnset)
        self.pushButtonSaveRT = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSaveRT.setFont(font)
        self.pushButtonSaveRT.setFlat(False)
        self.pushButtonSaveRT.setObjectName("pushButtonSaveRT")
        self.horizontalLayout.addWidget(self.pushButtonSaveRT)
        self.pushButtonNoRT = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonNoRT.setFont(font)
        self.pushButtonNoRT.setObjectName("pushButtonNoRT")
        self.horizontalLayout.addWidget(self.pushButtonNoRT)
        self.pushButtonForward = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonForward.setFont(font)
        self.pushButtonForward.setObjectName("pushButtonForward")
        self.horizontalLayout.addWidget(self.pushButtonForward)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonAmpP = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAmpP.setFont(font)
        self.pushButtonAmpP.setObjectName("pushButtonAmpP")
        self.verticalLayout.addWidget(self.pushButtonAmpP)
        self.pushButtonAmpM = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAmpM.setFont(font)
        self.pushButtonAmpM.setObjectName("pushButtonAmpM")
        self.verticalLayout.addWidget(self.pushButtonAmpM)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.checkBoxFilt = QtWidgets.QCheckBox(self.widget1)
        self.checkBoxFilt.setObjectName("checkBoxFilt")
        self.gridLayout_2.addWidget(self.checkBoxFilt, 0, 0, 1, 1)
        self.spinBoxFiltHc = QtWidgets.QSpinBox(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.spinBoxFiltHc.setFont(font)
        self.spinBoxFiltHc.setMinimum(100)
        self.spinBoxFiltHc.setMaximum(50000)
        self.spinBoxFiltHc.setSingleStep(10)
        self.spinBoxFiltHc.setProperty("value", 1000)
        self.spinBoxFiltHc.setObjectName("spinBoxFiltHc")
        self.gridLayout_2.addWidget(self.spinBoxFiltHc, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.spinBoxFiltLc = QtWidgets.QSpinBox(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.spinBoxFiltLc.setFont(font)
        self.spinBoxFiltLc.setMinimum(0)
        self.spinBoxFiltLc.setMaximum(50000)
        self.spinBoxFiltLc.setObjectName("spinBoxFiltLc")
        self.gridLayout_2.addWidget(self.spinBoxFiltLc, 1, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.spinBoxSyncAnalogEDF = QtWidgets.QSpinBox(self.widget1)
        self.spinBoxSyncAnalogEDF.setMinimum(-3)
        self.spinBoxSyncAnalogEDF.setMaximum(3)
        self.spinBoxSyncAnalogEDF.setObjectName("spinBoxSyncAnalogEDF")
        self.verticalLayout_3.addWidget(self.spinBoxSyncAnalogEDF)
        self.checkBoxRect = QtWidgets.QCheckBox(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.checkBoxRect.setFont(font)
        self.checkBoxRect.setObjectName("checkBoxRect")
        self.verticalLayout_3.addWidget(self.checkBoxRect)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBoxTKEO = QtWidgets.QCheckBox(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.checkBoxTKEO.setFont(font)
        self.checkBoxTKEO.setObjectName("checkBoxTKEO")
        self.horizontalLayout_2.addWidget(self.checkBoxTKEO)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.checkBoxTKEORect = QtWidgets.QCheckBox(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.checkBoxTKEORect.setFont(font)
        self.checkBoxTKEORect.setObjectName("checkBoxTKEORect")
        self.horizontalLayout_2.addWidget(self.checkBoxTKEORect)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.pushButtonOrig = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonOrig.setFont(font)
        self.pushButtonOrig.setObjectName("pushButtonOrig")
        self.verticalLayout_3.addWidget(self.pushButtonOrig)
        self.plainTextEditNote = QtWidgets.QPlainTextEdit(self.widget1)
        self.plainTextEditNote.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.plainTextEditNote.setFont(font)
        self.plainTextEditNote.setObjectName("plainTextEditNote")
        self.verticalLayout_3.addWidget(self.plainTextEditNote)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.tableViewRTS_plot_window = QtWidgets.QTableView(self.splitter)
        self.tableViewRTS_plot_window.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableViewRTS_plot_window.setFont(font)
        self.tableViewRTS_plot_window.setObjectName("tableViewRTS_plot_window")
        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)

        self.retranslateUi(DialogAnalog)
        self.horizontalSliderRtOnset.sliderMoved['int'].connect(self.spinBoxRtOnset.setValue) # type: ignore
        self.spinBoxRtOnset.valueChanged['int'].connect(self.horizontalSliderRtOnset.setValue) # type: ignore
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
        self.pushButtonAmpP.setText(_translate("DialogAnalog", "AMP +"))
        self.pushButtonAmpM.setText(_translate("DialogAnalog", "AMP-"))
        self.label_2.setText(_translate("DialogAnalog", "High cut"))
        self.checkBoxFilt.setText(_translate("DialogAnalog", "Filt"))
        self.label.setText(_translate("DialogAnalog", "Low Cut"))
        self.checkBoxRect.setText(_translate("DialogAnalog", "RECT"))
        self.checkBoxTKEO.setText(_translate("DialogAnalog", "TKEO"))
        self.label_3.setText(_translate("DialogAnalog", "+"))
        self.checkBoxTKEORect.setText(_translate("DialogAnalog", "RECT"))
        self.pushButtonOrig.setText(_translate("DialogAnalog", "ORIGINAL"))
        self.plainTextEditNote.setPlainText(_translate("DialogAnalog", "include"))
from pyqtgraph import GraphicsLayoutWidget
