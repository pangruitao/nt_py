# a=int(input('请输入一个数字:'))
# i=1
# print('#'*a)
# while i<=a-2:
#     print('#'+' '*(a-2)+'#')
#     i+=1
# print('#'*a)


a=int(input('请输入一个数字:'))
i=1
while i<=a:
    if i==1:
        print("#"*a)
    elif i==a:
        print('#'*a)
    else:
        print('#'+' '*(a-2)+'#')
    i+=1

