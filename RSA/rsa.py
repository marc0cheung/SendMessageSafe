# -*- coding: utf-8 -*-
# @Time    : 02-07-2022, 9:55 HKT
# @Author  : marc0cheung
# @Site    : https://marc0cheung.github.io/projects
# @File    : rsa.py
# @Software: SendMessageSafe

import os
import sys
import base64
import pyperclip

import Crypto.PublicKey.RSA
import Crypto.Cipher.PKCS1_v1_5
import Crypto.Random
import Crypto.Signature.PKCS1_v1_5
import Crypto.Hash

from PySide2 import QtCore, QtGui, QtWidgets
# import qimage2ndarray
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QDialog
from PySide2.QtGui import QImage, QPixmap, QIcon
from PySide2.QtCore import QRect, Qt

from ui_rsa_mainpage import Ui_MainWindow

# IF RUNNING ON macOS
import platform
os.environ['QT_MAC_WANTS_LAYER'] = '1'


# Use Crypto to Generate Public and Private Keys (.pem files)
def generateKeys():
    savePath = QFileDialog.getExistingDirectory(QDialog(), "Choose Save Directory")
    x = Crypto.PublicKey.RSA.generate(2048)
    #  Crypto.PublicKey.RSA.generate(2048, Crypto.Random.new().read)
    privateKey = x.exportKey("PEM")  # Generate Private Key
    publicKey = x.publickey().exportKey()  # Generate Public Key

    with open(savePath + "privateKey.pem", "wb") as x:
        x.write(privateKey)
    with open(savePath + "publicKey.pem", "wb") as x:
        x.write(publicKey)


# Use public key to encrypt
def encrypt_PublicKey():
    with open("publicKey.pem", "rb") as pemFile:
        msg = "一台獨立服務器"
        publicKey = pemFile.read()
        cipher_public = Crypto.Cipher.PKCS1_v1_5.new(Crypto.PublicKey.RSA.importKey(publicKey))
        cipher_text = cipher_public.encrypt(msg.encode('utf-8'))
        print(cipher_text)
        return cipher_text


# Use Private Key to decrypt
def decrypt_PrivateKey(cipher_text):
    with open("privateKey.pem", "rb") as pemFile:
        privateKey = pemFile.read()
        # If there's a password for Private Key, Use: Crypto.PublicKey.RSA.importKey(a, password)
        cipher_private = Crypto.Cipher.PKCS1_v1_5.new(Crypto.PublicKey.RSA.importKey(privateKey))
        text = cipher_private.decrypt(cipher_text, Crypto.Random.new().read)  # 使用私钥进行解密
        return text


# Use Private Key to Sign a SHA256 Signature
def sign_PrivateKey():
    with open("privateKey.pem", "rb") as pemFile:
        msg = "一台獨立服務器"
        c = pemFile.read()
        c_rsa = Crypto.PublicKey.RSA.importKey(c)
        signer = Crypto.Signature.PKCS1_v1_5.new(c_rsa)
        msg_hash = Crypto.Hash.SHA256.new()
        msg_hash.update(msg)
        sign = signer.sign(msg_hash)
        return sign


# Verify Sign Using Public Key
def verifySign_PublicKey(sign):
    with open("publicKey.pem", "rb") as pemFile:
        msg = "一台獨立服務器"
        d = pemFile.read()
        d_rsa = Crypto.PublicKey.RSA.importKey(d)
        verifer = Crypto.Signature.PKCS1_v1_5.new(d_rsa)
        msg_hash = Crypto.Hash.SHA256.new()
        msg_hash.update(msg)
        verify = verifer.verify(msg_hash, sign)
        print(verify)


class MainWindow(QMainWindow):
    publicKeySource = ""
    privateKeySource = ""
    text_encrypted_base64 = None

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('icon.png'))
        self.ui.statusbar.showMessage("Marco Cheung @ 2022,  https://github.com/marc0cheung/SendMessageSafe/")

        # Button Signals and Slots
        self.ui.genKeyBtn.clicked.connect(self.genKeysWithNames)

        self.ui.publicKeyBtn.clicked.connect(self.onPublicKeyBtn_Clicked)
        self.ui.privateKeyBtn.clicked.connect(self.onPrivateKeyBtn_Clicked)

        self.ui.encryptBtn.clicked.connect(self.onEncryptBtn_Clicked)
        self.ui.decryptBtn.clicked.connect(self.onDecryptBtn_Clicked)

        self.ui.switchBtn.clicked.connect(self.onSwitchBtn_Clicked)

        # Copy, Paste and Clear Function for Message and Output Textbox
        self.ui.copyInputBtn.clicked.connect(self.onCopyInputBtn_Clicked)
        self.ui.pasteInputBtn.clicked.connect(self.onPasteInputBtn_Clicked)
        self.ui.clearInputBtn.clicked.connect(self.clearInput)
        self.ui.copyOutputBtn.clicked.connect(self.onCopyOutputBtn_Clicked)
        self.ui.pasteOutputBtn.clicked.connect(self.onPasteOutputBtn_Clicked)
        self.ui.clearOutputBtn.clicked.connect(self.clearOutput)

        # CheckBox Signals and Slots
        self.ui.onTopCheckBox.stateChanged.connect(self.setAlwaysOnTop)

    # Use Crypto to Generate Public and Private Keys (.pem files)
    def genKeysWithNames(self):
        filename = self.ui.KeyFilenameInput.text()
        savePath = QFileDialog.getExistingDirectory(QDialog(), "Choose Save Directory")
        x = Crypto.PublicKey.RSA.generate(2048)
        #  Crypto.PublicKey.RSA.generate(2048, Crypto.Random.new().read)
        privateKey = x.exportKey("PEM")  # Generate Private Key
        publicKey = x.publickey().exportKey()  # Generate Public Key

        with open(savePath + "/" + filename + "_privateKey.pem", "wb") as x:
            x.write(privateKey)
        with open(savePath + "/" + filename + "_publicKey.pem", "wb") as x:
            x.write(publicKey)

    def onPublicKeyBtn_Clicked(self):
        source = QFileDialog.getOpenFileName(QDialog(), "Select Public Key")
        if source[0] != "":
            self.publicKeySource = source[0]
            self.ui.publicKeyLabel.setText(str(self.publicKeySource))

    def onPrivateKeyBtn_Clicked(self):
        source = QFileDialog.getOpenFileName(QDialog(), "Select Private Key")
        if source[0] != "":
            self.privateKeySource = source[0]
            self.ui.privateKeyLabel.setText(str(self.privateKeySource))

    def onSwitchBtn_Clicked(self):
        temp = self.ui.input.toPlainText()
        self.ui.input.setText(self.ui.output.toPlainText())  # Output msg to Input msg
        self.ui.output.setText(temp)

    def onCopyInputBtn_Clicked(self):
        pyperclip.copy(self.ui.input.toPlainText())

    def onPasteInputBtn_Clicked(self):
        cipher_text = pyperclip.paste()
        self.ui.input.setText(cipher_text)

    def clearInput(self):
        self.ui.input.clear()

    def onCopyOutputBtn_Clicked(self):
        pyperclip.copy(self.ui.output.toPlainText())

    def onPasteOutputBtn_Clicked(self):
        text = pyperclip.paste()
        self.ui.output.setText(text)

    def clearOutput(self):
        self.ui.output.clear()

    # Bug Here
    def setAlwaysOnTop(self):
        if self.ui.onTopCheckBox.checkState() == Qt.Checked:
            self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        elif self.ui.onTopCheckBox.checkState() == Qt.Unchecked:
            self.setWindowFlags(QtCore.Qt.Widget)

    def onEncryptBtn_Clicked(self):
        msg = self.ui.input.toPlainText()

        if self.publicKeySource != "":
            # Use Public Key to Encrypt Message
            with open(self.publicKeySource, "rb") as pemFile:
                publicKey = pemFile.read()
                cipher_public = Crypto.Cipher.PKCS1_v1_5.new(Crypto.PublicKey.RSA.importKey(publicKey))
                cipher_text = cipher_public.encrypt(msg.encode('utf-8'))
                cipher_text_base64 = base64.b64encode(cipher_text).decode()

                self.text_encrypted_base64 = cipher_text_base64
                self.ui.output.setText(cipher_text_base64)

        else:
            QMessageBox.critical(self, "No Public Key Found", "Select the public key you received")

    def onDecryptBtn_Clicked(self):
        # Use Private Key to Decrypt Message
        if self.text_encrypted_base64 is not None:
            cipher_text_base64 = self.ui.input.toPlainText().encode('utf-8')
        else:
            cipher_text_base64 = self.text_encrypted_base64

        cipher_text = base64.b64decode(cipher_text_base64)

        if self.privateKeySource != "":
            # Use Private Key to Decrypt Cipher Message
            with open(self.privateKeySource, "rb") as pemFile:
                privateKey = pemFile.read()
                # If there's a password for Private Key, Use: Crypto.PublicKey.RSA.importKey(a, password)
                cipher_private = Crypto.Cipher.PKCS1_v1_5.new(Crypto.PublicKey.RSA.importKey(privateKey))
                text_decrypted = cipher_private.decrypt(cipher_text, Crypto.Random.new().read)  # 使用私钥进行解密
                text_decrypted = text_decrypted.decode()
                self.ui.output.setText(text_decrypted)
        else:
            QMessageBox.critical(self, "Private Key Not Found", "Select your private key")


if __name__ == "__main__":
    print("Hello RSA")
    # generateKeys()
    # Verify Sign
    # decrypt_PrivateKey(encrypt_PublicKey())
    # verifySign_PublicKey(sign_PrivateKey())

    app = QtWidgets.QApplication(sys.argv)
    mainpage = MainWindow()
    mainpage.show()
    sys.exit(app.exec_())
