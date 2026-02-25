#-------------------------------------------数据容器总结与对比--------------------------------------------------

#特性         字符串(str)       列表(list)         元组(tuple)        集合(set)           字典(dict)
#有序性       有序              有序               有序              无序                 有序(3.7+)
#重复元素      允许               允许              允许              不允许                key不允许
#可变性       不可变              可变              不可变             可变                 可变
#索引访问      支持               支持              支持              不支持                不支持
#切片操作      支持               支持              支持              不支持                不支持
#使用场景      文本处理            有序可重复数据集合   固定数据记录       去重数据集合           键值对



#----------------------------------------------综合案例实操--------------------------------------------------
#   开发一个教务管理系统,在该系统中可以维护和管理学员的成绩信息,具体需求如下:
#1. 添加学生信息:根据提示录入学生姓名、语文、数学、英语成绩,录入完成保存到系统中。
#2. 修改学生信息:要求输入要修改的学生姓名,然后再提示输入语文、数学、英语成绩,输入完成后修改学员信息。
#3. 删除学生信息:要求输入要删除的学生姓名,根据姓名删除学生信息。
#4. 查询学生信息:要求输入要查询的学生姓名,根据姓名查询学生信息并输出。
#5. 列出所有学生:遍历所有学生信息并输出。
#6. 统计班级成绩:统计班级语文、数学、英语成绩的最高分、最低分、平均分,以及语文、数学、英语最高分和最低分的学员姓名。
#7. 退出系统。
student_passage={}
while True:
    print("你想要使用那一个功能? 1.添加学生信息,2.修改学生信息,3.删除学生信息,4.查询学生信息,5.列出所有学生,6.统计班级成绩,7.退出系统")
    menu=input("请输入:")
    match menu:
        case "1":
            student_name=input("请输入你要添加的学生姓名:")
            if student_name not in student_passage:
                student_passage[student_name]={"语文":int(input("语文成绩是:")),"数学":int(input("数学成绩是:")),"英语":int(input("英语成绩是:"))}
            else:
                print("系统已录入该学生信息,使用功能2可进行修改")
        case "2":
            student_name = input("请输入你要修改的学生姓名:")
            if  student_name in student_passage:
                student_passage[student_name] = {"语文": int(input("语文成绩修改为:")), "数学": int(input("数学成绩修改为:")),"英语": int(input("英语成绩修改为:"))}
            else:
                print("系统未录入该学生信息,使用功能1可进行添加")
        case "3":
            student_name = input("请输入你要删除的学生姓名:")
            if student_name not in student_passage:
                print("系统未录入该学生信息!")
            else:
                del student_passage[student_name]
        case "4":
            student_name = input("请输入你要查询的学生姓名:")
            if student_name not in student_passage:
                print("系统未录入该学生信息,使用功能1可进行添加")
            else:
                student_score = student_passage[student_name]
                print(f"{student_name}的语文成绩为:{student_score["语文"]},数学成绩为:{student_score["数学"]},英语成绩为:{student_score["英语"]}")
        case "5":
            for student_name in student_passage.keys():
                student_score = student_passage[student_name]
                print(f"{student_name}的语文成绩为:{student_score["语文"]},数学成绩为:{student_score["数学"]},英语成绩为:{student_score["英语"]}")
        case "6":
            english_list=[]
            math_list=[]
            chinise_list=[]
            chinise_min_name=[]
            math_min_name=[]
            english_min_name=[]
            chinise_max_name=[]
            math_max_name=[]
            english_max_name=[]
            student_score={}
            for student_name in student_passage.keys():
                student_score = student_passage[student_name]
                chinise_list.append(student_score["语文"])
                math_list.append(student_score["数学"])
                english_list.append(student_score["英语"])
            chinise_list_min=min(chinise_list)
            math_list_min=min(math_list)
            english_list_min=min(english_list)
            chinise_list_max=max(chinise_list)
            math_list_max=max(math_list)
            english_list_max=max(english_list)
            chinise_list_avg=sum(chinise_list)/len(chinise_list)
            math_list_avg=sum(math_list)/len(math_list)
            english_list_avg=sum(english_list)/len(english_list)
           # for student_name in student_passage.keys():
                #student_score = student_passage[student_name]
            chinise_min_name =[student_name for student_name in student_passage.keys()  if student_score["语文"] == chinise_list_min]
            math_min_name =[student_name for student_name in student_passage.keys() if student_score["数学"] == math_list_min]
            english_min_name=[student_name for student_name in student_passage.keys() if student_score["英语"] == english_list_min]
            chinise_max_name=[student_name for student_name in student_passage.keys() if student_score["语文"] == chinise_list_max]
            math_max_name = [student_name for student_name in student_passage.keys() if student_score["数学"] == math_list_max]
            english_max_name = [student_name for student_name in student_passage.keys() if student_score["英语"] == english_list_max]
            print(f"班级语文平均分为:{chinise_list_avg},数学平均分为:{math_list_avg},英语平均分为:{english_list_avg}")
            print(f"语文最低分是{chinise_min_name}的{chinise_list_min}数学最低分是{math_min_name}的{math_list_min},英语最低分是{english_min_name}的{english_list_min},\n语文最高分是{chinise_max_name}的{chinise_list_max},数学最低分是{math_max_name}的{math_list_max},英语最高分是{english_max_name}的{english_list_max}")
        case "7":
            break



"""
    案例:
    开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
        1. 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
        2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
        3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
        4. 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
        5. 列出所有学生：遍历所有学生信息并输出。
        6. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
        7. 退出系统。



# # # # # # # # # # # # # # # # # # # # # # # # # # 【菜单】 # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  1. 添加学生信息   2. 修改学生信息   3. 删除学生信息   4. 查询学生信息   5. 列出所有学生   6. 统计班级成绩   7. 退出系统       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

print("欢迎使用教务管理系统 ~")

student_scores = {}

while True:
    # 1. 制作菜单
    print(menu)

    # 2. 执行的具体操作
    choice = input("请选择要执行的操作(1-7): ")
    match choice:
        case "1":  # 添加学生信息
            student_name = input("请输入学生姓名: ")
            chinese_score = float(input("请输入语文成绩: "))
            math_score = float(input("请输入数学成绩: "))
            english_score = float(input("请输入英语成绩: "))

            # 如果学生存在, 则不执行添加, 提示信息
            if student_name in student_scores:
                print("该学生已存在, 请重新选择 ~")
            else:
                student_scores[student_name] = {"chinese": chinese_score, "math": math_score, "english": english_score}
                print("学生信息添加完毕 ~")
        case "2":  # 修改学生信息
            student_name = input("请输入要修改的学生姓名: ")
            # 如果学生不存在, 则提示错误信息, 重新选择
            if student_name not in student_scores:
                print("该学生不存在, 请重新选择 ~")
                continue

            chinese_score = float(input("请输入语文成绩: "))
            math_score = float(input("请输入数学成绩: "))
            english_score = float(input("请输入英语成绩: "))
            student_scores[student_name] = {"chinese": chinese_score, "math": math_score, "english": english_score}
            print("学生信息修改完毕 ~")
        case "3":  # 删除学生信息
            student_name = input("请输入要删除的学生姓名: ")

            # 如果学生不存在, 则提示错误信息, 重新选择
            if student_name not in student_scores:
                print("该学生不存在, 请重新选择 ~")
            else:
                del student_scores[student_name]
                print("学生信息删除完毕 ~")
        case "4":  # 查询学生信息
            student_name = input("请输入要查询的学生姓名: ")

            # 如果学生不存在, 则提示错误信息
            if student_name not in student_scores:
                print("该学生不存在, 请重新选择 ~")
            else:
                student_info = student_scores[student_name]
                print(f"学生姓名: {student_name}, 语文成绩: {student_info['chinese']}, 数学成绩: {student_info['math']}, 英语成绩: {student_info['english']}")
        case "5":  # 列出所有学生
            for student_name in student_scores.keys():
                student_info = student_scores[student_name]
                print(f"学生姓名: {student_name}, 语文成绩: {student_info['chinese']}, 数学成绩: {student_info['math']}, 英语成绩: {student_info['english']}")
        case "6":  # 统计班级成绩
            if not student_scores:
                print("系统中暂无学生信息，请先添加学生 ~")
                continue

            # 初始化统计变量
            chinese_scores = []
            math_scores = []
            english_scores = []

            # 收集所有成绩
            for student_name, scores in student_scores.items():
                chinese_scores.append(scores['chinese'])
                math_scores.append(scores['math'])
                english_scores.append(scores['english'])

            # 计算最高分、最低分、平均分
            chinese_max = max(chinese_scores)
            chinese_min = min(chinese_scores)
            chinese_avg = sum(chinese_scores) / len(chinese_scores)

            math_max = max(math_scores)
            math_min = min(math_scores)
            math_avg = sum(math_scores) / len(math_scores)

            english_max = max(english_scores)
            english_min = min(english_scores)
            english_avg = sum(english_scores) / len(english_scores)

            # 找出最高分和最低分的学生
            chinese_max_students = [name for name, scores in student_scores.items() if scores['chinese'] == chinese_max]
            chinese_min_students = [name for name, scores in student_scores.items() if scores['chinese'] == chinese_min]

            math_max_students = [name for name, scores in student_scores.items() if scores['math'] == math_max]
            math_min_students = [name for name, scores in student_scores.items() if scores['math'] == math_min]

            english_max_students = [name for name, scores in student_scores.items() if scores['english'] == english_max]
            english_min_students = [name for name, scores in student_scores.items() if scores['english'] == english_min]

            # 输出统计结果
            print("===== 班级成绩统计 =====")
            print(f"语文 - 最高分: {chinese_max}, 最低分: {chinese_min}, 平均分: {chinese_avg:.2f}")
            print(f"     最高分学生: {chinese_max_students}")
            print(f"     最低分学生: {chinese_min_students}")

            print(f"数学 - 最高分: {math_max}, 最低分: {math_min}, 平均分: {math_avg:.2f}")
            print(f"     最高分学生: {math_max_students}")
            print(f"     最低分学生: {math_min_students}")

            print(f"英语 - 最高分: {english_max}, 最低分: {english_min}, 平均分: {english_avg:.2f}")
            print(f"     最高分学生: {english_max_students}")
            print(f"     最低分学生: {english_min_students}")
            print("========================")
        case "7":  # 退出系统
            print("Bye ~")
            break
        case _:  # 匹配其他所有情况
            print("非法操作, 不支持!!!")
'''"""