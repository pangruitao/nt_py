#
##
###
# a=int(input('请输入直角边长:'))
# i=1
# while i<=a:
#     print("#"*i)
#     i+=1

#
##
###
# a=int(input('请输入直角边长:'))
# i=1
# while i<=a:
#     t='#'*i
#     print('%s'%t)
#     i+=1

#
##
###
# a=int(input('请输入直角边长:'))
# for i in range(a):
#     print('#'*(i+1))


  #
 ##
###
# a=int(input('请输入直角边长:'))
# i=1
# while i<=a:
#     t='#'*i
#     print(' '*(a-i) + '%s'%t)
#     i+=1


# a=int(input('请输入直角边长:'))
# i=1
# j=1
# while i<=a:
#     while j<=a:
#         print(' '*(a-j) + '#'*i)
#         j+=1
#         i+=1


  #
 ##
###
# a=int(input('请输入直角边长:'))
# for i in range(a):
#     print(' '*(a-1-i) + '#'*(i+1))

###
##
#
# a=int(input('请输入直角边长:'))
# i=a
# while i>0:
#     print('#'*i)
#     i=i-1
    
###
##
#
# a=int(input('请输入直角边长:'))
# for i in range(a):
#     print('#'*(a-i))

###
 ##
  #
# a=int(input('请输入直角边长:'))
# i=1
# while i<=a:
#     print(' '*(i-1)+'#'*(a+1-i))
#     i+=1

###
 ##
  #
# a=int(input('请输入直角边长:'))
# for i in range(a):
#   print(' '*i + '#'*(a-i))


#............................................
a=int(input('请输入直角边长:'))
for i in range(a):
    print('#'*(i+1))

for i in range(a):
    print(' '*(a-1-i) + '#'*(i+1))

for i in range(a):
    print('#'*(a-i))

for i in range(a):
  print(' '*i + '#'*(a-i))
