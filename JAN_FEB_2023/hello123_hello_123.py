n=input("enter string")
s=str()
for i in range (len(n)):
    if(n[i]>='0' and n[i]<='9'):
        s+=n[i]
    else:
        print(n[i],end='')
print("\n")
print(s)
    

    