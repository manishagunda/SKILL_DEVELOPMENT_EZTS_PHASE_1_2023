a=input("enter mail id")
b=input("enter password")
c="manisha28@gmail.com"
d="manisha28"
if(a!=c and b!=d):
    print("login failed both are invalid")
elif(a!=c):
    print("invalid mail id")
elif(b!=d):
    print("invalid password")
else:
    print("login successfully")

    
    