
L=[]
while True:
    n = str(input('请输入姓名:'))
    if n == '':
        print('结束输入.')
        break
    a = str(input('请输入年龄:'))
    s = str(input('请输入成绩:'))
    # T['name']=n
    # T['age']=a
    # T['score']=s
    T = {'name':n,'age':a,'score':s}    # =>关键字传参建立字典
    L.append(T)
print(L)


