i=['seven','alex']
j='123'
number=1
while number<=3:
    S1=str(input("请输入账号："))
    S2=str(input("请输入密码："))
    if S1 in i:
        if S2==j:
            print('登陆成功')
            break
    else:
        if number == 3:
            print('登录失败,三次机会已用完')
        else :
            print('登录失败')
    number+=1
