#函数---变量作用域:变量的作用域指的是变量的作用范围(标识这个变量在哪里可以使用,在哪儿不可以使用)。
## 定义函数
#num = 100------------>全局变量
count = 0
def circle_area(r):
    pi = 3.14
    area = pi * r * r  #---------->局部变量
    return area
# 调用函数
c_area = circle_area(10)  #----------->全局变量
print(c_area)

#全局变量:在函数之外定义的变量,称之为全局变量,在整个文件中(包括函数内)都可以使用(通常定义在文件的顶部)。
#局部变量:在函数内部定义的变量,称之为局部变量,只能在该函数内部使用,外部无法访问(函数执行完毕后,会自动销毁其内部局部变量)。

#在函数内部使用,声明接下来要使用的是全局变量,  语法:global Xxx
#例如：
a=10000
def circle_area(r):
    pi = 3.14
    global a
    a = 100
    area = pi * r * r  #---------->局部变量
    return area
c_area = circle_area(10)    #使用 global 后，调用这个函数（类似于激活这个语句之后），里面的a打印出来就是100
print(a)

# 注意事项
#1.尽量避免在函数中使用全局变量,因为会使代码难以维护和调试
#2.考虑使用函数参数和返回值来传递数据,而不是依赖全局变量
#3.global主要用在程序的状态、配置和计数器等场景中


#------------------------------函数参数详解-----------------------------
# 一、传参方式

# 1. 位置参数:调用函数时根据函数定义时的位置来传递参数。
def reg_stu(name, age, gender, city):
    print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}
# 调用函数
stu= reg_stu("张三",18,"男","北京")   #------>这种实参与形参需顺序一一对应
print(stu)

# 2.关键字参数:调用函数时以函数定义时形参名称作为关键字,以“键=值”的形式来传递参数(不要求顺序)。
def reg_stu(name, age, gender, city):
    print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}

stu=reg_stu(name="张三",age=18,gender="男",city="北京")  #----->此处直接是使用上述函数定义时的形参进行针对性赋值,不需要顺序一一对应
print(stu)

stu2=reg_stu(gender="男",name="王武",city="上海",age=22)
print(stu2)

# 3.位置+关键字传参
stu2= reg_stu("赵四",28,gender="男",city="上海")  #---->注意:如果位置参数与关键字参数混用,关键字参数必须在位置参数之后(关键字参数之间,没有顺序要求)
print(stu2)

#总结:  场景:参数少(不超多3个),且顺序自然优先使用位置传参更方便.     场景:参数较多,或易混淆的场景优先使用关键字传参,后期易维护


#----------------------------------------------------------------------------------------------------------------
# 二、默认参数
#默认参数也称为缺省参数,用于在定义函数时,为参数提供默认值,调用函数时,可以不传递有默认值的参数。
def reg_stu(name, age, gender, city='北京'):  #-------->默认值
    print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}

# 调用函数
stu= reg_stu("张三",18,"男")  #-------->未给它重新赋值的情况下,此处打印的city为北京
print(stu)

stu=reg_stu("赵四",22,"男","深圳")   #-------->又重新赋值后,此处打印的city为深圳
print(stu)

#注意:默认参数必须放在没有默认值的参数列表的后面,一个函数在定义时是可以设置多个默认参数的。
#注意:函数调用时,如果为默认参数传递了值,则会修改默认的参数值;如果没有传递该参数,则直接使用默认值。


#----------------------------------------------------------------------------------------------------------------
# 三、不定长参数
# 介绍:不定长参数也叫可变参数,用于函数定义及调用时参数个数不确定(0个或多个)的场景。

#类型:
#1.基于位置传递
def calc_data(*args):

    return args
#函数调用
data1 = calc_data(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)#---->即用args将传递的数据封装起来
print(data1)

data2 = calc_data(100, 200, 300, 400, 500)
print(data2)
#注意:传递的所有匹配的位置参数都会被args变量收集,这些参数会合并封装为一个元组,args是元组类型(注意并不会封装关键字参数)。
#注意:args只是约定俗成的变量名,并不是关键字,这里可以使用任何合法的变量名(如 *data)。


#2.基于关键字传递
def calc_data(*args, ** kwargs):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)
    if kwargs.get('round' ):
        avg_data = round(avg_data, kwargs.get('round' ))
    return min_data, max_data, avg_data

data = calc_data(100, 200, 300, 400, round=2, count=0)
print(data)

data = calc_data(33, 11, 28, 91, 32, 75, 49)
print(data)



