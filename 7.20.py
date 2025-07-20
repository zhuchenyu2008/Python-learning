a = "abcd"

print("the letter is : %s" %a)

b = 123

print("the number is : %d" %b)


c = a +" "+ str(b)
print("combined: %s" %c)

print("_________________________")

d = "hello"
e = "world"
print(d+e)
print("----------------------------")

f = input("输入你要判断的第一个文字或数字")
g = input("第二个")

h = g in f

if h == True :
    print("包含")
else :
    print("不包含")

print("-----------------------")

i = input("加法计算器：依次输入两个 \n第一个：")
j = input("第二个：")

print(i,"+",j,"=",  eval(i) + eval(j))