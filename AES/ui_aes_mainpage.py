# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aes_mainpage_autoresize.ui'
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
        MainWindow.resize(741, 412)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Key_Widget = QWidget(self.centralwidget)
        self.Key_Widget.setObjectName(u"Key_Widget")
        self.horizontalLayout_2 = QHBoxLayout(self.Key_Widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.key_label = QLabel(self.Key_Widget)
        self.key_label.setObjectName(u"key_label")

        self.horizontalLayout_2.addWidget(self.key_label)

        self.key_input = QLineEdit(self.Key_Widget)
        self.key_input.setObjectName(u"key_input")
        self.key_input.setMinimumSize(QSize(137, 21))
        self.key_input.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.key_input)


        self.horizontalLayout_3.addWidget(self.Key_Widget)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.VI_Widgets = QWidget(self.centralwidget)
        self.VI_Widgets.setObjectName(u"VI_Widgets")
        self.horizontalLayout = QHBoxLayout(self.VI_Widgets)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.vi_label = QLabel(self.VI_Widgets)
        self.vi_label.setObjectName(u"vi_label")

        self.horizontalLayout.addWidget(self.vi_label)

        self.vi_input = QLineEdit(self.VI_Widgets)
        self.vi_input.setObjectName(u"vi_input")
        self.vi_input.setMinimumSize(QSize(148, 21))
        self.vi_input.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout.addWidget(self.vi_input)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.horizontalLayout_3.addWidget(self.VI_Widgets)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Decrypted_Msg = QWidget(self.centralwidget)
        self.Decrypted_Msg.setObjectName(u"Decrypted_Msg")
        self.verticalLayout = QVBoxLayout(self.Decrypted_Msg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.msg_label = QLabel(self.Decrypted_Msg)
        self.msg_label.setObjectName(u"msg_label")

        self.verticalLayout.addWidget(self.msg_label)

        self.msg_input = QTextEdit(self.Decrypted_Msg)
        self.msg_input.setObjectName(u"msg_input")

        self.verticalLayout.addWidget(self.msg_input)

        self.Decrypted_Edit_Widget = QWidget(self.Decrypted_Msg)
        self.Decrypted_Edit_Widget.setObjectName(u"Decrypted_Edit_Widget")
        self.horizontalLayout_5 = QHBoxLayout(self.Decrypted_Edit_Widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Copy_Decrypted = QPushButton(self.Decrypted_Edit_Widget)
        self.Copy_Decrypted.setObjectName(u"Copy_Decrypted")

        self.horizontalLayout_5.addWidget(self.Copy_Decrypted)

        self.Paste_Decrypted = QPushButton(self.Decrypted_Edit_Widget)
        self.Paste_Decrypted.setObjectName(u"Paste_Decrypted")

        self.horizontalLayout_5.addWidget(self.Paste_Decrypted)

        self.Clear_Decrypted = QPushButton(self.Decrypted_Edit_Widget)
        self.Clear_Decrypted.setObjectName(u"Clear_Decrypted")

        self.horizontalLayout_5.addWidget(self.Clear_Decrypted)


        self.verticalLayout.addWidget(self.Decrypted_Edit_Widget)


        self.horizontalLayout_4.addWidget(self.Decrypted_Msg)

        self.de_en_Btn_Widget = QWidget(self.centralwidget)
        self.de_en_Btn_Widget.setObjectName(u"de_en_Btn_Widget")
        self.verticalLayout_3 = QVBoxLayout(self.de_en_Btn_Widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.RandomCheckBox = QCheckBox(self.de_en_Btn_Widget)
        self.RandomCheckBox.setObjectName(u"RandomCheckBox")

        self.verticalLayout_3.addWidget(self.RandomCheckBox)

        self.confirmBtn = QPushButton(self.de_en_Btn_Widget)
        self.confirmBtn.setObjectName(u"confirmBtn")

        self.verticalLayout_3.addWidget(self.confirmBtn)

        self.encryptBtn = QPushButton(self.de_en_Btn_Widget)
        self.encryptBtn.setObjectName(u"encryptBtn")

        self.verticalLayout_3.addWidget(self.encryptBtn)

        self.decryptBtn = QPushButton(self.de_en_Btn_Widget)
        self.decryptBtn.setObjectName(u"decryptBtn")

        self.verticalLayout_3.addWidget(self.decryptBtn)

        self.screenCapBtn = QPushButton(self.de_en_Btn_Widget)
        self.screenCapBtn.setObjectName(u"screenCapBtn")

        self.verticalLayout_3.addWidget(self.screenCapBtn)

        self.exchangeBtn = QPushButton(self.de_en_Btn_Widget)
        self.exchangeBtn.setObjectName(u"exchangeBtn")

        self.verticalLayout_3.addWidget(self.exchangeBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_4.addWidget(self.de_en_Btn_Widget)

        self.Encrypted_Widget = QWidget(self.centralwidget)
        self.Encrypted_Widget.setObjectName(u"Encrypted_Widget")
        self.verticalLayout_2 = QVBoxLayout(self.Encrypted_Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.output_label = QLabel(self.Encrypted_Widget)
        self.output_label.setObjectName(u"output_label")

        self.verticalLayout_2.addWidget(self.output_label)

        self.output = QTextEdit(self.Encrypted_Widget)
        self.output.setObjectName(u"output")

        self.verticalLayout_2.addWidget(self.output)

        self.Encrypted_Edit_Widget = QWidget(self.Encrypted_Widget)
        self.Encrypted_Edit_Widget.setObjectName(u"Encrypted_Edit_Widget")
        self.horizontalLayout_6 = QHBoxLayout(self.Encrypted_Edit_Widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Copy_Encrypted = QPushButton(self.Encrypted_Edit_Widget)
        self.Copy_Encrypted.setObjectName(u"Copy_Encrypted")

        self.horizontalLayout_6.addWidget(self.Copy_Encrypted)

        self.Paste_Encrypted = QPushButton(self.Encrypted_Edit_Widget)
        self.Paste_Encrypted.setObjectName(u"Paste_Encrypted")

        self.horizontalLayout_6.addWidget(self.Paste_Encrypted)

        self.Clear_Encrypted = QPushButton(self.Encrypted_Edit_Widget)
        self.Clear_Encrypted.setObjectName(u"Clear_Encrypted")

        self.horizontalLayout_6.addWidget(self.Clear_Encrypted)


        self.verticalLayout_2.addWidget(self.Encrypted_Edit_Widget)


        self.horizontalLayout_4.addWidget(self.Encrypted_Widget)


        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SendMessageSafe | \u5b89\u5fc3\u50b3\u8a0a | AES Version", None))
        self.key_label.setText(QCoreApplication.translate("MainWindow", u"AES Key:", None))
        self.key_input.setText(QCoreApplication.translate("MainWindow", u"hhhhhhhhhhhhhhhh", None))
        self.vi_label.setText(QCoreApplication.translate("MainWindow", u"AES VI:", None))
        self.vi_input.setText(QCoreApplication.translate("MainWindow", u"01020304050607080", None))
        self.msg_label.setText(QCoreApplication.translate("MainWindow", u"Decrypted:", None))
        self.Copy_Decrypted.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.Paste_Decrypted.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.Clear_Decrypted.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.RandomCheckBox.setText(QCoreApplication.translate("MainWindow", u"Random En/De-Crypt", None))
        self.confirmBtn.setText(QCoreApplication.translate("MainWindow", u"Confirm Pref", None))
        self.encryptBtn.setText(QCoreApplication.translate("MainWindow", u"Encrypted", None))
        self.decryptBtn.setText(QCoreApplication.translate("MainWindow", u"Decrypted", None))
        self.screenCapBtn.setText(QCoreApplication.translate("MainWindow", u"ScreenCap", None))
        self.exchangeBtn.setText(QCoreApplication.translate("MainWindow", u"\u21b9", None))
        self.output_label.setText(QCoreApplication.translate("MainWindow", u"Encrypted:", None))
        self.Copy_Encrypted.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.Paste_Encrypted.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.Clear_Encrypted.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
    # retranslateUi

