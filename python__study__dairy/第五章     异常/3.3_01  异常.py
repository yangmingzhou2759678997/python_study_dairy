#  异常:即便 Python 程序的语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常。

#-----------------------------------异常处理---------------------------------------
#-------------------------------------try/except类型----------------------------------
# 一. 异常捕捉------->异常捕捉可以使用 try/except 语句。

#语法为:  try:
#        {执行代码}
#    except:
#        {发生异常时执行的代码}

#语法示例:
'''
while True:
    try:
        #被监控的可能引发异常的语句块
        break
    except BaseException as e:
        #异常处理语句块,即产生异常要怎么办
'''

#这个过程中,语句按照如下方式工作;
#1.try块包含着可能引发异常的代码,except块则用来捕捉和处理发生的异常。
#2.执行的时候,如果try 块中没有引发异常,则跳过except 块继续执行后续代码;
#3.执行的时候,如果try 块中发生了异常,则跳过try 块中的后续代码,跳到相应的except块中处理异常;异常处理完后,继续执行后续代码
#代码验证:# 测试简单的0不能做除数异常
try:
    print("step1")
    a = 3/0
    print("step2")
except BaseException as e:
    print("step3")
    print(e)
print("step4")  #---->如果出现异常会打印1,3,异常原因,4;如果不出现异常则会打印1,2,4(上述异常执行过程实例)
## 处理程序将只针对对应的try子句中的异常进行处理,而不是其他的try的处理程序中的异常。



#----------------------------------try/多个except类型--------------------------------
#注意:一个try语句可能包含多个except子句,分别来处理不同的特定的异常。最多只有一个分支会被执行。
#之前的结构可以捕获所有的异常,工作中也很常见。但是,从经典理论考虑,一般建议尽量
#捕获可能出现的多个异常(按照先子类后父类的顺序),并且针对性的写出异常处理代码。为了避免遗漏可能出现的异常,可以在最后增加BaseException。
#结构如下:
try:
    a= input("请输入被除数:")
    b=input("请输入除数:")
    c = float(a) / float(b)
    print("结果是:",c)
except ZeroDivisionError: #except 最好是从尽可能小的错误方面然后逐渐扩大错误所述范围(即错误从精确到范围逐渐扩大,错误变得逐渐模糊)
    print("除数不能为0")
except ValueError:
    print("请输入数字")
except BaseException as e:
    print("出错了,错误是:",e)



#-------------------------------try/except/else类型----------------------------
try:
    a = input("Enter a number: ")
    b = input ("Enter b number: ")
    c = float(a) / float(b)
except ZeroDivisionError:
    print("除数不能为零")
else: #------->没有异常才会执行
    print("结果是:",c)



#-------------------------------try/except/else类型----------------------------
#try ... except ... finally结构中,finally 块无论是否发生异常都会被执行,通常用来释放 try 块中申请的资源
#例1:
try:
    a = input("Enter a number: ")
    b = input("Enter b number: ")
    c = float(a) / float(b)
except ZeroDivisionError:
    print("除数不能为零")
except BaseException as e:
    print("发生了其他异常",e)
else:
    print("计算结果是:",c)
finally:
    print("不管是否发生异常,都会执行")
print("程序继续执行")
#例2:
try:
    f = open("E:/a.txt","r")#打开文件
    content = f.readline()#读取文件内容
except FileNotFoundError:
    print("文件不存在")
except IOError:
    print("读写文件异常")
except BaseException as e:
    print("未知异常%s"%e)
else:
    print("读取文件内容:",content)
finally:
    f.close()    #不管文件相关操作有没有成功,最后都关闭文件释放内存
    print("文件关闭")

print("程序运行结束")



#-------------------------------自定义异常类型----------------------------
#程序开发中,有时候我们也需要自己定义异常类。自定义异常类一般都是运行时异常,通常继承Exception或其子类即可。命名一般以Error、Exception为后缀
#例1:
class InvalidEmailError(ValueError):
    '''自定义邮箱格式异常'''
def _init_(self, email) :
    super()._init_(f"无效邮箱格式:{email}")
    self.email = email
# 使用示例
email = "iwen@iwenwiki.com"
if "@" not in email or "." not in email.split("@") [1]:
    raise InvalidEmailError(email)        #---->自定义异常一般使用raise抛出

#例2:
x = 10
if x > 5:
    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))

#运行报错: Exception: x 不能大于 5。x 的值为: 10







