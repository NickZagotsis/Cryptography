from Crypto.Util.number import *
first = "label"
second = 13
temp = []
for c in first:
    temp.append(chr(ord(c)^second)) #take the ascii number and xor it with the desired number, then take the character representing the XOR'ed number
print("".join(temp))

