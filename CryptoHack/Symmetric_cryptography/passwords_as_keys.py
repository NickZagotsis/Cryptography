import hashlib
import binascii
import requests
from Crypto.Cipher import AES
result = requests.get('https://aes.cryptohack.org/passwords_as_keys/encrypt_flag')
ciphertext_hex = bytes.fromhex(result.json()["ciphertext"])

with open('words.txt','r') as f:
    for passwords in f:
        attempted_password = hashlib.md5(passwords.strip().encode()).hexdigest() #hash each password
        cipher = AES.new(bytes.fromhex(attempted_password),AES.MODE_ECB) # they key must be in bytes
        try:
            decrypt = cipher.decrypt(ciphertext_hex) #try to decrypt
            result = binascii.unhexlify(decrypt.hex())#make the decrypted binary
            if result.startswith("crypto".encode()):
                print("key: %s" % passwords)
                print(result.decode()) # decode it
        except ValueError as e :
            continue
        except Exception as e:
            print(e)