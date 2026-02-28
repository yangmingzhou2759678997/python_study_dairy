#需求
#1. 定义一个函数:根据传入的底和高计算三角形面积的函数(三角形面积=底*高/2)。
#2. 定义一个函数:计算传入的字符串中元音字母的个数(元音字母为 aeiouAEIOU)。
#3. 定义一个函数:计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数),并返回。


#1.
def san_jiao_area (di,gao):
    area=di * gao/2
    return area
di=int(input("请依次输入三角形的底:"))
gao=int(input("请依次输入三角形的高:"))
print("该三角形面积为：",san_jiao_area(di,gao))



#2.
str_= input("请输入一条字符串：")
def yuan_yin_num(str_):
    num = 0
    for s in str_:
        if s in "aeiouAEIOU":
            num+=1
    return num
print(f"{str_}这条字符串有{yuan_yin_num(str_)}个元音字母")



#3.
grade_list=[]
while True:
    grade=int(input("请输入成绩：(成绩必须为数字，如果记录完毕则输入-1并确定即可退出)"))
    if  grade != -1:
        grade_list.append(grade)
    else:
        print("记录完毕，退出记录")
        break
print(grade_list)
def grade_xi_tong(list):
    max_grade = max(list)
    min_grade = min(list)
    avg_grade = float(sum(list) / len(list))
    return max_grade, min_grade, avg_grade
print(f"您记录后的成绩单中最高分、最低分、平均分分别为：{grade_xi_tong(grade_list)}")




