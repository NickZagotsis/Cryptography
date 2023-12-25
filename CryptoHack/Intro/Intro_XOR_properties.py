# Commutative: A ⊕ B = B ⊕ A
# Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
# Identity: A ⊕ 0 = A
# Self-Inverse: A ⊕ A = 0
'''
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
'''
def xor(str1,str2):
    str1 = bytes.fromhex(str1)
    str2 = bytes.fromhex(str2)
    return bytes(a^b for a,b in zip(str1,str2)).hex()


KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2_3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
KEY_FLAG = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

KEY2 = xor(KEY2_1,KEY1) # do KEY1 xor KEY2 xor key1 = KEY2
KEY3 = xor(KEY2_3,KEY2) # do KEY2 XOR KEY3 XOR KEY2 = KEY3
KEY4 = xor(KEY2_1,KEY3) # key1 xor key2(key1 xor key2 xor key1) xor key3(key2 xor key3 xor key2) = flag

FLAG = xor(KEY4,KEY_FLAG)
print(bytes.fromhex(FLAG).decode())




