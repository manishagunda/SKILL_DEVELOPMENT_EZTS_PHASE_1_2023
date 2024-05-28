s='jmtcdpmkzmrrmkmdfcyprrmembegdrcbqgqrcp'
n=int(input())
for i in range (len(s)) :
    x = ord(s[i])
    x = x + n
    if x < 97 :
        x +=26
    if x > 122 :
        x -=26
    print(chr(x), end ="" )