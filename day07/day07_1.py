i=0
L=[1,1]
for i in range(1,39):
    L.append(L[i]+L[i-1])
print(L)
