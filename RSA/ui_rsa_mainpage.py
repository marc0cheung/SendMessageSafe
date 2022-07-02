# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rsa_mainpagehPnRcu.ui'
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
        MainWindow.resize(800, 743)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.publicKeyBtn = QPushButton(self.centralwidget)
        self.publicKeyBtn.setObjectName(u"publicKeyBtn")
        self.publicKeyBtn.setGeometry(QRect(650, 160, 93, 41))
        self.publicKeyLabel = QLabel(self.centralwidget)
        self.publicKeyLabel.setObjectName(u"publicKeyLabel")
        self.publicKeyLabel.setGeometry(QRect(40, 160, 601, 16))
        self.privateKeyLabel = QLabel(self.centralwidget)
        self.privateKeyLabel.setObjectName(u"privateKeyLabel")
        self.privateKeyLabel.setGeometry(QRect(40, 230, 601, 16))
        self.privateKeyBtn = QPushButton(self.centralwidget)
        self.privateKeyBtn.setObjectName(u"privateKeyBtn")
        self.privateKeyBtn.setGeometry(QRect(650, 220, 93, 41))
        self.input = QTextEdit(self.centralwidget)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(40, 320, 621, 161))
        self.output = QTextEdit(self.centralwidget)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(40, 530, 621, 171))
        self.encryptBtn = QPushButton(self.centralwidget)
        self.encryptBtn.setObjectName(u"encryptBtn")
        self.encryptBtn.setGeometry(QRect(680, 440, 93, 71))
        self.decryptBtn = QPushButton(self.centralwidget)
        self.decryptBtn.setObjectName(u"decryptBtn")
        self.decryptBtn.setGeometry(QRect(680, 540, 93, 71))
        self.aboutLabel = QLabel(self.centralwidget)
        self.aboutLabel.setObjectName(u"aboutLabel")
        self.aboutLabel.setGeometry(QRect(370, 720, 431, 20))
        self.msgLabel = QLabel(self.centralwidget)
        self.msgLabel.setObjectName(u"msgLabel")
        self.msgLabel.setGeometry(QRect(50, 290, 111, 16))
        self.outputLabel = QLabel(self.centralwidget)
        self.outputLabel.setObjectName(u"outputLabel")
        self.outputLabel.setGeometry(QRect(50, 500, 111, 16))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 270, 761, 21))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(20, 120, 761, 21))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.genKeyBtn = QPushButton(self.centralwidget)
        self.genKeyBtn.setObjectName(u"genKeyBtn")
        self.genKeyBtn.setGeometry(QRect(62, 50, 681, 51))
        self.genKeyLabel = QLabel(self.centralwidget)
        self.genKeyLabel.setObjectName(u"genKeyLabel")
        self.genKeyLabel.setGeometry(QRect(30, 20, 411, 16))
        self.switchBtn = QPushButton(self.centralwidget)
        self.switchBtn.setObjectName(u"switchBtn")
        self.switchBtn.setGeometry(QRect(330, 490, 41, 28))
        self.copyInputBtn = QPushButton(self.centralwidget)
        self.copyInputBtn.setObjectName(u"copyInputBtn")
        self.copyInputBtn.setGeometry(QRect(660, 320, 61, 28))
        self.copyOutputBtn = QPushButton(self.centralwidget)
        self.copyOutputBtn.setObjectName(u"copyOutputBtn")
        self.copyOutputBtn.setGeometry(QRect(660, 640, 61, 28))
        self.pasteInputBtn = QPushButton(self.centralwidget)
        self.pasteInputBtn.setObjectName(u"pasteInputBtn")
        self.pasteInputBtn.setGeometry(QRect(660, 350, 61, 28))
        self.clearBtn = QPushButton(self.centralwidget)
        self.clearBtn.setObjectName(u"clearBtn")
        self.clearBtn.setGeometry(QRect(660, 380, 61, 28))
        self.clearBtn_2 = QPushButton(self.centralwidget)
        self.clearBtn_2.setObjectName(u"clearBtn_2")
        self.clearBtn_2.setGeometry(QRect(660, 670, 61, 28))
        self.onTopCheckBox = QCheckBox(self.centralwidget)
        self.onTopCheckBox.setObjectName(u"onTopCheckBox")
        self.onTopCheckBox.setGeometry(QRect(20, 710, 211, 19))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SendMessageSafe\uff08\u5b89\u5fc3\u50b3\u8a0a\uff09 - RSA", None))
        self.publicKeyBtn.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.publicKeyLabel.setText(QCoreApplication.translate("MainWindow", u"Select Public Key (.pem)", None))
        self.privateKeyLabel.setText(QCoreApplication.translate("MainWindow", u"Select Private Key (.pem)", None))
        self.privateKeyBtn.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.encryptBtn.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.decryptBtn.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
        self.aboutLabel.setText(QCoreApplication.translate("MainWindow", u"Marco Cheung @ 2022, https://github.com/marc0cheung", None))
        self.msgLabel.setText(QCoreApplication.translate("MainWindow", u"Message:", None))
        self.outputLabel.setText(QCoreApplication.translate("MainWindow", u"Output:", None))
        self.genKeyBtn.setText(QCoreApplication.translate("MainWindow", u"Generate RSA Public and Private Keys", None))
        self.genKeyLabel.setText(QCoreApplication.translate("MainWindow", u"Generate Public and Private Keys:", None))
        self.switchBtn.setText(QCoreApplication.translate("MainWindow", u"\u21f5", None))
        self.copyInputBtn.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.copyOutputBtn.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.pasteInputBtn.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.clearBtn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.clearBtn_2.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.onTopCheckBox.setText(QCoreApplication.translate("MainWindow", u"Always on Top", None))
    # retranslateUi

