# a = int(input("请输入数字："))
# for i in range(a):
# 	print("*"*(i+1))
# for i in range((a-1),0,-1):
#     print("*"*(i))
# # a=int(input())
# # for i in range(a):
# i=1
# j=1
# for i in range(1,10):
# 	for j in range(1,10):
# 	    if i>=j:
# 		    print('%d×%d=%d' % (i,j,i*j),end=' ')
# 	print()

# L = ['I',' ','am',' ','a',' ','gril']
# L1 = []
# L.reverse()
# print(L1)

# L=str(input())
# L1=[]
# j=len(L)
# for i in L[j::-1]:
#     j=j-1
#     L1.append(i)
# print(L1)

# a = range(1,101)
# b = list(a[0:11])
# b1 = [i for i in a if i%3==0]
# b2 = [i for i in a if i<=50 if i%5==0]
# print(b)
# print(b1)
# print(b2)

# L=['Adam','Lisa','Bart','Paul']
# for i in range(3):
#     print(L[i])


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
    T['name']=n
    T['age']=a
    T['score']=s
    L.append(T)
print(L)
print('+' + '-'*(zuida+12) + '+' + '-'*8 + '+' + '-'*8 + '+')
print('|' + '姓名'.center(zuida+10) + '|' + '年龄'.center(6) + '|' + '成绩'.center(6) + '|')
print('+' + '-'*(zuida+12) + '+' + '-'*8 + '+' + '-'*8 + '+')

for D in L:
    j=0
    D['age']=int(D['age'])
    D['score'] = str(D['score'])
    for i in D['name']:
        if ord(i)>128:
            j+=1
    print('|'+D['name'].center(zuida+12-j)+'|'+D['age'].center(8)+'|'+D['score'].center(8)+'|')
print('+' + '-'*(zuida+12) + '+' + '-'*8 + '+' + '-'*8 + '+')




    # 2. 按如下表格打印学生信息
    # +---------------+-----------+----------+
    # |     姓名      |    年龄   |    成绩   |
    # +---------------+-----------+----------+
    # |    tarena     |     15    |    99    |
    # |     china     |     70    |    98    |
    # +---------------+-----------+----------+
