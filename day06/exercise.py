# a=list(range(1,11))
# print(a)
#.............我的.......................#
# a=int(input("请输入数字："))
# L=[]
# count = 0
# while True:
#     if a>0:
#         L+=[a]
#         a=int(input("请输入数字："))
#         count += 1 
#     else:
#         break   
# print('L=%s'%L)

# i=0
# for j in L:
#     i+=j
# i=0
# for j in L:
#     i+=j
# print("平均数是%.2f"%(i/count))

# n=L[0]
# for d in L:
#     if d>n:
#         n=d
#     else:
#         continue
# print('最大数是:%d'%n)


# L=[]
# while True:
#     n = int(input('请输入:'))
#     if n<0:
#         break
#     L+=[n
# print('L=',L)

# s=0
# count = 0
# for x in L:
#     s += x
#     count += 1
# print('平均数是:%.2f'%(s/count))

# zuida = L[0]
# i=1
# while i<count:


#................函数写...............................#

# L=[]
# while True:
#     a = int(input('请输入一个数:'))
#     if a>0:
#         L+=[a]   #==>>   L.append(a)
#     else:
#         break    
# print('L=%s'%L)
# print("你输入的数值中最大的是:",max(L))    #打印最大的数

# L2=L.copy()
# while max(L) in L2:
#     L2.remove(max(L))                  #打印第二大的数
# print('第二大的数是:',max(L2))

# L.remove(min(L))                       #删除一个最小的数
# print(L)


# i = range(10,0,-1)
# print(i) 
# for j in i:
#     print(j,end=' ')
# print()

# L=list(range(10))
# L.remove(0)
# L+=[0]
# print (L)
#....................运用    常用    方法..............#
# L=list(range(10))
# L.append(L.pop(0))   #=> 将列表的第一个数删除并放到最后 # 
# print(L)




# a=str(input('请输入数字:'))
# if a.isdigit():
#     a=int(a)
#     if a > 2:
#         for i in range(2,a):
#             if a%i==0:
#                 print('不是质数')
#                 break
#         else:
#             print('是质数')
    






