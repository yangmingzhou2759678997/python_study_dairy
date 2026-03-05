#需求:采用面向对象的编程思想,完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息,通过控制台菜单与用户交互,具体的功能如下:
#1. 添加学生成绩:根据输入的学生姓名、语文成绩、数学成绩、英语成绩,记录在系统中
#2. 修改学生成绩:根据输入的学生姓名,修改对应的学生成绩
#3. 删除学生成绩:根据输入的学生姓名,删除对应的学生成绩
#4. 查询指定学生成绩:根据输入的学生姓名,查找对应的学生成绩,并输出
#5. 展示全部学生成绩:展示出系统中所有学生的成绩
'''
class Grade:
    def __init__(self):
        self.dict_grade = {}
    def add_grade(self):
        name = input("请输入你要添加的学生姓名:")
        c_grade = int(input("请输入该学生语文成绩:"))
        m_grade = int(input("请输入该学生数学成绩:"))
        e_grade = int(input("请输入该学生英语成绩:"))
        self.dict_grade[name]=[c_grade,m_grade,e_grade]
        print("添加成功!")
    def modify_grade(self):
        name = input("请输入你要修改的学生姓名:")
        c_grade = int(input("请输入该学生新的语文成绩:"))
        m_grade = int(input("请输入该学生新的数学成绩:"))
        e_grade = int(input("请输入该学生新的英语成绩:"))
        self.dict_grade[name]=[c_grade,m_grade,e_grade]
        print("修改成功!")
    def del_grade(self):
        name = input("请输入你要删除的学生姓名:")
        del self.dict_grade[name]
        print("删除成功!")
    def query_grade(self):
        name=input("请输入你要查询的学生姓名:")
        print(self.dict_grade[name])
    def show_grade(self):
        print(f"所有学生成绩记录如下:")
        for name in self.dict_grade.keys():
#   print(self.dict_grade.)
            print(f"{name}的语文{self.dict_grade[name][0]},数学{self.dict_grade[name][1]},英语{self.dict_grade[name][2]}")

s1 = Grade()
while True:
    choice1=int(input("请输入你要执行的功能:1.添加 2.修改 3.删除 4.查询 5.展示所有 6.退出系统"))
    match choice1:
        case 1:
            s1.add_grade()
        case 2:
            s1.modify_grade()
        case 3:
            s1.del_grade()
        case 4:
            s1.query_grade()
        case 5:
            s1.show_grade()
        case 6:
            break
'''


# 改进版:
class grade:
    def __init__(self):
        # 修正：初始化时不需要传入具体学生信息，只需初始化存储容器
        self.dict_grade = {}

    def add_grade(self):
        name = input("请输入你要添加的学生姓名:")
        c_grade = int(input("请输入该学生语文成绩:"))
        m_grade = int(input("请输入该学生数学成绩:"))
        e_grade = int(input("请输入该学生英语成绩:"))
        # 将信息存入字典
        self.dict_grade[name] = [c_grade, m_grade, e_grade]
        print("添加成功!")

    def modify_grade(self):
        name = input("请输入你要修改的学生姓名:")
        if name in self.dict_grade:
            c_grade = int(input("请输入该学生新的语文成绩:"))
            m_grade = int(input("请输入该学生新的数学成绩:"))
            e_grade = int(input("请输入该学生新的英语成绩:"))
            self.dict_grade[name] = [c_grade, m_grade, e_grade]
            print("修改成功!")
        else:
            print("未找到该学生信息，无法修改。")

    def del_grade(self):
        name = input("请输入你要删除的学生姓名:")
        if name in self.dict_grade:
            del self.dict_grade[name]
            print("删除成功!")
        else:
            print("未找到该学生，删除失败。")

    def query_grade(self):
        name = input("请输入你要查询的学生姓名:")
        if name in self.dict_grade:
            scores = self.dict_grade[name]
            print(f"学生 {name} 的成绩为：语文:{scores[0]}, 数学:{scores[1]}, 英语:{scores[2]}")
        else:
            print("未找到该学生信息。")

    def show_grade(self):
        print("所有学生成绩记录如下:")
        # 修正：遍历字典的键值对，逐个打印
        if not self.dict_grade:
            print("系统内暂无成绩记录。")
        else:
            for name, scores in self.dict_grade.items():
                print(f"姓名:{name} -> 语文:{scores[0]}, 数学:{scores[1]}, 英语:{scores[2]}")

# --- 逻辑控制部分 ---
# 1. 必须先实例化一个对象！
student_system = grade() 

while True:
    choice1 = input("请输入你要执行的功能: 1.添加 2.修改 3.删除 4.查询 5.展示所有 6.退出系统\n")
    
    match choice1:
        case '1':
            # 使用实例对象调用方法
            student_system.add_grade()
        case '2':
            student_system.modify_grade()
        case '3':
            student_system.del_grade()
        case '4':
            student_system.query_grade()
        case '5':
            student_system.show_grade()
        case '6':
            print("退出系统，再见！")
            break
        case _:
            print("输入有误，请重新输入。")



