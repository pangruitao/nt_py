i=1
while i<=20:
    print( str(i).center(4))
    if i%5 == 0:
        print('\n')
    i+=1
else:
    print("完成")