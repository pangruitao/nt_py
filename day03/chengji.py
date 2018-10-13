a=float(input('请输入语文成绩：'))
b=float(input('请输入数学成绩：'))
c=float(input('请输入英语成绩：'))

# 经典＃
zhuida = a
if b>a:
    zhuida=b
if c>zhuida:
    zhuida=c
print('最大的成绩是:',zhuida)



# print("平均成绩%.2f" %((a+b+c)/3))

# 法２
# x=a if a>b else b
# x=x if x>c else c
# print("最高的成绩为:",x)
# y=a if a<b else b
# y=y if y<c else c
# print('最低成绩为:',y)
# m=(a+b+c)/3
# print("平均成绩:%.2f" %m)


  

# 法１
# if a>=b:
#     x=a
# elif a<b:
#     x=b
# if x>=c:
#     x=x
# elif x<c:
#     x=c
# print('您三科成绩中最高的分数是:',x)
# if a>=b:
#     y=b
# elif a<=b:
#     y=a
# if y>=c:
#     y=c
# elif y<=c:
#     pass
# print("您三科中成绩最少的是:",y)
# m = (a+b+c)/3
# print('你的平均成绩为:%.2f' % m)




