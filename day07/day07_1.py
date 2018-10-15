i=0
L=[1,1]
for i in range(1,39):
    L.append(L[i]+L[i-1])
print(L)

L=[1,1]
while len(L)<=40:
    L.append(L[-1]+L[-2])
print(L)

#.........经典..........#
L = []
a = 0   #==>a表示当前数b的前一个
b = 1   #==>b永远绑定当前的一个值
while len(L) < 40:
    L.append(b) #==>把当前的值加入进Ｌ
    c = a + b
    a = b　　　　# => a , b = b , a+b
    b = c
print(L)