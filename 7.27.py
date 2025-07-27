c="FuBY"
print(c)
d=c.lower()
while True:
    a=input("验证码: >>")
    b=a.lower()
    if b == d:
        print("验证码正确: %s"%c)
        break
    else:
        print("验证码错误，请重试")
