
# s='真好　真帅'
# for ch in s:
#     print("ch----->", ch)
# else :
#     print('else语句被执行')
# print('执行完毕')

# s=range(2,9,2)
# for a in s:
#     print('a--->',a)


#...........for语句的嵌套.....................#
# for x in "ABC":
#     for y in "123":
#         print(x+y,end=' ')
# print()

# for x in range(5):
#     if x == 2:
#         continue
#     print(x)

# for x in range(0,10):
#     if x%2==0:
#         continue
#     print(x,end=' ')
# print()

# i=0
# while i<=10:
#     if i%2==1:
#         print(i,end=' ')
#     i+=1
# print()


#.........重要,用while语句来实现输出１～１０的奇数................#
# i=0
# while i<=10:
#     if i%2==0:
#         i+=1
#         continue
#     print(i,end=' ')
#     i+=1
# print()

# for i in range(1,11,2):
#     print(i,end=' ')
# print()



# i=0
# for a in range(101):
#     if a%2==0 and a%3==0 and a%5==0 and a%7==0:
#         continue
#     i+=a
# print(i)


# L = list(range(10))
# # print(L)
# print(L+L)


#...........for语句的嵌套.....................#
# for x in "ABC":
#     for y in "123":
#         print(x+y,end=' ')
# print()
# a=int(input('请输入直角边长:'))


# x=[' ','  ','   ']
# y=['###','##','#']
# for i in x:
#     for j in y:
#         print(i+j)

# n=0
# for i in range(101):
#     if i%2==0:
#         n+=i
#     else:
#         continue
# print(n)


s=str(input('请输入账号：'))
s1=str(input('请输入密码：'))
L = ['seven','123']
for i in L:
    if i==s:
    else:
        print('账号错误！')
        break
    



        
         









