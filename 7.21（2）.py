a=input("注册/登录 （1/2）： >>")
user_name="admin"
user_password="admin"

if a == '1':
    print("注册程序启动")
    mistake=True
    while mistake==True:

        user_name=input("输入用户名： >>")
        user_password=input("输入密码： >>")
        user_password2=input("确认密码： >>")

        if user_password == user_password2:
            print("注册成功")
            mistake = False

            user_choice=input("是否进入登录程序？ (y/n) >>")
            if user_choice == 'y':
                a="2"
                break
            else:
                print("已退出")
                exit()
        else:
            print("两次密码不同，请重试")


if a == '2':
    print("登录程序启动")
    mistake = True
    while mistake == True:
        user_name_login=input("输入用户名： >>")
        user_password_login=input("输入密码： >>")
        if user_name_login==user_name and user_password_login==user_password:
            print("登录成功")
            if user_name=="admin":
                print("管理员登录")
                mistake = False
            else:
                print("欢迎你，%s" %user_name)
                mistake = False
        else:
            print("用户名或密码错误")
            mistake = True


else:
    print("输入错误"



