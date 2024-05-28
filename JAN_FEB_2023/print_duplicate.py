a=[1,2,5,2,6,3,5]
for i in range(0,len(a),1):
    x=a[i]%len(a)
    a[x]=a[x]+len(a)
for i in range(0,len(a)):
    if(a[i]>=2*len(a)):
        print(i)