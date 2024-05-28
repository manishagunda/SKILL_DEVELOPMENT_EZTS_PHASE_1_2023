days=84
calls=3000
msgs=100
data=2
d=int(input("enter days"))
if(d>0 and d<85):
    c=int(input("enter calls"))
    m=int(input("enter msgs"))
    da=float(input("enter data"))
    
    elif(d<=days and c<=calls and m<=msgs and da<=data):
        print("your plan will be expired on",days-d,"days")
        print("yet to call",calls-c)
        print("yet to msg",msgs-m)
        print("yet to data",data-da)
    elif(d<=days and c>calls and m<=msgs and da>data):
        print("your plan will be expired on",days-d,"days")
        print("call could not connect")
        print("yet to msg",msgs-m)
        print("your speed reduced")
    elif(d<=days and c<=calls and m>msgs and da>data):
        print("your plan will be expired on",days-d,"days")
        print("yet to call",calls-c)
        print("msg failed")
        print("your speed reduced")
    elif(d<=days and c>calls and m>msgs and da<=data):
        print("your plan will be expired on",days-d,"days")
        print("call could not connect")
        print("msg failed")
        print("yet to data",data-d)
 
    
    
