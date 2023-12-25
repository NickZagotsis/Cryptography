string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
stringt = [o for o in bytes.fromhex(string)]
for i in range(256):
    order = [ i ^ o for o in stringt ] #XOR every character with the ord number of each ascii char till you find the flag
    possible_flag = "".join([chr(o) for o in order])
    if possible_flag.startswith("crypto"):
        print(possible_flag)
        exit()