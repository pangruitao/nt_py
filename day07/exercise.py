#......................................................................................#
# d={ 1:'春季有1,2,3月',
#     2:'夏季有4,5,6月', 
#     3:'秋季有7,8,9月',
#     4:'冬季有10,11,12月'}
# yuefen = int(input('请输入你想知道的月份:'))
# if yuefen in d:
#     print(d[yuefen]) 
# else:
#     print('信息不存在')

#.......................................................................................#
# 输入一串字符串，打印出这个字符串中出现过的字符及出现的次数
# 如：
# ａ：４次
# ｂ：５次

# s=str(input('请输入一串字符：'))
# d={}
# for x in s:
#     if x not in d:
#         d[x] = 1
#     else:
#         d[x] = d[x]+1
# print(d)
# for k,v in d.items():
#     print(k,':',v,'次')  #==>  print('%s:%s次'%(k,v))





    # 写一个程序，让用户分两次输入一人的信息：
    #     信息包含　姓名和电话号码
    # 让用户输入多个人的信息，当输入姓名为空时结束输入
    # 把用户输入的数据存于字典中
    #     姓名作为键，电话号码作为值
    # 最后打印存储数据的字典

# a = {}  #==>  a = dick()
# while True:
#     name = str(input('请输入姓名:'))         
#     if name =='':          #==>if not name:  回车代表空值。
#         break
#     telephone = str(input('请输入电话:'))
#     a[name] = telephone
# print(a)
#.................................................#
#   已知有如下字符串的列表:
#     L = ['Tarena', 'XiaoZhang', 'xiaowang']
#   生成如下字典:
#     d = {'Tarena':6, 'XiaoZhang':9,
#           'xiaowang':8}
# L = ['Tarena','Xiaoming','Xiaozhang']
# a={x:len(x) for x in L} 
# print(a)

# L = ['Tarena','Xiaoming','Xiaozhang']
# a = {}
# for x in L:
#     a[x] = len(x) 
# print(a)

Nos = [1001,1002,1005,1006]
names = ['Tom','Jack','Jerry','Xiaoming']
a = {Nos[i]:names[i] for i in range(len(Nos))}
print(a)