#error
a=["python","c","java"]
#try:
for i in range(4):
    print("the index and element from array is",i,a[i])
#except:
    #print("index out of range")
    
#exception    
a=["python","c","java"]
try:
    for i in range(4):
        print("the index and element from array is",i,a[i])
except:
    print("index out of range")