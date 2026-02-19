"""#模式匹配  match ... case
#执行流程:
# 1. 首先计算match指定的表达式的值。
# 2. 从上到下依次和case后面的值进行匹配,匹配正确,就执行对应语句。
# 3. 如果前面所有的case都没有匹配上,就会执行默认的case

#案例：
# 工作日程安排
day=input("请输入星期几(1-7):")
match day:
    case "1":
        print("周一:工作会议日")
    case "2":
        print("周二:学习培训日")
    case "3":
        print("周三:项目开发日")
    case "4":
        print("周四:代码审查日")
    case "5":
        print("周五:总结规划日")
    case "6"|"7":
        print("周末:休息放松")
    case _:
        print("输入错误")
"""

#案例2   基于match ... case 实现一个简易的计算器,可以实现+ -* /运算,用户输入需要运算的两个数以及运算符之后,就可以进行计算。
num1 = int(input("请输入第一个数："))
num2 = int(input("请输入第二个数："))
fu_hao = input("你想要进行什么计算？请输入计算符号(+-*/):")
match fu_hao:
    case "-":
        print(num1 - num2)
    case "+":
        print(num1 + num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)
    case _:
        print("输入有误！")