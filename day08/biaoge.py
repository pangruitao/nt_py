    # 2. 按如下表格打印学生信息
    # +---------------+-----------+----------+
    # |     姓名      |    年龄   |    成绩   |
    # +---------------+-----------+----------+
    # |    tarena     |     15    |    99    |
    # |     china     |     70    |    98    |
    # +---------------+-----------+----------+

# print()
L=[]
zuida=0
while True:
    T={}
    n = str(input('请输入姓名:'))
    if n == '':
        print('结束输入.')
        break
    if zuida<len(n):
        zuida=len(n)
    a = str(input('请输入年龄:'))
    s = str(input('请输入成绩:'))
    # T['name']=n
    # T['age']=a
    # T['score']=s
    T = dict(name=n,age=a,score=s)
    L.append(T)
print(L)
print('+' + '-'*(zuida+12) + '+' + '-'*8 + '+' + '-'*8 + '+')
print('|' + '姓名'.center(zuida+10) + '|' + '年龄'.center(6) + '|' + '成绩'.center(6) + '|')
print('+' + '-'*(zuida+12) + '+' + '-'*8 + '+' + '-'*8 + '+')

for D in L:
    j=0
    # kage=str(D['age'])
    # kscore = str(D['score'])
    for i in D['name']:
        if ord(i)>128:
            j+=1
    print('|'+D['name'].center(zuida+12-j)+'|'+D['age'].center(8)+'|'+D['score'].center(8)+'|')
    # print('|'+D['name'].center(zuida+12-j)+'|'+kage.center(8)+'|'+kscore.center(8)+'|')
print('+' + '-'*(zuida+12) + '+' + '-'*8 + '+' + '-'*8 + '+')


    # 2. 按如下表格打印学生信息
    # +---------------+-----------+----------+
    # |     姓名      |    年龄   |    成绩   |
    # +---------------+-----------+----------+
    # |    tarena     |     15    |    99    |
    # |     china     |     70    |    98    |
    # +---------------+-----------+----------+


