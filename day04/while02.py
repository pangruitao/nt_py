# i=1
# j=1
# while j<=10:

#     while i<=20:
#         print(i,end=' ')
#         i+=1
#     else:
#         i=1
#         print()
#     j+=1


j=1
while j<=10:
    i=1
    print('第%d行' %j,end="  ")
    while i<=20:
        print(i,end=' ')
        i+=1
    else:
        print()
    j+=1

