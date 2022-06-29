# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aes_mainpageFbwDaD.ui'
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
        MainWindow.resize(832, 588)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.confirmBtn = QPushButton(self.centralwidget)
        self.confirmBtn.setObjectName(u"confirmBtn")
        self.confirmBtn.setGeometry(QRect(632, 70, 121, 111))
        self.vi_label = QLabel(self.centralwidget)
        self.vi_label.setObjectName(u"vi_label")
        self.vi_label.setGeometry(QRect(10, 70, 72, 15))
        self.vi_input = QTextEdit(self.centralwidget)
        self.vi_input.setObjectName(u"vi_input")
        self.vi_input.setGeometry(QRect(90, 40, 461, 71))
        self.encryptBtn = QPushButton(self.centralwidget)
        self.encryptBtn.setObjectName(u"encryptBtn")
        self.encryptBtn.setGeometry(QRect(590, 240, 93, 71))
        self.msg_input = QTextEdit(self.centralwidget)
        self.msg_input.setObjectName(u"msg_input")
        self.msg_input.setGeometry(QRect(90, 243, 461, 71))
        self.decryptBtn = QPushButton(self.centralwidget)
        self.decryptBtn.setObjectName(u"decryptBtn")
        self.decryptBtn.setGeometry(QRect(700, 240, 93, 71))
        self.output = QTextEdit(self.centralwidget)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(90, 333, 711, 181))
        self.msg_label = QLabel(self.centralwidget)
        self.msg_label.setObjectName(u"msg_label")
        self.msg_label.setGeometry(QRect(10, 270, 72, 15))
        self.output_label = QLabel(self.centralwidget)
        self.output_label.setObjectName(u"output_label")
        self.output_label.setGeometry(QRect(10, 370, 72, 15))
        self.key_input = QTextEdit(self.centralwidget)
        self.key_input.setObjectName(u"key_input")
        self.key_input.setGeometry(QRect(90, 140, 461, 71))
        self.key_label = QLabel(self.centralwidget)
        self.key_label.setObjectName(u"key_label")
        self.key_label.setGeometry(QRect(10, 170, 72, 15))
        self.about_label = QLabel(self.centralwidget)
        self.about_label.setObjectName(u"about_label")
        self.about_label.setGeometry(QRect(390, 560, 431, 20))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 530, 161, 51))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SendMessageSafe\uff08\u5b89\u5fc3\u50b3\u8a0a\uff09", None))
        self.confirmBtn.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.vi_label.setText(QCoreApplication.translate("MainWindow", u"AES VI:", None))
        self.vi_input.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">01020304050607080</p></body></html>", None))
        self.encryptBtn.setText(QCoreApplication.translate("MainWindow", u"Encrypted", None))
        self.decryptBtn.setText(QCoreApplication.translate("MainWindow", u"Decrypted", None))
        self.msg_label.setText(QCoreApplication.translate("MainWindow", u"Message:", None))
        self.output_label.setText(QCoreApplication.translate("MainWindow", u"Output:", None))
        self.key_input.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">hhhhhhhhhhhhhhhh</p></body></html>", None))
        self.key_label.setText(QCoreApplication.translate("MainWindow", u"AES Key:", None))
        self.about_label.setText(QCoreApplication.translate("MainWindow", u"Marco Cheung @ 2022, https://github.com/marc0cheung/", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Screen Decryption", None))
    # retranslateUi

