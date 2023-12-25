enc="0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
enc = bytes.fromhex(enc)
fl = b'crypto{' #binary

key = [o1 ^ o2 for (o1, o2) in zip(enc, fl)] + [ord("y")]
print("".join(chr(o) for o in key)) # using this we can see that a Y is missing from the end, so we add it manually
flag = []
for i in range(len(enc)):
    flag.append(chr(enc[i] ^ key[i % len(key)]))
print("".join(flag))