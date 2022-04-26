import time
import datetime
from turtle import towards
toWrite=""
Username = input("Username: ")
while(toWrite!="!quit"):
    convo = open("convo.txt","r+")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    for i in convo.readlines()[-20:]:
        if(i[-1]=="\n"):
            print(i[:-1])
        else:
            print(i)
    toWrite= str(datetime.datetime.now())[11:-7]+" "+Username+": "+input(Username+": ")+"\n"
    if len(toWrite)==len(Username)+12:
        pass
    else:
        convo.write(toWrite)
        print(len(toWrite))