#-------------------------------类与对象-----------------------------------------
# 对象:对象可以理解为现实中具体的人/物在程序中的数字化身(万物皆对象)。它把一个人/物的特征和功能(属性与方法)打包到一起,是面向对象编程的基本单元。
#                                                                                                  即 谁来帮我做这件事儿
# 类: 描述的是一组具有相同属性(特征)和方法(功能/行为)的模板。

#对象与类的关系: 1.对象是类的实例,是基于类创建出来的 (实例对象)。
#             2.对象是由类创建出来的,创建对象的过程,也称为对象的实例化。一个类可以创建无数个对象。


#--------------------------------------------类的定义------------------------------------------------------
#说明:类名的命名规范,遵循大驼峰命名法,每个单词的首字母都是大写,单词之间没有分隔符,比如:UserInfo,UserAccount。
#语法规则:
#class 类名:
#    pass

#对象名 =类名()
#对象名.属性名1=属性值1
#对象名.属性名2=属性值2


#具体代码案例:_________________不推荐版
# 定义类
class Car:
    pass

#创建对象
c1 = Car()
c1.brand = "BMW"
c1.name = "X5"
c1.price = 500000
print(c1.__dict__)
# 注意:上述类的定义方式不推荐,因为它动态定义了对象的属性,这样会降低代码可维护性与可读性,不便管理


#____________推荐版如下:   定义类时直接确定实例属性
# 定义类
"""
class 类名:
    def __init__(self,参数列表):
        self.属性名 = 参数值
        self.属性名 = 参数值

# 创建对象
对象名=类名(参数列表)
"""
#代码实例
# 定义类
class Car:
    def __init__(self, c_brand, c_name, c_price) : #__init__: 初始化方法,对象创建后自动调用,主要用于设置对象的初始状态(设置对象属性)
        self.brand = c_brand       # self: 方法的第一个参数,表示当前创建的实例对象
        self.name = c_name         # 每个属性的值设定为形参承接,后续通过创建对象进行具体针对每个属性进行赋值
        self.price = c_price
# 创建对象(将具体的对象属性信息输入进去)
c1 = Car("BMW", "X5", 500000)
print(c1 .__dict__ )     #--->说明:__ dict __ 是Python中用户自定义类实例的一个特殊属性用于以字典形式存储对象的属性。
#                              即   将对象属性信息以字典方式输出

# def部分的说明:定义在类的外面的称之为函数,定义在类中的函数称之为方法。



#-------------------------------在类中定义实例方法----------------------------------------------
#在类中定义实例方法时,定义语法与之前学习的函数定义的方式是一致的。与初始化方法平齐使用def即可
#语法规则:
'''# 定义类
class 类名:
def __init __(self,形参列表):
    self.属性名 =参数值
    self.属性名=参数值

def 方法名(self,形参列表):
    
def 方法名(self,形参列表):

# 创建对象
对象名=类名(参数列表)
对象名.方法名(实参)
'''
#代码案例
class Car:
    def __init__ (self, brand, name, price):
        self.brand = brand
        self.name = name
        self.price = price

    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶…")
    def total_cost(self, discount, rate):      #与函数用法一样
        return self.price * discount + self.price * rate

c1 = Car("BMW", "X5", 500000)
total_cost =c1.total_cost(0.9, 0.1)
print(f"提车总价为:{total_cost}")




#---------------------------------------定义魔法方法------------------------------------------
#魔法方法:是指Python中提供的以双下划线开头和结尾的特殊方法,用于定义类的特殊行为,比如:__init __
#注意:魔法方法是不需要我们手动调用的,Python会在合适的时机自动调用。

#       常见魔法方法
#       __init__                              初始化方法
#       __str__+                              字符串表示的方法
#       __eq__                                比较两个对象是否相等(equal)
#       __lt,__le,__gt,__ge                   支持比较两个对象的大小(小于(less than),小于等于(less than or equal),大于(greater than)
#                                             大于等于(greater than or equal))

#代码案例:
class Car:
    def __init__ (self, brand, name, price):
        self.brand = brand
        self.name = name
        self.price = price

    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶…")
    def total_cost(self, discount, rate):      #与函数用法一样
        return self.price * discount + self.price * rate

c1 = Car("BMW", "X5", 500000)
total_cost =c1.total_cost(0.9, 0.1)
print(f"提车总价为:{total_cost}")

# 魔法方法 的使用:
def __str__ (self):
    return f"{self. color} {self.brand} {self.name} {self. price}"

def __eq__ (self, other):
    return self.color == other. color and self.brand == other. brand and self.name == other.name and self.price == other.price

def __lt__(self, other):
    return self.price < other.price    #这个return值是需要自己根据实际需求自行设定的

c1 = Car("BMW", "X5", 500000)
c2 = Car("BMW", "X5", 500000)
print(c1 == c2)     #返回布尔值      Ture
print(c1 > c2)      #返回布尔值      false