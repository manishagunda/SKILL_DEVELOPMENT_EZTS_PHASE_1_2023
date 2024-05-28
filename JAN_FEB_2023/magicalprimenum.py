def prime(i):
    k=0
    for l in range(2,n):
        if i%l==0:
            k+=1
    if k==0:
        return True
    return False
for n in range(1000):
    if prime(n) and prime(int(str(n)[::-1])):
        print(n,end=' ')