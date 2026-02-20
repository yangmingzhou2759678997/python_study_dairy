 #while语法结构
#   while 条件表达式:
#       循环体语句1
#       循环体语句2


#案例  实现从1——100之间所有偶数的求和
m,n,j=0,1,2

while 1<=j<=98:
    j=n*2
    m=m+j
    n+=1
else:
    print(m,j,n)






#for循环结构    for循环,本质是一种轮询遍历机制,对一批内容进行逐个处理
#   for 元素 in 待处理数据集:
#       循环体代码(对元素进行处理)
#   else:
#       循环结束时,执行的代码

#案例1   # 案例1:计算 1-100 之间所有的奇数之和
# 注：以下两个案例中需要使用到range获取数据集，用法如下:
# 1.range(start,end)->获取一个从start开始,到end结束的数字序列(不含end本身)
#   range(2,8)获取的数据就是2,3,4,5,6,7
# 2.range(start,end,step)->获取一个从start开始,到end结束的数字序列,step步长(不含end本身)
# ·range(0,102)获取的数据就是0,2,4,6,8
total =0
for i in range(1, 101):
    if i % 2 == 1:# 奇数
        total += i
print("1-100之间的奇数累加之和:",total)


# 案例2:计算 100-500 之间所有3的倍数的数字之和
total =0 #记录累加之和
for i in range(100, 501):
    if i %3 == 0:# i是3的倍数
        total += i
print("100-500 之间所有3的倍数的数字之和:",total)



#嵌套循环(外部循环1次，内部循环n次)
#for 元素 in 待处理数据集1:
#   循环体的代码1
#   循环体的代码2
#   for 元素 in 待处理数据集2:
#       循环体的代码1
#       循环体的代码2

#案例3    循环嵌套:根据输入的长方形的长度 m,宽度 n,打印一个长方形;
#   如下:是一个长度为10,宽度为5 的长方形
#    *  *  *  *  *  *  *  *  *  *
#    *  *  *  *  *  *  *  *  *  *
#    *  *  *  *  *  *  *  *  *  *
#    *  *  *  *  *  *  *  *  *  *
#    *  *  *  *  *  *  *  *  *  *

m= int(input("请输入长方形的长度:"))
n= int(input("请输入长方形的宽度:"))
for j in range(n): #控制行
    for i in range(m):  #控制列
        print("*", end=" ")
    print()


#案例4    打印九九乘法表
#使用for循环实现
for i in range(1,10):
    for j in range(i,10):
        print(f"{i}*{j}={i*j}",end="\t")
    print()


#使用while循环实现
m,n=1,1
while m<=9:
    while n<=9:
        print(f"{m}*{n}={m*n}",end="\t")
        n+=1
    m+=1
    n=m
    print()
