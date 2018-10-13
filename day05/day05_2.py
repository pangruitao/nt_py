a=int(input('请输入一个整数:'))
for i in range(2,a):
    if a%i==0:
        print('%d不是质数'%a)  
        break
else:
    print('%d是一个质数'%a)


# a=int(input('请输入一个整数:'))
# i=2
# while i<a:
#     if a%i==0:
#         print('这个数不是质数')
#         break
#     i+=1
# else:
#     print('这个数是质数')
    

# a=int(input('请输入一个整数:'))
# if a<2:
#     print("不是素数")
# j=True
# for i in range(2,a):
#     if a%i==0:
#         j=False
#         i+=1
#         break
# if j:
#     print('是素数')
# else:
#     print("不是素数")

    
    
    
     