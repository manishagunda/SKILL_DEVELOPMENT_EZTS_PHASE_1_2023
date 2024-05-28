a=int(input("enter num"))
c=''
b=int(input("enter position"))
'''while(a>0):
    b=a%2
    c=c+str(b)
    a=a//2
    
print(c)
if(c[b]=='1'):
    print("True")
else:
    print("False")'''
    
    
    
c=a>>b
if(c%2!=0):
    print("true")
else:
    print("false")
    