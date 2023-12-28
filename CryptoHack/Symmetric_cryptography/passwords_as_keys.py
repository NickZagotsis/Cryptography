import requests
url="https://aes.cryptohack.org/passwords_as_keys/passwords_as_keys/encrypt_flag/"
enc = requests.get(url).json()
enc= bytes.fromhex(enc['ciphertext'])
fl = b'crypto{' #binary
key = [o1 ^ o2 for (o1, o2) in zip(enc, fl)]
print("".join(chr(o) for o in key)) # using this we can see that a Y is missing from the end, so we add it manually
flag = []
for i in range(len(enc)):
    flag.append(chr(enc[i] ^ key[i % len(key)]))
print("".join(flag))