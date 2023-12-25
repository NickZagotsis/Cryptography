def extendedGcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1 # init
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def main():
    a = int(input("a="))
    b = int(input("b="))
    gcd,x,y=extendedGcd(a,b)
    print("GCD:",gcd,"X:",x,"Y:",y)

if __name__=="__main__":
    main()