n=input("enter string")
s=str()
for i in range (len(n)):
    if(n[i]>='0' and n[i]<='9'):
        s+=n[i]
    else:
        print(n[i],end='')
print("\n")
s=int(s)
m=0
while(s>0):
    d=s%10
    m=m+d
    s=s//10
if(m>9):
    a=0
    while(m>0):
        e=m%10
        a=a+e
        m=m//10
    print(a)
else:
    print(m)
        


    
