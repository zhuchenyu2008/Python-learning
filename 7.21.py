import random
b = random.randint(1,100)
c = False
e = 0
while not c:
    a = eval(input("输入数字:>>"))
    if a == b:
        print("猜对了")
        c = True
    elif a > b :
        print("猜大了")
        c = False
        e = e + 1

        if a-b < 10 :
            print("但是离答案很近了")

        if e > 10:
            d = input("你已经猜了%s次还要继续吗？（y/n） >>" % e)
            if d == 'y':
                c = False
            else:
                c = True

    elif a < b :
        print("猜小了")
        c = False
        e = e + 1

        if b-a < 10:
            print("但是离答案很近了")

        if e > 10:
            d = input("你已经猜了%s次还要继续吗？（y/n） >>" % e)
            if d == 'y':
                c = False
            else:
                c = True

if c == True:
    print("答案是：",b

