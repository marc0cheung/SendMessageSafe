# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rsa_mainpageBbPqqo.ui'
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
        self.publicKeyLabel.setGeometry(QRect(40, 160, 251, 16))
        self.privateKeyLabel = QLabel(self.centralwidget)
        self.privateKeyLabel.setObjectName(u"privateKeyLabel")
        self.privateKeyLabel.setGeometry(QRect(40, 230, 251, 16))
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
        self.aboutLabel.setGeometry(QRect(360, 710, 431, 20))
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
        self.genKeyBtn.setGeometry(QRect(650, 50, 93, 51))
        self.genKeyLabel = QLabel(self.centralwidget)
        self.genKeyLabel.setObjectName(u"genKeyLabel")
        self.genKeyLabel.setGeometry(QRect(30, 20, 411, 16))
        self.fileNameInput = QTextEdit(self.centralwidget)
        self.fileNameInput.setObjectName(u"fileNameInput")
        self.fileNameInput.setGeometry(QRect(130, 60, 201, 41))
        self.fileNameLabel = QLabel(self.centralwidget)
        self.fileNameLabel.setObjectName(u"fileNameLabel")
        self.fileNameLabel.setGeometry(QRect(40, 70, 91, 16))
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
        self.genKeyBtn.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.genKeyLabel.setText(QCoreApplication.translate("MainWindow", u"1. Generate Public and Private Keys:", None))
        self.fileNameLabel.setText(QCoreApplication.translate("MainWindow", u"FileName:", None))
    # retranslateUi

