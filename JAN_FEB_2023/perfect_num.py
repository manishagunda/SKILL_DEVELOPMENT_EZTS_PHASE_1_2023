a=int(input("enter num"))
s=0
for i in range(1,a):
    if(a%i==0):
        s=s+i
if(s==a):
    print("perfect num")
else:
    print("imperfect num")