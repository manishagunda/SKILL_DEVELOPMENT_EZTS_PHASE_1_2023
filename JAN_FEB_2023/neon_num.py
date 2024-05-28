print ("Enter the lower bound ")
lower_bound = int(input())
print ("Enter the upper bound ")
upper_bound = int(input())
def neon_or_not (num) :
    square = num * num 
    sum = 0
    while (square != 0) : 
        sum = sum + (square % 10)
        square = square // 10
    c = (sum == num)
    return c
i= lower_bound
print ("Neon numbers between",lower_bound,"and",upper_bound,"are :")
while i <= upper_bound : 
  if (neon_or_not(i)) : 
    print(i)
  i = i + 1