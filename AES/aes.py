# -*- coding: utf-8 -*-
# @Time    : 14-07-2022, 18:06 HKT
# @Author  : marc0cheung
# @Site    : https://marc0cheung.github.io/projects
# @File    : aes.py
# @Software: SendMessageSafe
import os
import sys
import base64
import secrets
# pip install pycryptodome
import pyperclip
from Crypto.Cipher import AES

from PySide2 import QtWidgets
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QDialog
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt

from ui_aes_mainpage import Ui_MainWindow

# IF RUNNING ON macOS, Uncomment Line 24 (Below)
os.environ['QT_MAC_WANTS_LAYER'] = '1'


def aes_encrypt(encrypt_key, source_data):
    vi = '0102030405060708'
    pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
    source_data = pad(source_data)
    # String Pad left
    cipher = AES.new(encrypt_key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
    encryptedbytes = cipher.encrypt(source_data.encode('utf8'))
    # encrypted data types in bytes
    encodestrs = base64.b64encode(encryptedbytes)
    # Encoding with base64, returning byte strings
    enctext = encodestrs.decode('utf8')
    # Decoding of byte strings in utf-8
    return enctext


def aes_decrypt(encrypt_key, encrypted_data):
    vi = '0102030405060708'
    encrypted_data = encrypted_data.encode('utf8')
    encodebytes = base64.decodebytes(encrypted_data)
    # Convert encrypted data to bit bytes type data
    cipher = AES.new(encrypt_key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
    text_decrypted = cipher.decrypt(encodebytes)
    unpad = lambda s: s[0:-s[-1]]
    text_decrypted = unpad(text_decrypted)
    text_decrypted = text_decrypted.decode('utf8')
    return text_decrypted


class MainWindow(QMainWindow):
    vi = "01020304050607080"
    encrypt_key = "hhhhhhhhhhhhhhhh"
    source_data = None
    encrypted_data = None
    randomEncrypt = False

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('icon.png'))
        self.ui.statusbar.showMessage("Marco Cheung @ 2022,  https://github.com/marc0cheung/SendMessageSafe/")

        # Push Buttons Signals and Slots
        self.ui.confirmBtn.clicked.connect(self.onConfirmBtnClicked)
        self.ui.exchangeBtn.clicked.connect(self.onExchangeBtn_Clicked)
        self.ui.encryptBtn.clicked.connect(self.encrypt)
        self.ui.decryptBtn.clicked.connect(self.decrypt)

        self.ui.Copy_Decrypted.clicked.connect(self.onDecryptedCopyBtn_Clicked)
        self.ui.Paste_Decrypted.clicked.connect(self.onDecryptedPasteBtn_Clicked)
        self.ui.Clear_Decrypted.clicked.connect(self.onDecryptedClearBtn_Clicked)

        self.ui.Copy_Encrypted.clicked.connect(self.onEncryptedCopyBtn_Clicked)
        self.ui.Paste_Encrypted.clicked.connect(self.onEncryptedPasteBtn_Clicked)
        self.ui.Clear_Encrypted.clicked.connect(self.onEncryptedClearBtn_Clicked)

        # CheckBox Signals and Slots
        self.ui.RandomCheckBox.stateChanged.connect(self.onRandomCheckBox_Changed)

    def encrypt(self):
        if not self.randomEncrypt:
            # Base64 Everything - Base64 Encode
            # input_msg = '测试加密是否成功'  # にほんご한국어
            input_msg = str(self.ui.msg_input.toPlainText())
            original_msg = base64.b64encode(input_msg.encode('utf-8'))
            # print("Original Message(Based64): " + str(original_msg, 'utf-8'))  # Debugging

            # AES Encrypt
            key = str(self.ui.key_input.text())
            # Must Use 5L2g5aW9 instead of b'5L2g5aW9' to encrypt!
            data = str(original_msg, 'utf-8')
            enctext = aes_encrypt(key, data)
            self.ui.output.setText(enctext)

        elif self.randomEncrypt:
            # Use "secrets" to generate a safe random int value
            encrypt_times = secrets.randbelow(5)
            print(encrypt_times)

            # Get Original Message
            data = str(self.ui.msg_input.toPlainText())
            key = str(self.ui.key_input.text())

            # AES Encrypt Random Times
            for i in range(0, encrypt_times):
                data = str(base64.b64encode(data.encode('utf-8')), 'utf-8')
                data = aes_encrypt(key, data)

            self.ui.output.setText(str(data) + str(encrypt_times))

    def decrypt(self):
        if not self.randomEncrypt:
            self.encrypted_data = str(self.ui.output.toPlainText())

            # AES Decrypt
            self.encrypt_key = str(self.ui.key_input.text())
            msg_decrypted = aes_decrypt(self.encrypt_key, self.encrypted_data)

            # Base64 Decode
            self.ui.msg_input.setText(str(base64.b64decode(msg_decrypted), 'utf-8'))

        elif self.randomEncrypt:
            self.encrypt_key = str(self.ui.key_input.text())
            # Remove the last number of the encrypted message
            encrypted_msg = str(self.ui.output.toPlainText())[:-1]
            # Pending: If the last one is not number then throw Error
            encrypted_times = int(str(self.ui.output.toPlainText())[-1:])

            # AES Decrypt Random Times
            for i in range(0, encrypted_times):
                encrypted_msg = aes_decrypt(self.encrypt_key, encrypted_msg)
                encrypted_msg = str(base64.b64decode(encrypted_msg), 'utf-8')

            self.ui.msg_input.setText(encrypted_msg)

    def onConfirmBtnClicked(self):
        self.vi = str(self.ui.vi_input.text())
        self.encrypt_key = str(self.ui.key_input.text())
        popup_msg = "Vi: " + self.vi + "\nKey: " + self.encrypt_key
        QMessageBox.information(self, "Vi and Key Set", popup_msg)

    def onRandomCheckBox_Changed(self):
        if self.ui.RandomCheckBox.checkState() == Qt.Checked:
            self.randomEncrypt = True
        elif self.ui.RandomCheckBox.checkState() == Qt.Unchecked:
            self.randomEncrypt = False

    def onExchangeBtn_Clicked(self):
        temp = self.ui.output.toPlainText()
        self.ui.output.setText(self.ui.msg_input.toPlainText())
        self.ui.msg_input.setText(temp)

    def onDecryptedCopyBtn_Clicked(self):
        pyperclip.copy(self.ui.msg_input.toPlainText())

    def onDecryptedPasteBtn_Clicked(self):
        text = pyperclip.paste()
        self.ui.msg_input.setText(text)

    def onDecryptedClearBtn_Clicked(self):
        self.ui.msg_input.clear()

    def onEncryptedCopyBtn_Clicked(self):
        pyperclip.copy(self.ui.output.toPlainText())

    def onEncryptedPasteBtn_Clicked(self):
        text = pyperclip.paste()
        self.ui.output.setText(text)

    def onEncryptedClearBtn_Clicked(self):
        self.ui.output.clear()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    mainpage = MainWindow()
    mainpage.show()
    sys.exit(app.exec_())
