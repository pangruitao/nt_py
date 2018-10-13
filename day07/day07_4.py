
L=[]
T={}
while True:
    n = str(input('请输入姓名:'))
    if n == '':
        print('结束输入.')
        break
    a = str(input('请输入年龄:'))
    s = str(input('请输入成绩:'))
    T['name']=n
    T['age']=a
    T['score']=s
    L.append(T)
print(L)


