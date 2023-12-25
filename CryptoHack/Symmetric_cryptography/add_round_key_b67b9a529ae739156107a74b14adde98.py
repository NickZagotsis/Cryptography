state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    temp=[]
    for i in range(4):
        for j in range(4):
            temp.append(matrix[i][j])
    #return "".join(chr(c) for c in temp)
    return temp

def add_round_key(s, k):
    s = matrix2bytes(s)
    k = matrix2bytes(k)
    temp=[]
    for i in range(len(s)):
        temp.append(s[i] ^ k[i])
    return(temp)

print("".join(chr(c) for c in add_round_key(state, round_key)))

