# ---------------类型注解: 是Python中的一种语法特性,用于明确标识变量、函数参数和返回值的数据类型,从而使代码更清晰、更安全、更易维护。
#代码案例:
# 定义变量
a: int = 695
score: float = 98.5
hobby: str= "Python"
flag: bool= True
pic: None= None
names: list[str] = ["A", "C", "E" ]    #例如,这个定义即表示这个列表里的数据都是字符类型
phones: set[str | int] = {"13309091111", "15209109121"}   #这个定义即表示这个列表里的数据都是字符或者int类型
options: dict[str, int] = {"count": 0, "total": 0}
goods: tuple[str,int,int] =("手机",5999,1)
#注意:---------类型注解只是起到语法提示作用,并不会影响程序运行的结果,因为python是动态语言


# -----------------类型推断: 是指Python解释器自动推断出变量、表达式或函数返回值的数据类型的能力,而无需开发者显式声明。----------------

# -----注意:在对变量进行直接赋值,或者涉及到变量的运算、容器的推导等场景时,解释器会自动推导出变量的类型。此时是不用专门进行注解声明的




#-----------------------------------函数类型注解--------------------------------------
#为函数添加类型注解, 其实主要就是为函数的参数和返回值添加类型注解,具体语法如下:
def calc(scores:list[int]) -> float:

    return sum(scores) / len(scores)


def calc_data(scores: list[int]) -> tuple[int, int, float]:   #函数形参直接在括号内注解,返回值类型使用->后进行注解
    max_v = max(scores)
    min_v = min(scores)
    avg_v = sum(scores) / len(scores)
    return max_v, min_v, avg_v

#总结:对于需要团队协作开发和长期维护的项目,推荐使用类型注解

