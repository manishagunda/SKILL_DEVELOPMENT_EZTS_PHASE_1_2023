a=list(map(int,input().split()))
s=a[0]
s1=a[0]
for i in range(len(a)):
    if(a[i]>=s):
        s=a[i]
        s1=s1+s
print(s1)
    