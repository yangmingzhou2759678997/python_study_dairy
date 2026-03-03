# 需求1: 定义一个函数,根据传入的数字,计算该数字阶乘的结果。

def jie_cheng (n):
    jie_cheng_num=None
    if n >1:
        jie_cheng_num = n * jie_cheng(n-1)  #--->递归: 自己函数中再次使用到自己(自己调用自己),递归得有终结点,要知道什么情况下得结束
    elif n == 1:
        jie_cheng_num = 1
    else:
        print("请输入正整数")

    return jie_cheng_num

m=int(input("你想计算哪个数的阶乘?:"))
num = jie_cheng (m)
print(num)




#------------------------------------------------------------------------------------------
#需求2:定义一个函数,用于根据传入的一批商品信息(商品名、价格、数量)、优惠(优惠券、积分抵扣)、运费信息计算订单的总金额。
#具体规则如下:
# 1.优惠券需要商品金额满5000才可以使用,且优惠券金额不能超过商品总价。
# 2.积分抵扣需要商品总金额满5000才可以使用,100积分抵扣1元(且抵扣金额不能超过商品总价,积分只能整百抵扣)。

#代码一:
def all_price(coupon,score,express,**shoppingcart_information):
    #shoppingcart_information={"商品名":(product_price,product_num)}#"优惠":(coupon,score),"运费":express
    all_price=[product_price*product_num for (product_price,product_num) in shoppingcart_information.values()]
    sum_price=sum(all_price)
    if sum_price>=5000 and coupon<=sum_price:
        last_price=sum_price-coupon
    else:
        last_price=sum_price
    if sum_price>=5000 and score//100 <= sum_price:
        last_price-=score//100
    else:
        last_price=last_price
    return last_price + express
shopping_expenses=all_price(100,4000,20,**{"搓衣板":(250,10),"5090显卡":(3000,1),"鼠标":(200,5)})
print(shopping_expenses)


#代码二:
def all_price(**kwargs):
    """
    kwargs 的结构预期为：
    {
        "discount": {"coupon": 100, "score": 4000},
        "shipping": {"express": 20},
        "products": {"商品名": (价格, 数量), ...}
    }
    """
    # 1. 直接通过嵌套字典计算商品总金额
    # 注意这里直接访问 kwargs['products']
    all_price_list = [info[0] * info[1] for info in kwargs['products'].values()]
    sum_price = sum(all_price_list)
    # 初始化最终价格
    last_price = sum_price
    # 2. 优惠券逻辑：直接从 kwargs['discount'] 中读取
    # 满5000可用，且优惠金额不能超过当前总价
    if sum_price >= 5000 and kwargs['discount']['coupon'] <= last_price:
        last_price -= kwargs['discount']['coupon']
    else:
        last_price = last_price
    # 3. 积分逻辑：直接从 kwargs['discount'] 中读取
    # 满5000可用，100积分抵1元，抵扣额不能超过当前总价
    score_deduction = kwargs['discount']['score'] // 100
    if sum_price >= 5000 and score_deduction <= last_price:
        last_price -= score_deduction
    else:
        last_price = last_price
    # 4. 加上运费并返回：直接从 kwargs['shipping'] 中读取
    return last_price + kwargs['shipping']['express']
# --- 调用部分：构造嵌套字典结构 ---
# 将所有分类信息封装进对应的子字典中
shopping_expenses = all_price(discount={"coupon":100,"score":4000},shipping={"express": 20},products={"搓衣板": (250, 10),"5090显卡": (3000, 1),"鼠标": (200, 5)})
print(f"订单总金额为: {shopping_expenses}")
















