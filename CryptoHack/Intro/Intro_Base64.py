import base64
encodeString="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
encodedtobytes=bytes.fromhex(encodeString)
flag = base64.b64encode(encodedtobytes).decode()
print(flag)