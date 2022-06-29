# -*- coding: utf-8 -*-
# @Time    : 29-06-2022, 14:09
# @Author  : marc0cheung
# @Site    : https://marc0cheung.github.io/projects
# @File    : aes.py
# @Software: SendMessageSafe


import sys
import base64
# pip install pycryptodome
from Crypto.Cipher import AES

from PySide2 import QtCore, QtGui, QtWidgets
import qimage2ndarray
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QDialog
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtCore import QRect, Qt

from ui_aes_mainpage import Ui_MainWindow


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

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Push Buttons Signals and Slots
        self.ui.confirmBtn.clicked.connect(self.onConfirmBtnClicked)
        self.ui.encryptBtn.clicked.connect(self.encrypt)
        self.ui.decryptBtn.clicked.connect(self.decrypt)

    def encrypt(self):
        # Base64 Everything
        # Base64 Encode
        # input_msg = '测试加密是否成功'  # にほんご한국어
        input_msg = str(self.ui.msg_input.toPlainText())
        original_msg = base64.b64encode(input_msg.encode('utf-8'))
        # print("Original Message(Based64): " + str(original_msg, 'utf-8'))

        # AES Encrypt
        key = str(self.ui.key_input.toPlainText())
        data = str(original_msg)
        aes_encrypt(key, data)
        enctext = aes_encrypt(key, data)
        # print("\nEncrypted Result: ")
        # print(enctext)
        self.ui.output.setText(enctext)

    def decrypt(self):
        self.encrypted_data = str(self.ui.msg_input.toPlainText())

        # AES Decrypt
        self.encrypt_key = str(self.ui.key_input.toPlainText())
        msg_decrypted = aes_decrypt(self.encrypt_key, self.encrypted_data)
        msg_decrypted_processed = msg_decrypted[2:len(msg_decrypted) - 1]

        # Base64 Decode
        self.ui.output.setText(str(base64.b64decode(msg_decrypted_processed), 'utf-8'))

    def onConfirmBtnClicked(self):
        self.vi = str(self.ui.vi_input.toPlainText())
        self.encrypt_key = str(self.ui.key_input.toPlainText())
        popup_msg = "Vi: " + self.vi + "\nKey: " + self.encrypt_key
        QMessageBox.information(self, "Vi and Key Set", popup_msg)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    mainpage = MainWindow()
    mainpage.show()
    sys.exit(app.exec_())
