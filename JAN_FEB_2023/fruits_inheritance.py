class fruits:
    def prime(self):
        n=int(input("enter num"))
        f=0
        if(n>1):
            for i in range(2,n):
                if(n%i==0):
                    f=1
                break
            if(f==0):
                print("prime")
            else:
                print("not prime")
        else:
            print("enter valid num")
    
class apple(fruits):
    def neon(self):
        n=int(input("enter range"))
        for i in range(0,n):
            s=i*i
            sum=0
            while(s!=0):
                sum=sum+s%10
                s=s//10
                if(i==sum):
                    print(i,end=" ")
                    
class banana(apple):
    def pattern(self):
        str1=input('Enter the string:')
        for i in range(len(str1)):
            for j in range(0,i+1):
                print(str1[j],end=' ')
            print('\n')

class pineapple(banana):
    def hello(self):
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
        


    


        
p=pineapple()
p.hello()
p.pattern()
p.neon()
p.prime()