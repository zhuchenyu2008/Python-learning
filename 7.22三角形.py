a=0
b="*"
c="      "
d=6

while a<7:
    print(c,b)
    b=b+"**"
    a=a+1
    d=d-1
    c=c[0:d]