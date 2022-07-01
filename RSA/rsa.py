# -*- coding: utf-8 -*-
# @Time    : 30-06-2022, 16:30 HKT
# @Author  : marc0cheung
# @Site    : https://marc0cheung.github.io/projects
# @File    : rsa.py
# @Software: SendMessageSafe

import sys

import Crypto.PublicKey.RSA
import Crypto.Cipher.PKCS1_v1_5
import Crypto.Random
import Crypto.Signature.PKCS1_v1_5
import Crypto.Hash

from PySide2 import QtCore, QtGui, QtWidgets
import qimage2ndarray
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QDialog
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtCore import QRect, Qt

from ui_rsa_mainpage import Ui_MainWindow

msg = b'helloworld!!!'


# Use Crypto to Generate Public and Private Keys (.pem files)
def generateKeys():
    x = Crypto.PublicKey.RSA.generate(2048)
    #  Crypto.PublicKey.RSA.generate(2048, Crypto.Random.new().read)
    privateKey = x.exportKey("PEM")  # Generate Private Key
    publicKey = x.publickey().exportKey()  # Generate Public Key

    with open("privateKey.pem", "wb") as x:
        x.write(privateKey)
    with open("publicKey.pem", "wb") as x:
        x.write(publicKey)


# Use public key to encrypt
def encrypt_PublicKey():
    with open("publicKey.pem", "rb") as pemFile:
        publicKey = pemFile.read()
        cipher_public = Crypto.Cipher.PKCS1_v1_5.new(Crypto.PublicKey.RSA.importKey(publicKey))
        cipher_text = cipher_public.encrypt(msg)
        print(cipher_text)
        return cipher_text


# Use Private Key to decrypt
def decrypt_PrivateKey(cipher_text):
    with open("privateKey.pem", "rb") as pemFile:
        privateKey = pemFile.read()
        # If there's a password for Private Key, Use: Crypto.PublicKey.RSA.importKey(a, password)
        cipher_private = Crypto.Cipher.PKCS1_v1_5.new(Crypto.PublicKey.RSA.importKey(privateKey))
        text = cipher_private.decrypt(cipher_text, Crypto.Random.new().read)  # 使用私钥进行解密
        return(text)


# Use Private Key to Sign a SHA256 Signature
def sign_PrivateKey():
    with open("privateKey.pem", "rb") as pemFile:
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
        d = pemFile.read()
        d_rsa = Crypto.PublicKey.RSA.importKey(d)
        verifer = Crypto.Signature.PKCS1_v1_5.new(d_rsa)
        msg_hash = Crypto.Hash.SHA256.new()
        msg_hash.update(msg)
        verify = verifer.verify(msg_hash, sign)
        print(verify)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Button Signals and Slots
        # CheckBox Signals and Slots


if __name__ == "__main__":
    print("Hello RSA")
    # generateKeys()

    print(str(decrypt_PrivateKey(encrypt_PublicKey()), 'utf-8'))

    # Verify Sign
    # decrypt_PrivateKey(encrypt_PublicKey())
    # verifySign_PublicKey(sign_PrivateKey())

    app = QtWidgets.QApplication(sys.argv)
    mainpage = MainWindow()
    mainpage.show()
    sys.exit(app.exec_())
