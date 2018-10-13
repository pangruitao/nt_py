i = 1
j = 1
for i in range(1,10):
    for j in range(1,10):
        if j <= i:
            m ="%d×%d=%d" %(i,j,(i*j))
            print("%-8s" %m, end=' ')
        else:
            break
    print()