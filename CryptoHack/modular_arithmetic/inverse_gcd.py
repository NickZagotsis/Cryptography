def extendedGcd():
    a=input("a=")
    b=input("b=")
    a=int(a)
    al = a
    b=int(b)
    c=a%b #a mod b
    p = []
    p.append(0)
    p.append(1)
    idx = 2
    while c!=0: # if a mod b != loop
        t = a//b
        p.append((p[idx-2] - (p[idx-1]* t )) % al) # einai typos standard : https://web.archive.org/web/20230511143526/http://www-math.ucdenver.edu/~wcherowi/courses/m5410/exeucalg.html
        idx+=1
        a=b #kaneis olisthisi ta dedomena , bazeis a ->b kai to mod sto b
        b=c
        c=a%b
    if(c==0 and b == 1):
        print("Inverse:",p[-1])
    else:
        print("No inverse")
def main():
    extendedGcd()

if __name__ == "__main__":
    main()