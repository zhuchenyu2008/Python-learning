a = input("请输入四位整数")
b = a[3:4]
c = a[2:3]
d = a[1:2]
e = a[0:1]
# 区分出各个位数

g = a[3:4]
h = a[2:3]
i = a[1:2]
j = a[0:1]
#判断是否为四位数

if  g == "" or h == "" or i == "" or j == "" :
    print("请输入符合要求的四位整数")
else:
    print("你输入了："+ a)
    print("个位数：" + b)
    print("十位数：" + c)
    print("百位数：" + d)
    print("千位数：" + e)
