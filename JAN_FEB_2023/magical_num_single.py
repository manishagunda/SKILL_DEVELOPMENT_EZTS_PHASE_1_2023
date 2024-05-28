n=int(input("enter num"))
rev=0
t=n
f=0
for i in range(2,n):
    if(n%i==0):
        f=1
        break
if(f==0):
    num=i
        d=num%10
        rev=rev*10+d
        num=num//10
for j in range(2,rev):
    if(rev%j==0):
        f=1
if(f==1):
    print("not magical prime num")
else:
    print("magical prime")
        
