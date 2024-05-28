l=int(input("enter no of lemons"))
g=3
s=7*g
if(l<0):
    print("enter correct number")   
if(l==s):
    print("sufficient")
if(l<s & l>0):
    n=s-l
    print(n,"insufficient number of lemons")   
if(l>s & l>0):
    m=l-s
    print(m,"extra number of lemons")