L=[1,3,4,2,1,5,6,54,6,2,6,87,78,5,4,4,67,78,345,3,76,4,56,6,87]
L2=[]
for i in L:
    if i not in L2:
        # L2 += [i]
        L2.append(i)
print(L2)

L3=[]
for j in L:
    if L.count(j)==2:      #if j not in L3 and L.count(j)==2:
        if j not in L3:    #    L3.append(j) 
            L3.append(j)
print(L3)




