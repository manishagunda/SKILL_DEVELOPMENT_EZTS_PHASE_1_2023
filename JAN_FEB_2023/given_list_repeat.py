a=list(map(int,input().split()))
print(a)
for i in a:
    if(a.count(i)==1):
        print(i)