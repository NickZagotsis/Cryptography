import requests
import os
ciphertext = requests.get("https://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/").json()
ciphertext = ciphertext['ciphertext']
print(ciphertext)
