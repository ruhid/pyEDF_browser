# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rand.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1361, 650)
        Dialog.setMinimumSize(QtCore.QSize(100, 0))
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 210, 1027, 246))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(1, 0, 1, 1)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comboBoxPorts = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBoxPorts.setMinimumSize(QtCore.QSize(100, 10))
        self.comboBoxPorts.setObjectName("comboBoxPorts")
        self.horizontalLayout_3.addWidget(self.comboBoxPorts)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButtonrefreshcoms = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonrefreshcoms.setObjectName("pushButtonrefreshcoms")
        self.horizontalLayout_3.addWidget(self.pushButtonrefreshcoms)
        self.horizontalLayout_3.setStretch(0, 30)
        self.horizontalLayout_3.setStretch(2, 10)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalSliderred = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSliderred.setMinimumSize(QtCore.QSize(400, 50))
        self.horizontalSliderred.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderred.setObjectName("horizontalSliderred")
        self.horizontalLayout_7.addWidget(self.horizontalSliderred)
        self.lcdNumberred = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcdNumberred.setMinimumSize(QtCore.QSize(100, 50))
        self.lcdNumberred.setObjectName("lcdNumberred")
        self.horizontalLayout_7.addWidget(self.lcdNumberred)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSlidergreen = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSlidergreen.setMinimumSize(QtCore.QSize(400, 50))
        self.horizontalSlidergreen.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlidergreen.setObjectName("horizontalSlidergreen")
        self.horizontalLayout.addWidget(self.horizontalSlidergreen)
        self.lcdNumbergreen = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcdNumbergreen.setMinimumSize(QtCore.QSize(100, 50))
        self.lcdNumbergreen.setObjectName("lcdNumbergreen")
        self.horizontalLayout.addWidget(self.lcdNumbergreen)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalSliderblue = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSliderblue.setMinimumSize(QtCore.QSize(400, 50))
        self.horizontalSliderblue.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderblue.setObjectName("horizontalSliderblue")
        self.horizontalLayout_9.addWidget(self.horizontalSliderblue)
        self.lcdNumbeblue = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcdNumbeblue.setMinimumSize(QtCore.QSize(100, 50))
        self.lcdNumbeblue.setObjectName("lcdNumbeblue")
        self.horizontalLayout_9.addWidget(self.lcdNumbeblue)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButtonStartBlinks = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonStartBlinks.setObjectName("pushButtonStartBlinks")
        self.horizontalLayout_4.addWidget(self.pushButtonStartBlinks)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.spinBoxcount = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBoxcount.setObjectName("spinBoxcount")
        self.horizontalLayout_4.addWidget(self.spinBoxcount)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.doubleSpinBoxdelay = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxdelay.setObjectName("doubleSpinBoxdelay")
        self.horizontalLayout_4.addWidget(self.doubleSpinBoxdelay)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 5)
        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayout_4.setStretch(3, 1)
        self.horizontalLayout_4.setStretch(5, 1)
        self.horizontalLayout_4.setStretch(6, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonrefreshcoms.setText(_translate("Dialog", "REFRESH COM PORTS"))
        self.pushButtonStartBlinks.setText(_translate("Dialog", "Start Blinks"))
        self.label_2.setText(_translate("Dialog", "Counts"))
        self.label.setText(_translate("Dialog", "Delay"))
