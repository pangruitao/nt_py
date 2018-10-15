
# 购物车功能要求：
# 要求用户输入总资产，例如： 2000
# 显示商品列表，让用户根据序号选择商品，加入购物车
# 购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
# goods = [
# {"name":"电脑","price":1999},
# {"name":"鼠标","price":10},
# {"name":"游艇","price":20},
# {"name":"美女","price":98},
a = int(input('请输入总资产：'))
D={}
m=0
c=0
goods=[]
while True:
    n=str(input('商品：'))
    p=str(input('价格：'))
    m=int(p)
    c+=m
    if c<=a:
        D['name']=n
        D['price']=p
        goods.append(D)
    else:
        print('余额不足，请充值.')
        break  
print(goods)
