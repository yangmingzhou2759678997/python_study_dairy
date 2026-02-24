'''''#字典:使用键值对(key:value)来存储数据,每一个键都对应一个值,通过键(key)可以快速找到对应的值(value)
#特点:键值对(key:value)存储、键(key)不能重复、可修改。

# 定义字典
#字典名称={key: value, key:value, key:value ... }

# 定义空字典
#字典名称={}
#字典名称=dict()

# 根据key获取value
# 值 = 字典名称[key]
# dict1={"王林":670,"韩立":556,"李慕婉":582,"紫灵":435,"许立国":608,"王政":512,"张紫":678}

######  注意:字典(dict)中的value可以是任何类型的数据,而key不能为可变类型(如:不能为 列表list、集合set、字典dict)。

# 字典 -- key不能重复(如果重复,后面的值,会覆盖前面的值)、key必须得是不可变类型(str,int,float,tuple)
# 定义字典
dict1={"王林":670,"李慕婉":608,"徐立国":580,"韩立":688}
print(dict1)
print(type(dict1))


# key必须得是不可变类型(str,int,float,tuple),不能是list、set、dict
dict2 = {0:670, 1.5:608, (1,2):580, ('A' , 'B' ):688}
print(dict2)


# 访问
print(dict1["李慕婉"])  #获取
dict1["李慕婉"]=688   #value值可修改
print(dict1)





#------------------------------------------字典常用操作---------------------------------------
# 添加      字典名称[key]=value         往指定字典中添加key-value键值对                dict1["涛哥"]= 688
#
# 删除      字典名称.pop(key)           删除字典中指定的key,并返回该key对应的value      score=dict1.pop("涛哥")
#          del 字典名称[key]           删除字典中指定的键值对                         del dict1["涛哥"]
#
#修改       字典名称[key]= value        修改字典中指定的key对应的值                    dict1["小智"]= 658
#          字典名称[key]               根据key获取value                            dict1["涛哥"]
#          字典名称.get(key)           根据key获取value                            dict1.get("涛哥")
#
#查询       字典名称.keys()             获取所有的key                               dict1.keys()
#          字典名称.values()           获取所有的value                             dict1.values()
#          字典名称.items()            获取所有的key-value键值对                    dict1.items ()


#代码示例
dict1={"王林":670,"李慕婉":608,"许立国":580,"韩立":688}
print(dict1)

# 添加 - key不存在就是添加
dict1["涛哥"]=550
print(dict1)

# 修改 -key存在就是修改
dict1["涛哥"]=620
print(dict1)

# 查询
print(dict1["涛哥"])#根据key获取value
print(dict1.get("涛哥"))#根据key获取value
print(dict1.keys())#获取所有的key
print(dict1.values())#获取所有的value
print(dict1.items())#获取所有的键值对 key:value

# 删除
score=dict1.pop("许立国")
print(score)
print(dict1)

del dict1["韩立"]
print(dict1)

# 遍历
for k in dict1.keys( ):
    print(f"{k} : {dict1[k]}")
for item in dict1.items( ):
    print(f"{item[0]} : {item[1]}")
for k,v in dict1.items():
    print(f"{k} : {v}")
'''''


#------------------------------------------案例----------------------------------------------
#需求:开发一个购物车管理系统,实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据,通过控制台菜单与用户交互。具体功能如下:
#1. 添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量,保存该商品信息到购物车。
#2. 修改购物车:要求用户输入要修改的购物车商品名称,然后再提示输入该商品的价格、数量,输入完成后修改该商品信息。
#3. 删除购物车:要求用户输入要删除的购物车名称,根据名称删除购物车中的商品。
#4. 查询购物车:将购物车中的商品信息展示出来,格式为:“商品名称:xxx,商品价格:xxx,商品数量:xxx"。
#5. 退出购物车

dict={}

while True:
    menu = input("你想要执行哪项操作? 1.添加购物车 2.修改购物车 3.删除购物车 4.查询购物车 5.退出购物车: ")
    match  menu:
        case "1":
            a=input("请输入你要添加的商品名:")
            dict[a]={"价格":float(input("请录入商品的价格:")),"数量":int(input("请录入商品的数量:"))}
        case "2":
            b = input("请输入你要修改的商品名:")
            dict[b]= {"价格":float(input("请录入商品新的价格:")),"数量":int(input("请录入商品新的数量:"))}
        case "3":
            del dict [input("请输入你要删除的商品名:")]
        case "4":
            dict_list = list(dict.items())
            print(f"当前购物车存储的商品信息如下:",dict_list)
        case "5":
            break
