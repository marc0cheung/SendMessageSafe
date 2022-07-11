# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aes_mainpage.ui'
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
        MainWindow.resize(837, 589)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.confirmBtn = QPushButton(self.centralwidget)
        self.confirmBtn.setObjectName(u"confirmBtn")
        self.confirmBtn.setGeometry(QRect(632, 70, 121, 111))
        self.vi_label = QLabel(self.centralwidget)
        self.vi_label.setObjectName(u"vi_label")
        self.vi_label.setGeometry(QRect(10, 70, 72, 15))
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
        self.key_label = QLabel(self.centralwidget)
        self.key_label.setObjectName(u"key_label")
        self.key_label.setGeometry(QRect(10, 170, 72, 15))
        self.about_label = QLabel(self.centralwidget)
        self.about_label.setObjectName(u"about_label")
        self.about_label.setGeometry(QRect(460, 560, 361, 20))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 530, 161, 51))
        self.RandomCheckBox = QCheckBox(self.centralwidget)
        self.RandomCheckBox.setObjectName(u"RandomCheckBox")
        self.RandomCheckBox.setGeometry(QRect(610, 200, 211, 20))
        self.key_input = QLineEdit(self.centralwidget)
        self.key_input.setObjectName(u"key_input")
        self.key_input.setGeometry(QRect(90, 160, 331, 31))
        self.key_input.setEchoMode(QLineEdit.Password)
        self.vi_input = QLineEdit(self.centralwidget)
        self.vi_input.setObjectName(u"vi_input")
        self.vi_input.setGeometry(QRect(90, 60, 331, 31))
        self.vi_input.setEchoMode(QLineEdit.Normal)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SendMessageSafe\uff08\u5b89\u5fc3\u50b3\u8a0a\uff09", None))
        self.confirmBtn.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.vi_label.setText(QCoreApplication.translate("MainWindow", u"AES VI:", None))
        self.encryptBtn.setText(QCoreApplication.translate("MainWindow", u"Encrypted", None))
        self.decryptBtn.setText(QCoreApplication.translate("MainWindow", u"Decrypted", None))
        self.msg_label.setText(QCoreApplication.translate("MainWindow", u"Message:", None))
        self.output_label.setText(QCoreApplication.translate("MainWindow", u"Output:", None))
        self.key_label.setText(QCoreApplication.translate("MainWindow", u"AES Key:", None))
        self.about_label.setText(QCoreApplication.translate("MainWindow", u"Marco Cheung @ 2022, https://github.com/marc0cheung/", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Screen Decryption", None))
        self.RandomCheckBox.setText(QCoreApplication.translate("MainWindow", u"Random En/De-Crypt", None))
        self.key_input.setText(QCoreApplication.translate("MainWindow", u"hhhhhhhhhhhhhhhh", None))
        self.vi_input.setText(QCoreApplication.translate("MainWindow", u"01020304050607080", None))
    # retranslateUi

