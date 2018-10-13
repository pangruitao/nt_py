# s='asdf'
# a=int(len(s))
# print(s[0])
# print(s[-1])
# if a%2==1:
#     print(s[a//2])
# else:
#     pass

# s=input('请输入字符串：')
# a=int(len(s))
# print(s[1:a-1])
# m=s[:]
# n=s[-1:-a-1:-1]
# if m == n:
#     print('为对称文字')
# else:
#     print('不对称')
# print(m)
# print(n)

# a=input("请输入一个字符串:")
# if a:
#     print(ord(a[0:1]))
# else:
#     print('字符串为空。')



# b=int(input('请输入一个整数(0~65535):'))
# if 0<=b<=65535:
#     print('这个数字代表的字符为：' , chr(b))
# else:
#     print('输入的数字不在范围之中。')

# /............

# s=input('请输入一个字符串：')
# blank_count=s.count(' ')
# print('空格的个数是:',blank_count)

# s2=s.strip()
# print("去掉空格后是:",s2)

# if s2.isdigit():
#     print("您刚才输出的都是数字。")
#     n=int(s2)
#     if n>100:
#         print("您输入的数字大于100.")
# else:
#     print('您输出的不全是数字。')

a="hello world"
b="abcd"
c="aaaaaa"

# print('%20s' % a)
# print('%20s' % b)
# print('%20s' % c)
# print("%20s" % "hello world")

A=int(len(a))
B=int(len(b))
C=int(len(c))

# 　经典比较大小　＃
zhuida = A
if A<B:
    zhuida=B
if C>zhuida:
    zhuida=C

# print("输出最大值是:",zhuida)
# print(' '*(zhuida-A)+a)
# print(' '*(zhuida-B)+b)
# print(' '*(zhuida-C)+c)

print('********************')
o = "%" + str(zhuida) + "s"
print('fmt=',o)
print(o %a)
print(o %b)
print(o %c)
print('%11s' %a)



