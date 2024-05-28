#print all num except 50,75,100 rollnum
rollnum=0
while(rollnum<=120):
    if(rollnum==50 or rollnum==75 or rollnum==100):
        rollnum+=1
        continue
    print("allowed to event",rollnum)
    rollnum+=1
#print all num except from 50 rollnum
rollnum=0
while(rollnum<=120):
    if(rollnum==50):
        rollnum+=1
        break
    print("allowed to event",rollnum)
    rollnum+=1