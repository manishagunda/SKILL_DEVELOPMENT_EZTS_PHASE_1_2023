#write python program to print the difference between leftsum and rightsum
#sample input:10 4 8 3
#left sum:0 10 14 22
#right sum:15 11 3 0
#output:15 1 11 22
a=list(map(int,input().split()))
res=[]
for i in range(len(a)):
    rs=sum(a[i+1:])
    ls=sum(a[0:i])
    res.append(abs(ls-rs))
print(res)