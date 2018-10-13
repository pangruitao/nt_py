a=int(input('请输入正方形的宽和高:'))
for i in range(1,a+1):
    for j in range(0,a):
        print(i+j,end=' ')
        if j == a-1:
            print()


# a=int(input('请输入正方形的宽和高:'))
# n=0
# for i in range(1,a+1):
#     n+=1
#     for j in range(n,n+a):
#         print(j,end =' ')
#     print()

# a=int(input('请输入正方形的宽和高:'))
# n=0
# for i in range(1,a+1):
#     n+=i
#     for j in range(n,n+a):
#         print(j,end =' ')
#     n=0
#     print()

# n=int(input('请输入正方形的宽和高:'))
# for x in range(1,n+1):
#     for y in range(x,x+n):
#         print(y,end=' ')
#     print() 

# n=int(input("请输入一个数:"))
# j=0
# while j<n:
#     i=j
#     while i<=j+n:
#         print(i+1,end=' ')
#         i+=1
#     print()
#     j+=1



