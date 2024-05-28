c=30
def fun():
    a=10
    global b
    b=20
    print("a=",a)
    print("b=",b)
    print("c=",c)
fun()
# print("after fun a=",a) as a is local
print("after fun b=",b)
print("after fun c=",c)

def apple():
    print(b,c)
apple()