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
            for student_name,student_score in student_passage.items():  #遍历字典后将子字典中的分数添加到对应空列表中
                chinise_list.append(student_score["语文"])
                math_list.append(student_score["数学"])
                english_list.append(student_score["英语"])
            #使用函数确定分数最小值并存储
            chinise_list_min=min(chinise_list)
            math_list_min=min(math_list)
            english_list_min=min(english_list)
            # 使用函数确定分数最大值并存储
            chinise_list_max=max(chinise_list)
            math_list_max=max(math_list)
            english_list_max=max(english_list)
            # 使用函数确定分数平均值并存储
            chinise_list_avg=sum(chinise_list)/len(chinise_list)
            math_list_avg=sum(math_list)/len(math_list)
            english_list_avg=sum(english_list)/len(english_list)
            #使用列表推导式加上条件语句快速找到目标学生名
            chinise_min_name =[student_name for student_name,student_score in student_passage.items()  if student_score["语文"] == chinise_list_min]
            math_min_name =[student_name for student_name,student_score in student_passage.items() if student_score["数学"] == math_list_min]
            english_min_name=[student_name for student_name,student_score in student_passage.items() if student_score["英语"] == english_list_min]
            chinise_max_name=[student_name for student_name,student_score in student_passage.items() if student_score["语文"] == chinise_list_max]
            math_max_name = [student_name for student_name,student_score in student_passage.items() if student_score["数学"] == math_list_max]
            english_max_name = [student_name for student_name,student_score in student_passage.items() if student_score["英语"] == english_list_max]
            print(f"班级语文平均分为:{chinise_list_avg},数学平均分为:{math_list_avg},英语平均分为:{english_list_avg}")
            print(f"语文最低分是{chinise_min_name}的{chinise_list_min}数学最低分是{math_min_name}的{math_list_min},英语最低分是{english_min_name}的{english_list_min},\n语文最高分是{chinise_max_name}的{chinise_list_max},数学最低分是{math_max_name}的{math_list_max},英语最高分是{english_max_name}的{english_list_max}")
        case "7":
            break
