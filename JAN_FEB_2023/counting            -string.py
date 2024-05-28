name="manisha gunda07@gmail.com"
d=0
vs=0
v=0
c=0
ss=0
for i in range(len(name)):
    if(name[i]>='0' and name[i]<='9'):
        d+=1
    elif(name[i]==" "):
        vs+=1
    elif(name[i]>=chr(0) and name[i]<=chr(31) or name[i]>=chr(33) and name[i]<=chr(47) or name[i]>=chr(58) and name[i]<=chr(64) or name[i]>=chr(91) and name[i]<=chr(96) or name[i]>=chr(123) and name[i]<=chr(127) or name[i]>=chr(128) and name[i]<=(255)):
        ss+=1
    elif(name[i]=='a' or name[i]=='e' or name[i]=='i' or name[i]=='o' or name[i]=='u'or name[i]=='A' or name[i]=='E' or name[i]=='I' or name[i]=='O' or name[i]=='U'):
        v+=1
    else:
        c+=1
print("digits",d)
print("vowels",v)
print("special characters",ss)
print("consonants",c)
print("void spaces",vs)

