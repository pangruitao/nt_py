j = 1
L=[]
for i in range(1,11):
    j = (j+1)*2
    L += [j] 
print(L)
print('第一天一共有:',L[-1],'个桃子.')



# L = ((j+1)*2 for i in range(1,11))
# print(L)