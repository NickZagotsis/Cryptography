a=input("a=")
b=input("b=")
a=int(a)
b=int(b)
c=a%b #a mod b
while c!=0: # if a mod b != loop
    print(a,"=",a//b,"x",b,"+",c) #a = a DIV b * b + mod poy perissevei
    a=b #kaneis olisthisi ta dedomena , bazeis a ->b kai to mod sto b
    b=c
    c=a%b
print("gcd:",b)
