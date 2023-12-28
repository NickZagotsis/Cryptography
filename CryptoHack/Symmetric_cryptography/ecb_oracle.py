from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import requests
def req(par):
    url = "https://aes.cryptohack.org/ecb_oracle/encrypt/"+par+"/"
    data = requests.get(url).json()
    return data['ciphertext']
def get_padding(l):
    return byte_list[l-1]
byte_list = []
for i in range(1,256):
    h = hex(i)[2:]
    if len(h) == 1:
        h = '0' + h
    byte_list.append(h)


flag = ""
idx2 = 8
idx = 15
while True:
    payload = 'AA'*idx2
    ciphertext = req(payload)
    last_block = ciphertext[-32:]
    if last_block=="c1511dbc19f27396337d05c2dc9d182f": #if the last block is empty we start all over again, so we check the previous block
        idx = 16 #16 because it is empty
        last_block=ciphertext[-64:-32]
    found = False
    for b in byte_list:
        inp = b + flag + get_padding(idx) * idx #this Is the padding used by AES, by adding one more byte in the plaintext the last byte gets first in the last block, ex:
        #if
        #AAAAAAAAAAAAAAAA 
        #....crypto{flag} and we append one more A we push } to the next blocks start like this:
        #}...............
        res = req(inp)
        #print("Trying ",inp)
        first_block = res[:32]
        if(last_block in first_block):
            found = True
            flag = b + flag
            found_byte = chr(int(b,16))
            if idx != 0:
                idx -= 1
            idx2+=1
            if found_byte != "{":
                print("Found: " + b +" which is \' %c \'" % found_byte)
                break
            else:
                print(flag.reverse())
                exit("Found flag!")
    if not found:
        break
idx2 = 8+16
idx = 15
while True:
    payload= idx2*'AA'
    ciphertext = req(payload)
    last_block=ciphertext[-64:-32]
    if last_block == "c1511dbc19f27396337d05c2dc9d182f":
        last_block = ciphertext[-64:-32]
        idx = 16
    found = False
    for b in byte_list:
        inp = b + flag + get_padding(idx) * idx #this Is the padding used by AES, by adding one more byte in the plaintext the last byte gets first in the last block, ex:
        #if
        #AAAAAAAAAAAAAAAA 
        #....crypto{flag} and we append one more A we push } to the next blocks start like this:
        #}...............
        res = req(inp)
        #print("Trying ",inp)
        first_block = res[:32]
        if(last_block in first_block):
            found = True
            flag = b + flag
            found_byte = chr(int(b,16))
            if idx != 0:
                idx -= 1
            idx2+=1
            if found_byte != "{":
                print("Found: " + b +" which is \' %c \'" % found_byte)
                break
            else:
                print(flag)
                print("crypto"+bytes.fromhex(flag))
                exit("Found flag!")
    if not found:
        print(flag)
        exit('Not found')