# 属性分为:
# 1.实例属性:实例属性属于每个具体对象的属性,每个对象都是独立的。(各个对象特有的数据)
# 2.类属性:类属性是属于类本身的属性,所有实例共享的。(所有对象共享的数据或配置)
class Car:
    wheel = 4 # 轮胎数量           #类属性(通过 类名.属性的方式操作    所有属性共享)
    tax_rate =0.1 # 购置税
    def __init__(self, c_brand, c_name, c_price):
        self.brand = c_brand
        self.name = c_name             #实例属性(通过 实例对象.属性的方式操作    每个对象独特的自己的属性)
        self.price = c_price
        self.wheel = 2
    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶 .. ")

c1 = Car("BYD", "汉",180000)
c2 = Car("Tesla", "Model Y", 260000)
print(c1.__dict__)
#说明: 通过实例查找属性时, 会先查找实例属性, 实例属性不存在时, 再查找类属性。
print(c1.wheel)      #此时输出的是2