def prime():
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
    
def oddeven():
    n=int(input("enter num"))
    if(n%2==0):
        print(n,"even")
    else:
        print(n,"odd")

def fact():
    n=int(input("enter num"))
    f=1
    for i in range(1,n+1):
        f=f*i
    print("factorial=",f)
    
def pattern():
    n=str(input("enter string"))
    for i in range(len(n)):
        for j in range(0,i+1):
            print(n[j],end=" ")
        print("\n")
            
def palindrome():
    n=int(input("enter num"))
    t=n
    r=0
    while(n>0):
        d=n%10
        r=r*10+d
        n=n//10
    if(t==r):
        print("palindrome")
    else:
        print("not palindrome")
    
prime()
oddeven()
fact()
pattern()
palindrome()