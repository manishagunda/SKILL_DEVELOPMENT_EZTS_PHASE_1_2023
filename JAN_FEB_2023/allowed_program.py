roll_num=int(input("enter roll num"))
for i in range(1,121):
    if(i<21 or i==50 or i!=100 or i>100):
        print({i},"allowed")
    else:
        print({i},"not allowed")