c=int(input("enter calls"))
m=int(input("enter msgs"))
da=float(input("enter data"))
if(d<=days and c<=calls and m<=msgs and da<=data):
    print("your plan will be expired on",days-d,"days")
    print("yet to call",calls-c)
    print("yet to msg",msgs-m)
    print("yet to data",data-da)
elif(d>days):
    print("kindly recharge ur plan expired")
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
elif(d<=days and c>calls and m>msgs and da>data):
    print("your plan will be expired on",days-d,"days")
    print("calls could not connect")
    print("msg failed")
    print("your speed reduced")
elif(d<0 or c<0 or m<0 or da<0):
    print("please enter valid data")