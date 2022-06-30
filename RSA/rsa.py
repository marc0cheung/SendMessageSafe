# -*- coding: utf-8 -*-
# @Time    : 30-06-2022, 12:36
# @Author  : marc0cheung
# @Site    : https://marc0cheung.github.io/projects
# @File    : rsa.py
# @Software: SendMessageSafe

import Crypto.PublicKey.RSA
import Crypto.Cipher.PKCS1_v1_5
import Crypto.Random
import Crypto.Signature.PKCS1_v1_5
import Crypto.Hash


def generateKeys():
    x = Crypto.PublicKey.RSA.generate(2048)
    #  Crypto.PublicKey.RSA.generate(2048, Crypto.Random.new().read)
    privateKey = x.exportKey("PEM")  # Generate Private Key
    publicKey = x.publickey().exportKey()  # Generate Public Key

    with open("privateKey.pem", "wb") as x:
        x.write(privateKey)
    with open("publicKey.pem", "wb") as x:
        x.write(publicKey)


if __name__ == "__main__":
    print("Hello")
    generateKeys()
    # app = QtWidgets.QApplication(sys.argv)
    # mainpage = MainWindow()
    # mainpage.show()
    # sys.exit(app.exec_())
