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
        DialogAnalog.resize(870, 747)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        DialogAnalog.setFont(font)
        self.gridLayout_3 = QtWidgets.QGridLayout(DialogAnalog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graphicsView = GraphicsLayoutWidget(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.graphicsView.setFont(font)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.horizontalSliderRtOnset = QtWidgets.QSlider(DialogAnalog)
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
        self.pushButtonBackward = QtWidgets.QPushButton(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonBackward.setFont(font)
        self.pushButtonBackward.setObjectName("pushButtonBackward")
        self.horizontalLayout.addWidget(self.pushButtonBackward)
        self.spinBoxRtOnset = QtWidgets.QSpinBox(DialogAnalog)
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
        self.pushButtonSaveRT = QtWidgets.QPushButton(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSaveRT.setFont(font)
        self.pushButtonSaveRT.setObjectName("pushButtonSaveRT")
        self.horizontalLayout.addWidget(self.pushButtonSaveRT)
        self.pushButtonForward = QtWidgets.QPushButton(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonForward.setFont(font)
        self.pushButtonForward.setObjectName("pushButtonForward")
        self.horizontalLayout.addWidget(self.pushButtonForward)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonAmpP = QtWidgets.QPushButton(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAmpP.setFont(font)
        self.pushButtonAmpP.setObjectName("pushButtonAmpP")
        self.verticalLayout.addWidget(self.pushButtonAmpP)
        self.pushButtonAmpM = QtWidgets.QPushButton(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAmpM.setFont(font)
        self.pushButtonAmpM.setObjectName("pushButtonAmpM")
        self.verticalLayout.addWidget(self.pushButtonAmpM)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.spinBoxFiltHc = QtWidgets.QSpinBox(DialogAnalog)
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
        self.label = QtWidgets.QLabel(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.spinBoxFiltLc = QtWidgets.QSpinBox(DialogAnalog)
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
        self.label_2 = QtWidgets.QLabel(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.pushButtonFilt = QtWidgets.QPushButton(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonFilt.setFont(font)
        self.pushButtonFilt.setObjectName("pushButtonFilt")
        self.gridLayout_2.addWidget(self.pushButtonFilt, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonTKEO = QtWidgets.QPushButton(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonTKEO.setFont(font)
        self.pushButtonTKEO.setObjectName("pushButtonTKEO")
        self.gridLayout.addWidget(self.pushButtonTKEO, 2, 0, 1, 1)
        self.checkBoxRect = QtWidgets.QCheckBox(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.checkBoxRect.setFont(font)
        self.checkBoxRect.setObjectName("checkBoxRect")
        self.gridLayout.addWidget(self.checkBoxRect, 1, 0, 1, 1)
        self.pushButtonOrig = QtWidgets.QPushButton(DialogAnalog)
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonOrig.setFont(font)
        self.pushButtonOrig.setObjectName("pushButtonOrig")
        self.gridLayout.addWidget(self.pushButtonOrig, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.tableViewRTS_plot_window = QtWidgets.QTableView(DialogAnalog)
        self.tableViewRTS_plot_window.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tableViewRTS_plot_window.setFont(font)
        self.tableViewRTS_plot_window.setObjectName("tableViewRTS_plot_window")
        self.gridLayout_3.addWidget(self.tableViewRTS_plot_window, 0, 2, 1, 1)

        self.retranslateUi(DialogAnalog)
        self.horizontalSliderRtOnset.sliderMoved['int'].connect(self.spinBoxRtOnset.setValue) # type: ignore
        self.spinBoxRtOnset.valueChanged['int'].connect(self.horizontalSliderRtOnset.setValue) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DialogAnalog)

    def retranslateUi(self, DialogAnalog):
        _translate = QtCore.QCoreApplication.translate
        DialogAnalog.setWindowTitle(_translate("DialogAnalog", "Dialog"))
        self.pushButtonBackward.setText(_translate("DialogAnalog", "<<"))
        self.pushButtonSaveRT.setText(_translate("DialogAnalog", "SAVE RT"))
        self.pushButtonForward.setText(_translate("DialogAnalog", ">>"))
        self.pushButtonAmpP.setText(_translate("DialogAnalog", "AMP +"))
        self.pushButtonAmpM.setText(_translate("DialogAnalog", "AMP-"))
        self.label.setText(_translate("DialogAnalog", "Low Cut"))
        self.label_2.setText(_translate("DialogAnalog", "High cut"))
        self.pushButtonFilt.setText(_translate("DialogAnalog", "Filter"))
        self.pushButtonTKEO.setText(_translate("DialogAnalog", "TKEO"))
        self.checkBoxRect.setText(_translate("DialogAnalog", "RECT"))
        self.pushButtonOrig.setText(_translate("DialogAnalog", "ORIGINAL"))
from pyqtgraph import GraphicsLayoutWidget
