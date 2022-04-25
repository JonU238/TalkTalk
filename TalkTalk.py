import time
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
    toWrite=Username+": "+input(Username+": ")+"\n"
    if len(toWrite)==len(Username)+3:
        pass
    else:
        convo.write(toWrite)