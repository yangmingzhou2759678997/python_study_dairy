#标识符:程序员为变量、函数、类等元素所起的名字
#规则:
# 1.只能包含字母(大小写)、数字、下划线
# 2.不能数字开头
# 3.不能用关键字（True、False、None、and、or、if、else、elif、for、while等）
# 4. 严格区分大小写


ture=1     #可运行
print(ture)

#True = 1     #无法运行
#print(True)

#变量名命名尽量：1.需要见名知意 2.多部分使用下划线连接 3.英文字母全部小写

#案例：实现变量交换 a=2; b=6 -> a=6; b=2
a=2 ; b=6
c = a
a = b
b = c
print(a,b,c)
