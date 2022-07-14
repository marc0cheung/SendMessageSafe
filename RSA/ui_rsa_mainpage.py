# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rsa_mainpage_autosize.ui'
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
        MainWindow.resize(789, 601)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.genKey_Widget = QWidget(self.centralwidget)
        self.genKey_Widget.setObjectName(u"genKey_Widget")
        self.horizontalLayout_5 = QHBoxLayout(self.genKey_Widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.genKeyLabel = QLabel(self.genKey_Widget)
        self.genKeyLabel.setObjectName(u"genKeyLabel")

        self.horizontalLayout_5.addWidget(self.genKeyLabel)

        self.lineEdit = QLineEdit(self.genKey_Widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaxLength(60)
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lineEdit)

        self.genKeyBtn = QPushButton(self.genKey_Widget)
        self.genKeyBtn.setObjectName(u"genKeyBtn")
        self.genKeyBtn.setMinimumSize(QSize(85, 32))
        self.genKeyBtn.setMaximumSize(QSize(85, 32))

        self.horizontalLayout_5.addWidget(self.genKeyBtn)


        self.verticalLayout_4.addWidget(self.genKey_Widget)

        self.PubKeySelector_Widget = QWidget(self.centralwidget)
        self.PubKeySelector_Widget.setObjectName(u"PubKeySelector_Widget")
        self.horizontalLayout = QHBoxLayout(self.PubKeySelector_Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.publicKeyLabel = QLabel(self.PubKeySelector_Widget)
        self.publicKeyLabel.setObjectName(u"publicKeyLabel")

        self.horizontalLayout.addWidget(self.publicKeyLabel)

        self.publicKeyBtn = QPushButton(self.PubKeySelector_Widget)
        self.publicKeyBtn.setObjectName(u"publicKeyBtn")
        self.publicKeyBtn.setMinimumSize(QSize(85, 32))
        self.publicKeyBtn.setMaximumSize(QSize(85, 32))

        self.horizontalLayout.addWidget(self.publicKeyBtn)


        self.verticalLayout_4.addWidget(self.PubKeySelector_Widget)

        self.PrivKeySelector_Widget = QWidget(self.centralwidget)
        self.PrivKeySelector_Widget.setObjectName(u"PrivKeySelector_Widget")
        self.horizontalLayout_2 = QHBoxLayout(self.PrivKeySelector_Widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.privateKeyLabel = QLabel(self.PrivKeySelector_Widget)
        self.privateKeyLabel.setObjectName(u"privateKeyLabel")

        self.horizontalLayout_2.addWidget(self.privateKeyLabel)

        self.privateKeyBtn = QPushButton(self.PrivKeySelector_Widget)
        self.privateKeyBtn.setObjectName(u"privateKeyBtn")
        self.privateKeyBtn.setMinimumSize(QSize(85, 32))
        self.privateKeyBtn.setMaximumSize(QSize(85, 32))

        self.horizontalLayout_2.addWidget(self.privateKeyBtn)


        self.verticalLayout_4.addWidget(self.PrivKeySelector_Widget)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Msg_Widget = QWidget(self.centralwidget)
        self.Msg_Widget.setObjectName(u"Msg_Widget")
        self.verticalLayout = QVBoxLayout(self.Msg_Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.msgLabel = QLabel(self.Msg_Widget)
        self.msgLabel.setObjectName(u"msgLabel")

        self.verticalLayout.addWidget(self.msgLabel)

        self.input = QTextEdit(self.Msg_Widget)
        self.input.setObjectName(u"input")

        self.verticalLayout.addWidget(self.input)

        self.MsgBtn_Widget = QWidget(self.Msg_Widget)
        self.MsgBtn_Widget.setObjectName(u"MsgBtn_Widget")
        self.horizontalLayout_3 = QHBoxLayout(self.MsgBtn_Widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.copyInputBtn = QPushButton(self.MsgBtn_Widget)
        self.copyInputBtn.setObjectName(u"copyInputBtn")

        self.horizontalLayout_3.addWidget(self.copyInputBtn)

        self.pasteInputBtn = QPushButton(self.MsgBtn_Widget)
        self.pasteInputBtn.setObjectName(u"pasteInputBtn")

        self.horizontalLayout_3.addWidget(self.pasteInputBtn)

        self.clearBtn = QPushButton(self.MsgBtn_Widget)
        self.clearBtn.setObjectName(u"clearBtn")

        self.horizontalLayout_3.addWidget(self.clearBtn)


        self.verticalLayout.addWidget(self.MsgBtn_Widget)


        self.horizontalLayout_6.addWidget(self.Msg_Widget)

        self.ControlBtn_Widget = QWidget(self.centralwidget)
        self.ControlBtn_Widget.setObjectName(u"ControlBtn_Widget")
        self.verticalLayout_3 = QVBoxLayout(self.ControlBtn_Widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.onTopCheckBox = QCheckBox(self.ControlBtn_Widget)
        self.onTopCheckBox.setObjectName(u"onTopCheckBox")

        self.verticalLayout_3.addWidget(self.onTopCheckBox)

        self.encryptBtn = QPushButton(self.ControlBtn_Widget)
        self.encryptBtn.setObjectName(u"encryptBtn")

        self.verticalLayout_3.addWidget(self.encryptBtn)

        self.decryptBtn = QPushButton(self.ControlBtn_Widget)
        self.decryptBtn.setObjectName(u"decryptBtn")

        self.verticalLayout_3.addWidget(self.decryptBtn)

        self.switchBtn = QPushButton(self.ControlBtn_Widget)
        self.switchBtn.setObjectName(u"switchBtn")

        self.verticalLayout_3.addWidget(self.switchBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_6.addWidget(self.ControlBtn_Widget)

        self.Output_Widget = QWidget(self.centralwidget)
        self.Output_Widget.setObjectName(u"Output_Widget")
        self.verticalLayout_2 = QVBoxLayout(self.Output_Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.outputLabel = QLabel(self.Output_Widget)
        self.outputLabel.setObjectName(u"outputLabel")

        self.verticalLayout_2.addWidget(self.outputLabel)

        self.output = QTextEdit(self.Output_Widget)
        self.output.setObjectName(u"output")

        self.verticalLayout_2.addWidget(self.output)

        self.OutputBtn_Widget = QWidget(self.Output_Widget)
        self.OutputBtn_Widget.setObjectName(u"OutputBtn_Widget")
        self.horizontalLayout_4 = QHBoxLayout(self.OutputBtn_Widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.copyInputBtn_2 = QPushButton(self.OutputBtn_Widget)
        self.copyInputBtn_2.setObjectName(u"copyInputBtn_2")

        self.horizontalLayout_4.addWidget(self.copyInputBtn_2)

        self.pasteInputBtn_2 = QPushButton(self.OutputBtn_Widget)
        self.pasteInputBtn_2.setObjectName(u"pasteInputBtn_2")

        self.horizontalLayout_4.addWidget(self.pasteInputBtn_2)

        self.clearBtn_2 = QPushButton(self.OutputBtn_Widget)
        self.clearBtn_2.setObjectName(u"clearBtn_2")

        self.horizontalLayout_4.addWidget(self.clearBtn_2)


        self.verticalLayout_2.addWidget(self.OutputBtn_Widget)


        self.horizontalLayout_6.addWidget(self.Output_Widget)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SendMessageSafe | \u5b89\u5fc3\u50b3\u8a0a | RSA Version", None))
        self.genKeyLabel.setText(QCoreApplication.translate("MainWindow", u"Generate Public and Private Keys:", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"KeyFileName", None))
        self.genKeyBtn.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.publicKeyLabel.setText(QCoreApplication.translate("MainWindow", u"Select Public Key (a .pem file you received)", None))
        self.publicKeyBtn.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.privateKeyLabel.setText(QCoreApplication.translate("MainWindow", u"Select Private Key (your own private .pem file)", None))
        self.privateKeyBtn.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.msgLabel.setText(QCoreApplication.translate("MainWindow", u"Message:", None))
        self.copyInputBtn.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.pasteInputBtn.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.clearBtn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.onTopCheckBox.setText(QCoreApplication.translate("MainWindow", u"Always on Top", None))
        self.encryptBtn.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.decryptBtn.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
        self.switchBtn.setText(QCoreApplication.translate("MainWindow", u"\u21b9", None))
        self.outputLabel.setText(QCoreApplication.translate("MainWindow", u"Output:", None))
        self.copyInputBtn_2.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.pasteInputBtn_2.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.clearBtn_2.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
    # retranslateUi

