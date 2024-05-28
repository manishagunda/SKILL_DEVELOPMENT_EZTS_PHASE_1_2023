n=int(input("enter row num"))
b=int(input("enter box num"))
x=n*n
if(b<=x):
    if(0<=b<=n or (n-1)*n<b<=n*n or b%n==0 or (b-1)%(n)==0):
        print("neem tree")
    else:
        print("mango tree")
else:
    print("invalid box num")
