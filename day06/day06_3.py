# L=[]
# for i in range(3,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         L.append(i)
# print(L)


L=[]
for i in range(101):
    if i<=2:
        continue
    else:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            L.append(i)
print(L)