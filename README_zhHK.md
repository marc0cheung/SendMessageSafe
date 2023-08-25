# SendMessageSafe（安心傳訊）

**選擇語言**: [English](https://github.com/marc0cheung/SendMessageSafe/blob/main/README.md/) | 正體中文

<br>

安心傳訊（SendMessageSafe）是一款基於 Python 語言開發的即時通訊信息加密解密軟體。該軟體致力於透過加密來規避審查，以便在任何帶有審查之平台提供令人安心的傳訊體驗，避免由於「口出狂言」而遭到「______」的關注。本軟體支持基於 AES 與 RSA 的兩種加密方式。

<br>

## [RSA 版本](https://github.com/marc0cheung/SendMessageSafe/tree/main/RSA)

### Python 依賴包

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

### 如何使用本軟體

使用本軟體前，需粗淺了解 RSA 這一非對稱加密算法的加密解密原理。簡單概括：「公鑰加密，私鑰解密」。RSA 適用於在一對一對話中使用，但如涉及三人或以上的群組對話，則難以使用。

<br>

**以一個情境來解釋 RSA 加密與本軟體之用法：**

- Alice 與 Bob 在一個帶有審查的高風險聊天平台上進行交流，他們使用本軟體來規避審查。
- Alice 使用本軟體生成名為` Alice_publicKey.pem` 與 `Alice_privateKey.pem` 的公鑰和密鑰檔案。
  Bob 使用本軟體生成名為 `Bob_publicKey.pem` 與 `Bob_privateKey.pem` 的公鑰和密鑰檔案。
- 通過聊天平台，雙方將公鑰進行交換（公鑰在審查平台上交換是安全的，僅私鑰不可外傳），並通過本軟體的 **Select Public Key** 部分選擇對方發來的 `_publicKey.pem` 檔案
- Alice 和 Bob 通過本軟體的 **Select Private Key** 部分，選擇自己保留的私鑰 `_privateKey.pem` 檔案。
- 此時，Alice 的軟體密鑰檔案路徑中，應當為： `Bob_publicKey.pem` 與 `Alice_privateKey.pem` 檔案
  同時，Bob 的軟體密鑰檔案路徑中，應當為： `Alice_publicKey.pem` 與 `Bob_privateKey.pem` 檔案
- Alice 在 Message 框中鍵入可能會被審查的敏感訊息，選中「Encrypt」，即可在右側 Output 中得到加密結果，使用下方 「Copy」將密文拷貝後，轉入聊天平台中複製。
- Bob 收到 Alice 發來的密文後，複製密文，在 Message 框下方選擇「Paste」，將密文貼上 Message 框，選擇「Decrypt」，即可在右側 Output 中得到解密後的明文訊息。

<br>

<div align="center"><img src="https://github.com/marc0cheung/SendMessageSafe/raw/main/README.assets/SMS-RSA-Mainpage-2.png" alt="SMS-RSA-Mainpage-2" width="700px"></div>

<br>

- 在窗體上方輸入框輸入你想設置的任意密鑰名後，按下 Generate 按鈕，選擇保存路徑，程序會自動生成公鑰與私鑰：`{FileName}_publicKey.pem`  與 ` {fileName}_privateKey.pem` 文件。如果不輸入文件名，則系統會提示自動使用默認名稱生成：`a_publicKey.pem` 與 `a_privateKey.pem` 文件。
- 「Always on Top」功能暫未開發完畢。同時，個人認為「拷貝 - 貼上」之流程並不十分友好，正在考慮使用類似與「螢幕取詞」或者別的什麼方式進行更加高效的明文加密與密文解密。

<br>

### 軟體使用示意圖

<div align="center"><img src="https://github.com/marc0cheung/SendMessageSafe/raw/main/README.assets/SMS-RSA-Mainpage.png" alt="SMS-RSA-Mainpage" width="700px"></div>

<br>

### 如何基於源代碼進行修改

- （不必要）通過 anaconda 創建新環境，方便管理
- 通過 pip 安裝：

```bash
pip install pycryptodome
pip install pyperclip
pip install PySide2
```

- 使用 Qt Designer 對 QtUI 下的 UI 文件進行修改，並使用 `pyside2-uic` 對 UI 文件進行編譯
- 使用 Python IDE 例如 PyCharm 以源碼建立新項目，對代碼進行更改

<br><br>

## [AES 版本](https://github.com/marc0cheung/SendMessageSafe/tree/main/AES)

### Python 依賴包

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

### 如何使用本軟體

AES 作為一種對稱式加密算法，不需要生成密鑰，只需要以安全的方法交換 16 位密鑰與 VI 值，即可進行加密解密。該方法適合兩人以上甚至多人的對話（使用同一密鑰進行加密解密）。**但如果對話者之間沒有找到安全傳遞密鑰的辦法[1]，則 AES 的安全性是非常差的。**

<br>

**以一個情境來解釋 AES 加密與本軟體之用法：**

- Alice 與 Bob 在一個帶有審查的高風險聊天平台上進行交流，他們使用本軟體的 AES 版本來規避審查。
- Alice 和 Bob 通過線下見面（或者其它確保安全的方式）約定好密鑰和 VI 值，並在本軟體設定這兩個值。
- Alice 在 Decrypted 框中鍵入可能會被審查的敏感訊息（明文），選中「Encrypt」，即可在右側 Encrypted 框中得到加密結果，使用下方 「Copy」將密文拷貝後，轉入聊天平台中複製。
- Bob 收到 Alice 發來的密文後，複製密文，在 Encrypted 框下方選擇「Paste」，將密文貼上 Encrypted 框，選擇「Decrypt」，即可在左側 Decrypted 框中得到解密後的明文訊息。

<br>

<div align="center"><img src="https://github.com/marc0cheung/SendMessageSafe/raw/main/README.assets/SMS-AES-Mainpage.png" alt="SMS-AES-Mainpage" width="700px"></div>

<br>

[1] 一種安全傳遞密鑰的辦法是：先利用利用 RSA 傳遞 AES 的密鑰，再使用 AES 進行對話訊息的加密與解密。

<br>

### 如何基於源代碼進行修改

- （不必要）通過 anaconda 創建新環境，方便管理
- 通過 pip 安裝：

```bash
pip install pycryptodome
pip install pyperclip
pip install PySide2
```

- 使用 Qt Designer 對 QtUI 下的 UI 文件進行修改
- 使用 Python IDE 例如 PyCharm 以源碼建立新項目，對代碼進行更改

<br>
<br>
