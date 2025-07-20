import time
print ("this is a new world of python")
time.sleep(1)
i=input("Are you ready to strat?(y/n)")
if i=='y':
    print("Let's start")
    print("give you a lot of welcome!")
else:
    print("Goodbye")
    exit()

a = 100
b = 1
while 0 < a:
    print("welcome")
    a= a - b
    time.sleep(0.1)
    print("这是第", 100-a , "个welcome")

print("break")

#注释

"""

多行注释

"""

