a=int(input('请输入一个数:'))
i=1
while i<=a:
    j=1
    while j<=i:
        m = '%d×%d=%d' %(i,j,i*j)
        print("%-8s" % m,end=' ')
        # print('%d'+'×'+'%d'＝'%d' , %i %j %(i*j) end='  ')
        j+=1
    else:
        print()
    i+=1
else:
    print()    