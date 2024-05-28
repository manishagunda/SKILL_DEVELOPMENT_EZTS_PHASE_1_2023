a=[4,3,4,2,1,2,1,5,5,8,3]
c=0
for i in range(0,len(a),1):
    c=c^a[i]
print(c)