# SendMessageSafe（安心傳訊）
SendMessageSafe is a Python-based message encryption and decryption tool for securely transmitting messages on platforms with censorship without having to get caught by "the old big brother". Supports AES symmetric encryption and RSA asymmetric encryption.

<br>

## [AES Version](https://github.com/marc0cheung/SendMessageSafe/tree/main/AES)

### Package Requirement
```python
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
```

<br>

### How to use

<div align="center"><img src="https://github.com/marc0cheung/SendMessageSafe/raw/main/README.assets/SMS-AES-Mainpage-2.png" alt="SMS-AES-Mainpage-2" width="700px"></div>

### Screenshot of SendMessageSafe AES Version Mainpage (in use)

<div align="center"><img src="https://github.com/marc0cheung/SendMessageSafe/raw/main/README.assets/SMS-AES-Mainpage.png" alt="SMS-AES-Mainpage" width="700px"></div>

<br>

### How to make changes from source code

<br><br>

## [RSA Version](https://github.com/marc0cheung/SendMessageSafe/tree/main/RSA)

### Package Requirement
```python
import binascii
import os
import sys
import base64
import pyperclip

# pip install pycryptodome
import Crypto.PublicKey.RSA
import Crypto.Cipher.PKCS1_v1_5
import Crypto.Random
import Crypto.Signature.PKCS1_v1_5
import Crypto.Hash

from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QDialog
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt
```

<br>

### How to use



<br>

### How to make changes from source code

<br>
<br>
