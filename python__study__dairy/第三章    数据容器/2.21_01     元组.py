#介绍:元组是不可变的序列,类似于列表,但创建后不能修改。
#特点:1.可以存储不同类型的元素    2.元素可以重复、有序、不可以修改(支持索引访问、切片)
# 定义元组: t1 = (5, 7, 9, 1, 2, 3, 10, 6, 4, 8 ,12, 7, 5)
# 定义空元组: t2 = ()   t3 = tuple()

# 元组基本操作 - tuple --- >元素可以重复,有序,不可修改
# 定义
t1 = (80, 95, 78, 50, 76, 80, 85, 20)
print(t1)
print(type(t1))
# 索引访问
print(t1[0])
print(t1[-1])
# 切片
print(t1[0:5:1])
# count()统计元索的个数
print(t1.count(80))
# index()获取元素的索引(第一个元素的位置)
print(t1.index(80))
# 注意点:如果定义单元素的元组,单个元素之后需要加上逗号,比如(100,)
t3 = (100,)
print(t3)
print(type(t3))


#--------------------------------------元组的组包与解包--------------------------------------
#组包(Packing):将多个值合并到一个容器(元组、列表)中。
#解包(Unpacking):将容器(元组、列表)解开成独立的元素,分别赋值给多个变量。
# 定义元组,组包
t1 = (5, 7, 9, 1)
# 定义元组,组包
t2 = 5, 7, 9, 1
# 基础解包
a, b, c, d = t1
# (*)扩展解包

s, *o = t2    # s为5,o为[7,9,1]
*O,e= t2      # o为[5,7,9],e为1
x,*y,z =t2    # x为5,y为[7,9],z为1

#示例
# 组包操作
t1 = (5, 7, 9, 10, 2, 23, 12)
t2 = 5, 7, 9, 10, 2, 23, 12
print(t1)
print(t2)

# 解包操作
# 基础解包(变量数量与容器的元素个数一致)
a,b,c,d,e,f,g = t1
print(a,b,c,d,e,f,g)

#* 扩展解包(*收集剩余的所有元素,封装列表list中)
first, second, *other, last = t1
print(first,second)
print(other)
print(last)

*other, last2,last1 = t1
print(other)
print(last2)
print(last1)


#--------------------------------案例需求-----------------------------
# 案例1:现有两个变量,分别为:a= 10,b=20,现需要将这两个变量值交换,然后输出到控制台。
a = 10
b = 20
s_n=[a,b]
b,a=s_n
print("a的新值为:",a,"\t""b的新值为:",b)



# 案例2:现有三个变量,分别为:a=100,b=200,c=300,现而要将这三个变量值进行交换,将a,b,c的值分别赋值给c,a,b,并将其输出到控制台。
a=100
b=200
c=300
sn=[a,b,c]
c,a,b=sn
print(a,b,c)


#案例3:根据提供的学生成绩单,完成如下需求:
#1. 计算每个学生的总分、各科平均分,然后一并输出出来。
#2. 统计各科成绩的最低分、最高分、平均分,并输出。
#3. 查找成绩优秀(平均分大于90)的学生,并输出。

students=(
    ("s001","王林",85,92,78),
    ("s002","李慕婉",92,88,95),
    ("s003","十三",78,85,82),
    ("s004","曾牛",88,79,91),
    ("s005","周怡",95,96,89),
    ("s006","王卓",76,82,77),
    ("s007","红蝶",89,91,94),
    ("s008","徐立国",75,69,82),
    ("s009","许木",86,89,98),
    ("s010","遁天",66,59,72)
)

# 方式一: 1. 计算每个学生的总分、各科平均分,然后一并输出出来。--- >{avg :. 1f} --- >保留1位小数 .
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
for s in students: # ("S001", "EM", 85, 92, 78)
    total= s[2] + s[3] + s[4]
    avg = total / 3
    print(f"{s[0]} \t {s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {total} \t {avg:.1f}")

# 1.方式二:(采用解包的方式去做,将s直接解包,后续代码更加直观)
#for id, name, chinese, math, english in students:
#    total = chinese + math + english
#    avg = total / 3
#    print(f"{id} \t {name} \t {chinese} \t {math} \t {english} \t {total} \t {avg :. 1f}")

# 2. 统计各科成绩的最低分、最高分、平均分,并输出。
# 2.1 获取到各科的成绩列表
chinese_scores = [s[2] for s in students]   #列表推导式
math_scores = [s[3] for s in students]
english_scores = [s[4] for s in students]

# 2.2 统计各科成绩的最低分、最高分、平均分,并输出。
print(f"语文最低分:{min(chinese_scores)},最高分:{max(chinese_scores)},平均分:{sum(chinese_scores)/len(chinese_scores)}")
print(f"数学最低分:{min(math_scores)},最高分:{max(math_scores)},平均分:{sum(math_scores)/len(math_scores)}")
print(f"英语最低分:{min(english_scores)},最高分:{max(english_scores)},平均分:{sum(english_scores)/len(english_scores)}")

# 3. 查找成绩优秀(平均分大于90)的学生,并输出。
print("优秀学生(平均分>90)名单如下:")
for s in students:                  #同理,此处也可进行解包操作
    total = s[2] + s[3] + s[4]
    avg = total / 3
    if avg > 90:# 优秀学生
        print(f"学号:{s[0]},姓名:{s[1]},平均分:{avg:.1f}")