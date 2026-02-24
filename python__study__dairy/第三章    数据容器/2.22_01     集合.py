#介绍:集合(set)是一种无序的、不可重复、可修改的数据容器。
# 定义集合
s8 = {"C", "D", "X", "T", "0","U"}
# 定义空集合
s9 = set()   #注意:空集合的定义不可以使用{},{}表示的是空字典;由于集合是无序的,因此是不支持下标索引访问的。




#---------------------------------------------集合常用方法----------------------------------------------
#add( .. )              添加元素到集合中                                             s1.add('t')
#remove( .. )           移除集合中的指定元素(指定元素不存在将报错)                       s1.remove('t')
#pop()                  随机删除集合中的元素并返回                                     e = s1.pop()
#clear ()               清空集合                                                    s1.clear()
#difference()           求取两个集合的差集(包含在第一个集合但不包含在第二个集合的元素)       s1.difference(s2)
#union()                求取两个集合的并集 (所有区域)                                  s1.union(s2)
#intersection()         求取两个集合的交集                                           s1.intersection(s2)

# 常见方法:
# add():添加元素到集合
s1 = {100,200,300,400,500,600,700,800}
print(s1)
s1.add(1200)
print(s1)

# remove():移除集合中的指定元素(指定元素不存在将报错)
s1.remove(200)
print(s1)

# pop():随机删除集合中的元素并返回
e = s1.pop()
print(e)
print(s1)

# clear():清空集合
s1.clear()
print(s1)

# difference():求两个集合的差集(存在于第一个集合,但不存在于第二个集合)
s2 = {"A", "B", "C", "D", "E", "X", "Y"}
s3 = {"C", "E", "Y", "Z"}
print(s2.difference(s3))

# union():求两个集合的并集
print(s2.union(s3))
print(s3.union(s2))

# intersection():求两个集令的交集
print(s2.intersection(s3))
print(s2.intersection(s3))



#--------------------------------------------案例---------------------------------------------
#根据提供的班级学生的选课情况,完成如下需求:
#1. 找出同时选修了法语和艺术的学生
#2. 找出同时选修了所有四门课程的学生
#3. 找出选修了足球,但是没有选修篮球的学生
#4. 统计每一个学生选修的课程数量

# 选修足球学生名单
football_set = {"王林","曾牛","徐立国","遁天","天运子","韩立","厉飞雨","乌丑","紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁","墨居仁","王林","姜老道","曾牛","王蝉","韩立","天运子","李化元","厉飞雨","云露"}
# 选修法语学生名单
french_set= {"许木","王卓","十三","虎咆","姜老道","天运子","红蝶","厉飞雨","韩立","曾牛"}
# 选修艺术学生名单
art_set = {"遁天","天运子","韩立","虎咆","姜老道","紫灵"}

#1. 找出同时选修了法语和艺术的学生
print(french_set.intersection(art_set ))

#2. 找出同时选修了所有四门课程的学生   #交集可用符号 & 表示
s1=french_set.intersection(art_set.intersection(football_set).intersection(basketball_set))
print("同时选修四门课的人有:",s1)

#3. 找出选修了足球,但是没有选修篮球的学生   #差集可用符号 - 表示    并集可用 | 表示
print("选修了足球,但是没有选修篮球的是:",football_set.difference(basketball_set))
###这个需求也可以使用集合推导式完成   fb_set3 = {s for s in football_set if s not in basketball_set}

#4. 统计每一个学生选修的课程数量
all_list=[*football_set,*basketball_set,*art_set,*french_set]    #将集合中的元素解包后用列表承接,因为列表的数据可重复
for i in all_list:
    num=all_list.count(i)
    print(f"{i}总共选修了{num}门课")























