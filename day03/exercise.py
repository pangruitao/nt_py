a=float(input('请输入你要跑的公里:'))
if a<=3:
    print('您的费用为13元')
elif 3<a<=15:
    print('您的缴费金额为:',13+(a-3)*2.3)
elif a>15:
    print('您的缴费金额为:',13+12*2.3+ \
                          (a-15)*3.45)


# 错了
# pay=13
# if a>3:
#     pay+=(a-3)*2.3
# elif a>15:
#     pay+=(a-15) * 3.45
# print(pay)
