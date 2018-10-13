a=float(input('输入体重（公斤）:'))
b=float(input('输入身高（米）:'))
BIM=a/(b**2)
print('您的BIM值为%.2f:'%BIM)
if BIM<18.5:
    print("体重过轻")
elif 18.5<=BIM<=24:
    print('体重正常')
elif BIM>24:
    print('体重正常')
