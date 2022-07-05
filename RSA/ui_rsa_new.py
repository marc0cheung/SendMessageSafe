# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rsa_newcSBSWm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(924, 705)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter_12 = QSplitter(self.centralwidget)
        self.splitter_12.setObjectName(u"splitter_12")
        self.splitter_12.setOrientation(Qt.Vertical)
        self.splitter_11 = QSplitter(self.splitter_12)
        self.splitter_11.setObjectName(u"splitter_11")
        self.splitter_11.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter_11)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.genKeyLabel = QLabel(self.widget)
        self.genKeyLabel.setObjectName(u"genKeyLabel")

        self.verticalLayout.addWidget(self.genKeyLabel)

        self.genKeyBtn = QPushButton(self.widget)
        self.genKeyBtn.setObjectName(u"genKeyBtn")
        self.genKeyBtn.setMinimumSize(QSize(341, 61))
        self.genKeyBtn.setMaximumSize(QSize(341, 16777215))

        self.verticalLayout.addWidget(self.genKeyBtn)

        self.splitter_11.addWidget(self.widget)
        self.widget1 = QWidget(self.splitter_11)
        self.widget1.setObjectName(u"widget1")
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.widget1)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.publicKeyLabel = QLabel(self.splitter)
        self.publicKeyLabel.setObjectName(u"publicKeyLabel")
        self.splitter.addWidget(self.publicKeyLabel)
        self.publicKeyBtn = QPushButton(self.splitter)
        self.publicKeyBtn.setObjectName(u"publicKeyBtn")
        self.splitter.addWidget(self.publicKeyBtn)

        self.verticalLayout_2.addWidget(self.splitter)

        self.splitter_2 = QSplitter(self.widget1)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.privateKeyLabel = QLabel(self.splitter_2)
        self.privateKeyLabel.setObjectName(u"privateKeyLabel")
        self.splitter_2.addWidget(self.privateKeyLabel)
        self.privateKeyBtn = QPushButton(self.splitter_2)
        self.privateKeyBtn.setObjectName(u"privateKeyBtn")
        self.splitter_2.addWidget(self.privateKeyBtn)

        self.verticalLayout_2.addWidget(self.splitter_2)

        self.splitter_11.addWidget(self.widget1)
        self.splitter_12.addWidget(self.splitter_11)
        self.splitter_10 = QSplitter(self.splitter_12)
        self.splitter_10.setObjectName(u"splitter_10")
        self.splitter_10.setOrientation(Qt.Horizontal)
        self.widget2 = QWidget(self.splitter_10)
        self.widget2.setObjectName(u"widget2")
        self.verticalLayout_3 = QVBoxLayout(self.widget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.splitter_5 = QSplitter(self.widget2)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Horizontal)
        self.splitter_4 = QSplitter(self.splitter_5)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Vertical)
        self.msgLabel = QLabel(self.splitter_4)
        self.msgLabel.setObjectName(u"msgLabel")
        self.splitter_4.addWidget(self.msgLabel)
        self.input = QTextEdit(self.splitter_4)
        self.input.setObjectName(u"input")
        self.splitter_4.addWidget(self.input)
        self.splitter_5.addWidget(self.splitter_4)
        self.splitter_3 = QSplitter(self.splitter_5)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Vertical)
        self.copyInputBtn = QPushButton(self.splitter_3)
        self.copyInputBtn.setObjectName(u"copyInputBtn")
        self.splitter_3.addWidget(self.copyInputBtn)
        self.pasteInputBtn = QPushButton(self.splitter_3)
        self.pasteInputBtn.setObjectName(u"pasteInputBtn")
        self.splitter_3.addWidget(self.pasteInputBtn)
        self.clearBtn = QPushButton(self.splitter_3)
        self.clearBtn.setObjectName(u"clearBtn")
        self.splitter_3.addWidget(self.clearBtn)
        self.splitter_5.addWidget(self.splitter_3)

        self.verticalLayout_3.addWidget(self.splitter_5)

        self.switchBtn = QPushButton(self.widget2)
        self.switchBtn.setObjectName(u"switchBtn")

        self.verticalLayout_3.addWidget(self.switchBtn)

        self.splitter_8 = QSplitter(self.widget2)
        self.splitter_8.setObjectName(u"splitter_8")
        self.splitter_8.setOrientation(Qt.Horizontal)
        self.splitter_6 = QSplitter(self.splitter_8)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setOrientation(Qt.Vertical)
        self.outputLabel = QLabel(self.splitter_6)
        self.outputLabel.setObjectName(u"outputLabel")
        self.splitter_6.addWidget(self.outputLabel)
        self.output = QTextEdit(self.splitter_6)
        self.output.setObjectName(u"output")
        self.splitter_6.addWidget(self.output)
        self.splitter_8.addWidget(self.splitter_6)
        self.splitter_7 = QSplitter(self.splitter_8)
        self.splitter_7.setObjectName(u"splitter_7")
        self.splitter_7.setOrientation(Qt.Vertical)
        self.copyOutputBtn = QPushButton(self.splitter_7)
        self.copyOutputBtn.setObjectName(u"copyOutputBtn")
        self.splitter_7.addWidget(self.copyOutputBtn)
        self.clearBtn_2 = QPushButton(self.splitter_7)
        self.clearBtn_2.setObjectName(u"clearBtn_2")
        self.splitter_7.addWidget(self.clearBtn_2)
        self.splitter_8.addWidget(self.splitter_7)

        self.verticalLayout_3.addWidget(self.splitter_8)

        self.splitter_10.addWidget(self.widget2)
        self.splitter_9 = QSplitter(self.splitter_10)
        self.splitter_9.setObjectName(u"splitter_9")
        self.splitter_9.setOrientation(Qt.Vertical)
        self.encryptBtn = QPushButton(self.splitter_9)
        self.encryptBtn.setObjectName(u"encryptBtn")
        self.splitter_9.addWidget(self.encryptBtn)
        self.decryptBtn = QPushButton(self.splitter_9)
        self.decryptBtn.setObjectName(u"decryptBtn")
        self.splitter_9.addWidget(self.decryptBtn)
        self.splitter_10.addWidget(self.splitter_9)
        self.splitter_12.addWidget(self.splitter_10)

        self.gridLayout.addWidget(self.splitter_12, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SendMessageSafe\uff08\u5b89\u5fc3\u50b3\u8a0a\uff09- RSA", None))
        self.genKeyLabel.setText(QCoreApplication.translate("MainWindow", u"Generate Public and Private Keys:", None))
        self.genKeyBtn.setText(QCoreApplication.translate("MainWindow", u"Generate RSA Public and Private Keys", None))
        self.publicKeyLabel.setText(QCoreApplication.translate("MainWindow", u"Select Public Key (.pem)", None))
        self.publicKeyBtn.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.privateKeyLabel.setText(QCoreApplication.translate("MainWindow", u"Select Private Key (.pem)", None))
        self.privateKeyBtn.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.msgLabel.setText(QCoreApplication.translate("MainWindow", u"Message:", None))
        self.copyInputBtn.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.pasteInputBtn.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.clearBtn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.switchBtn.setText(QCoreApplication.translate("MainWindow", u"\u21f5", None))
        self.outputLabel.setText(QCoreApplication.translate("MainWindow", u"Output:", None))
        self.copyOutputBtn.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.clearBtn_2.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.encryptBtn.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.decryptBtn.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
    # retranslateUi

