import base64
from Crypto.Cipher import PKCS1_v1_5
from Crypto import Random
from Crypto.PublicKey import RSA


# ------------------------Generate RSA Private & Public Keys------------------------
def create_rsa_pair(is_save=False):
    f = RSA.generate(2048)
    private_key = f.exportKey("PEM")  # Generate Private Key
    public_key = f.publickey().exportKey()  # Generate Public Key
    if is_save:
        with open("crypto_private_key.pem", "wb") as f:
            f.write(private_key)
        with open("crypto_public_key.pem", "wb") as f:
            f.write(public_key)
    return public_key, private_key


def read_public_key(file_path="publicKey.pem") -> bytes:
    with open(file_path, "rb") as x:
        b = x.read()
        return b


def read_private_key(file_path="privateKey.pem") -> bytes:
    with open(file_path, "rb") as x:
        b = x.read()
        return b


# ------------------------Encrypt with Public Key------------------------
def encryption(text: str, public_key: bytes):
    # convert string to bytes
    text = text.encode('utf-8')
    # Import Public Key
    cipher_public = PKCS1_v1_5.new(RSA.importKey(public_key))
    # Encrypted Message
    text_encrypted = cipher_public.encrypt(text)
    # base64 encode and covert it to string
    text_encrypted_base64 = base64.b64encode(text_encrypted).decode()
    return text_encrypted_base64


# ------------------------Decrypt with Private Key------------------------
def decryption(text_encrypted_base64: str, private_key: bytes):
    # convert string to bytes
    text_encrypted_base64 = text_encrypted_base64.encode('utf-8')
    # base64 decode
    text_encrypted = base64.b64decode(text_encrypted_base64)
    # import Private Key
    cipher_private = PKCS1_v1_5.new(RSA.importKey(private_key))
    # Decrypt to bytes
    text_decrypted = cipher_private.decrypt(text_encrypted, Random.new().read)
    # bytes decode to string
    text_decrypted = text_decrypted.decode()
    return text_decrypted


if __name__ == '__main__':
    # Uncomment the function Below to save rsa key pair
    # create_rsa_pair(is_save=True)

    # Uncomment the 2 lines below to read public and private key
    public_key = read_public_key()
    private_key = read_private_key()

    # public_key, private_key = create_rsa_pair(is_save=False)

    # Encrypt
    text = 'John_Lee'
    text_encrypted_base64 = encryption(text, public_key)
    print('Cipher Text: ', text_encrypted_base64)

    # Decrypt
    text_decrypted = decryption(text_encrypted_base64, private_key)
    print('Decrypted Message: ', text_decrypted)
