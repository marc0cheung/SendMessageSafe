# SendMessageSafe（安心傳訊）
**Select Language**: English | [正體中文](https://github.com/marc0cheung/SendMessageSafe/blob/main/README_zhHK.md/)

<br>

_SendMessageSafe_ is a Python-based message encryption and decryption tool for securely transmitting messages on platforms with censorship without having to get caught by "the old big brother". Supports AES symmetric encryption and RSA asymmetric encryption.

<br>

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

Before using _SendMessageSafe_, it is important to have a basic understanding of the encryption and decryption principles of RSA, an asymmetric encryption algorithm. RSA is suitable for use in one-to-one conversations, but is difficult to use in group conversations involving three or more people.

<br>

**Explain the use of RSA encryption with this software in a context**:

- Alice and Bob communicate on a censored, high-risk chat platform and use _SendMessageSafe_ to circumvent censorship.
- Alice uses _SendMessageSafe_ to generate public and private key files called `Alice_publicKey.pem` and `Alice_privateKey.pem`.
  Bob uses the software to generate public and private key files named `Bob_publicKey.pem` and `Bob_privateKey.pem`.
- Through the chat platform, both parties exchange the public key (the public key exchange is secure on the censored platform, only the private key cannot be transferred) and select the `_publicKey.pem` file sent by the other party through the **Select Public Key** section of _SendMessageSafe_
- Alice and Bob select their own private key `_privateKey.pem` file via the **Select Private Key** section of _SendMessageSafe_.
- In this case, Alice's _SendMessageSafe_ key file path should be: `Bob_publicKey.pem` and `Alice_privateKey.pem` 
  At the same time, Bob's _SendMessageSafe_ key file path should be: `Alice_publicKey.pem` and `Bob_privateKey.pem` 
- Alice types in a sensitive message that may be censored in the Message box of _SendMessageSafe_ and presses "Encrypt" to get the encrypted result in the Output on the right.
- After Bob receives the cipher message from Alice, copy the cipher message, select "Paste" at the bottom of the Message box, paste the cipher message into the Message box and select "Decrypt" to get the decrypted plain text message in the Output on the right.

<br>

<div align="center"><img src="https://github.com/marc0cheung/SendMessageSafe/raw/main/README.assets/SMS-RSA-Mainpage-2.png" alt="SMS-RSA-Mainpage-2" width="700px"></div>

<br>

- After entering any key name you wish to set in the input box at the top of the form, press the Generate button and select the save path, the program will automatically generate the public key and private key: `{FileName}_publicKey.pem` and ` {fileName}_privateKey.pem` files. If no file name is entered, the system will prompt to automatically generate the default name: `a_publicKey.pem` and `a_privateKey.pem` files.
- The "Always on Top" feature is not yet developed. In the meantime, I find the "copy-paste" process not very user-friendly and am considering a more efficient way of encrypting plaintext and decrypting ciphertext, similar to "on-screen word detection" or something else.

<br>

### Screenshot of SendMessageSafe RSA Version Mainpage (in use)

<div align="center"><img src="https://github.com/marc0cheung/SendMessageSafe/raw/main/README.assets/SMS-RSA-Mainpage.png" alt="SMS-RSA-Mainpage" width="700px"></div>

<br>

### How to make changes from source code

- (Non-essential step) Use Anaconda to create a new virtual environment.

- Install via pip:

  ```bash
  pip install pycryptodome
  pip install pyperclip
  pip install PySide2
  ```

- Use Qt Designer to modifiy the `.ui` files under `/QtUI` folder, and compile them with `pyside2-uic`

- Use Python IDE (e.g. PyCharm) to create a new project based on the source code and modify the source code.

<br><br>

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

AES, as a symmetric encryption algorithm, does not require the generation of `.pem` files, only the secure exchange of a 16-bit key with a VI value for encryption and decryption. This method is suitable for conversations between more than two or even more people (using the same key for encryption and decryption). **But AES security is very poor if no secure way of passing the key between the conversants is found [1].**

<br>

**Explain the use of AES encryption with this software in a context**:

- Alice and Bob communicate on a censored, high-risk chat platform, using the AES version of _SendMessageSafe_ to circumvent censorship.
- Alice and Bob agree on a key and VI value through an offline meeting (or other secure method) and set these two values in _SendMessageSafe_.
- Alice enters a sensitive message (plaintext) that may be censored in the Decrypted box and selects "Encrypt" to get the encrypted result in the Encrypted box on the right.
- Bob will receive the cipher text from Alice, copy the cipher text, select 'Paste' below the Encrypted box, paste the cipher text into the Encrypted box and select 'Decrypt' to get the decrypted plain text message in the Decrypted box on the left.

<br>

<div align="center"><img src="https://github.com/marc0cheung/SendMessageSafe/raw/main/README.assets/SMS-AES-Mainpage.png" alt="SMS-AES-Mainpage" width="700px"></div>

<br>

[1] One way to securely pass the AES key is to use RSA to pass the AES key and then use AES to encrypt and decrypt the conversation message.

<br>

### How to make changes from source code

- (Non-essential step) Use Anaconda to create a new virtual environment.

- Install via pip:

  ```bash
  pip install pycryptodome
  pip install pyperclip
  pip install PySide2
  ```

- Use Qt Designer to modifiy the `.ui` files under `/QtUI` folder, and compile them with `pyside2-uic`

- Use Python IDE (e.g. PyCharm) to create a new project based on the source code and modify the source code.

<br>
<br>
