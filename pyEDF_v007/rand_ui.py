# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'randQIxBkr.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1361, 650)
        Dialog.setMinimumSize(QSize(100, 0))
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(110, 210, 1027, 246))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(1, 0, 1, 1)
        self.comboBoxPorts = QComboBox(self.layoutWidget)
        self.comboBoxPorts.setObjectName(u"comboBoxPorts")
        self.comboBoxPorts.setMinimumSize(QSize(100, 10))

        self.horizontalLayout_3.addWidget(self.comboBoxPorts)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButtonrefreshcoms = QPushButton(self.layoutWidget)
        self.pushButtonrefreshcoms.setObjectName(u"pushButtonrefreshcoms")

        self.horizontalLayout_3.addWidget(self.pushButtonrefreshcoms)

        self.horizontalLayout_3.setStretch(0, 30)
        self.horizontalLayout_3.setStretch(2, 10)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSliderred = QSlider(self.layoutWidget)
        self.horizontalSliderred.setObjectName(u"horizontalSliderred")
        self.horizontalSliderred.setMinimumSize(QSize(400, 50))
        self.horizontalSliderred.setOrientation(Qt.Horizontal)

        self.horizontalLayout_7.addWidget(self.horizontalSliderred)

        self.lcdNumberred = QLCDNumber(self.layoutWidget)
        self.lcdNumberred.setObjectName(u"lcdNumberred")
        self.lcdNumberred.setMinimumSize(QSize(100, 50))

        self.horizontalLayout_7.addWidget(self.lcdNumberred)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSlidergreen = QSlider(self.layoutWidget)
        self.horizontalSlidergreen.setObjectName(u"horizontalSlidergreen")
        self.horizontalSlidergreen.setMinimumSize(QSize(400, 50))
        self.horizontalSlidergreen.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.horizontalSlidergreen)

        self.lcdNumbergreen = QLCDNumber(self.layoutWidget)
        self.lcdNumbergreen.setObjectName(u"lcdNumbergreen")
        self.lcdNumbergreen.setMinimumSize(QSize(100, 50))

        self.horizontalLayout.addWidget(self.lcdNumbergreen)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSliderblue = QSlider(self.layoutWidget)
        self.horizontalSliderblue.setObjectName(u"horizontalSliderblue")
        self.horizontalSliderblue.setMinimumSize(QSize(400, 50))
        self.horizontalSliderblue.setOrientation(Qt.Horizontal)

        self.horizontalLayout_9.addWidget(self.horizontalSliderblue)

        self.lcdNumbeblue = QLCDNumber(self.layoutWidget)
        self.lcdNumbeblue.setObjectName(u"lcdNumbeblue")
        self.lcdNumbeblue.setMinimumSize(QSize(100, 50))

        self.horizontalLayout_9.addWidget(self.lcdNumbeblue)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.pushButtonStartBlinks = QPushButton(self.layoutWidget)
        self.pushButtonStartBlinks.setObjectName(u"pushButtonStartBlinks")

        self.horizontalLayout_4.addWidget(self.pushButtonStartBlinks)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.spinBoxcount = QSpinBox(self.layoutWidget)
        self.spinBoxcount.setObjectName(u"spinBoxcount")

        self.horizontalLayout_4.addWidget(self.spinBoxcount)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.doubleSpinBoxdelay = QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxdelay.setObjectName(u"doubleSpinBoxdelay")

        self.horizontalLayout_4.addWidget(self.doubleSpinBoxdelay)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 5)
        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayout_4.setStretch(3, 1)
        self.horizontalLayout_4.setStretch(5, 1)
        self.horizontalLayout_4.setStretch(6, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButtonrefreshcoms.setText(QCoreApplication.translate("Dialog", u"REFRESH COM PORTS", None))
        self.pushButtonStartBlinks.setText(QCoreApplication.translate("Dialog", u"Start Blinks", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Counts", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Delay", None))
    # retranslateUi

