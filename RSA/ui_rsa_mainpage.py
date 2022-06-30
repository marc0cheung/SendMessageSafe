# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rsa_mainpagegJITIa.ui'
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
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.publicKeyBtn = QPushButton(self.centralwidget)
        self.publicKeyBtn.setObjectName(u"publicKeyBtn")
        self.publicKeyBtn.setGeometry(QRect(650, 20, 93, 41))
        self.publicKeyLabel = QLabel(self.centralwidget)
        self.publicKeyLabel.setObjectName(u"publicKeyLabel")
        self.publicKeyLabel.setGeometry(QRect(40, 20, 251, 16))
        self.privateKeyLabel = QLabel(self.centralwidget)
        self.privateKeyLabel.setObjectName(u"privateKeyLabel")
        self.privateKeyLabel.setGeometry(QRect(40, 90, 251, 16))
        self.privateKeyBtn = QPushButton(self.centralwidget)
        self.privateKeyBtn.setObjectName(u"privateKeyBtn")
        self.privateKeyBtn.setGeometry(QRect(650, 80, 93, 41))
        self.input = QTextEdit(self.centralwidget)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(40, 180, 621, 161))
        self.output = QTextEdit(self.centralwidget)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(40, 390, 621, 171))
        self.encryptBtn = QPushButton(self.centralwidget)
        self.encryptBtn.setObjectName(u"encryptBtn")
        self.encryptBtn.setGeometry(QRect(680, 300, 93, 71))
        self.decryptBtn = QPushButton(self.centralwidget)
        self.decryptBtn.setObjectName(u"decryptBtn")
        self.decryptBtn.setGeometry(QRect(680, 400, 93, 71))
        self.aboutLabel = QLabel(self.centralwidget)
        self.aboutLabel.setObjectName(u"aboutLabel")
        self.aboutLabel.setGeometry(QRect(360, 570, 431, 20))
        self.msgLabel = QLabel(self.centralwidget)
        self.msgLabel.setObjectName(u"msgLabel")
        self.msgLabel.setGeometry(QRect(50, 150, 111, 16))
        self.outputLabel = QLabel(self.centralwidget)
        self.outputLabel.setObjectName(u"outputLabel")
        self.outputLabel.setGeometry(QRect(50, 360, 111, 16))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 130, 761, 21))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.publicKeyBtn.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.publicKeyLabel.setText(QCoreApplication.translate("MainWindow", u"Select Public Key (.pem)", None))
        self.privateKeyLabel.setText(QCoreApplication.translate("MainWindow", u"Select Private Key (.pem)", None))
        self.privateKeyBtn.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.encryptBtn.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.decryptBtn.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
        self.aboutLabel.setText(QCoreApplication.translate("MainWindow", u"Marco Cheung @ 2022, https://github.com/marc0cheung", None))
        self.msgLabel.setText(QCoreApplication.translate("MainWindow", u"Message:", None))
        self.outputLabel.setText(QCoreApplication.translate("MainWindow", u"Output:", None))
    # retranslateUi

