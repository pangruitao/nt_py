s=input('请输入第一行字符串:')
s1=input('请输入第二行字符串:')
s2=input('请输入第三行字符串:')
a=int(len(s))
a1=int(len(s1))
a2=int(len(s2))
da=a
if a<a1:
    da=a1
if da<a2:
    da=a2    # gfdydytryd
print(da)
print("+" + '-' * (da+2) + '+')
print("|" + s.center(da+2) + '|' )
print("|" + s1.center(da+2) + '|' )
print("|" + s2.center(da+2) + '|' )
print("+" + '-' * (da+2) + '+')
