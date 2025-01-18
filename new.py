import time
print ("this is a new world of python")
time.sleep(1)
i=input("Are you ready to strat?(y/n)")
if i=='y':
    print("Let's start")
    print("give you a lot of weclome!")
else:
    print("Goodbye")
    exit()

a = 100
while 0 < a:
    print("weclome")
    a=a-1
    time.sleep(0.1)
    if 1<a:
        print(a-1,"left")
    else:
        print("so far")


