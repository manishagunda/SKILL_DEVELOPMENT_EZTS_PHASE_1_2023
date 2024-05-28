n=int(input())
for i in range(n):
    for j in range(n):
        if(j==0 and 0<=i<n or i==0 and 0<=j<n or i==n-1 and 0<=j<n or j==n-1 and 0<=i<n):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("\n")
