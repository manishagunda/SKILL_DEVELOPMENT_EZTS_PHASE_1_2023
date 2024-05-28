a=list(map(int,input().split()))
s=0
m=0
c=[]
d=[]
q=[]
for i in range(0,len(a)):
    s=0
    for j in range(0,i):
        s=s+a[j]
    c.append(s)
print(c)
for i in range(0,len(a)):
    m=0
    for j in range(i+1,len(a)):
        m=m+a[j]
    d.append(m)
print(d)
for i in range(len(c)):
            q.append(abs(c[i]-d[i]))
print(q)

        
        
    
    