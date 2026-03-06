#需求:
#采用面向对象的编程思想,开发一个购物车管理系统,实现商品信息的添加、修改、删除、查询功能。系统使用自定义对象存储商品数据,通过控制台菜单与用户交互。具体功能如下:
#1. 添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量,保存该商品信息到购物车。
#2. 修改购物车:要求用户输入要修改的购物车商品名称,然后再提示输入该商品的价格、数量,输入完成后修改该商品信息。
#3. 删除购物车:要求用户输入要删除的购物车名称,根据名称删除购物车中的商品。
#4. 查询购物车:将购物车中的商品信息展示出来,格式为:“商品名称:xxx,商品价格:xxx,商品数量:xxx"。
'''
class Shopping_Cart:
    def __init__(self):
        self.cart_dict = {}
    def add_shopping_cart(self):
        name=input("请输入你要添加的商品名:")
        if name in self.cart_dict.keys():
            print("购物车中已有该商品,添加失败!返回至菜单")
            return
        else:
            price = int(input("请输入商品价格:"))
            num = int(input("请输入商品数量:"))
            self.cart_dict[name] = {"价格":price,"数量":num}
            print("添加完毕")
    def modify_shopping_cart(self):
        name=input("请输入你要修改的商品名:")
        if name not in self.cart_dict.keys():
            print("购物车中无该商品,返回至菜单")
            return
        else:
            price = int(input("请输入修改后的商品价格:"))
            num = int(input("请输入修改后的商品数量:"))
            self.cart_dict[name] = {"价格": price, "数量": num}
            print("修改完毕")
    def delete_shopping_cart(self):
        name = input("请输入你要删除的商品名:")
        if name not in self.cart_dict.keys():
            print("购物车中没有该商品,删除失败!返回至菜单")
            return
        else:
            del self.cart_dict[name]
    def show_shopping_cart(self):
        print("购物车所有商品及信息如下:")
        for name in self.cart_dict.keys():
            print(f"商品名称:{name}  商品价格:{self.cart_dict[name]["价格"]}  商品数量:{self.cart_dict[name]["数量"]}")

shopping_test = Shopping_Cart()
while True:
    choice1 =input("请输入你想进行的操作:1.添加商品 2.修改商品 3.删除商品 4.查询商品 5.退出系统")
    match choice1:
        case "1":
            shopping_test.add_shopping_cart()
        case "2":
            shopping_test.modify_shopping_cart()
        case "3":
            shopping_test.delete_shopping_cart()
        case "4":
            shopping_test.show_shopping_cart()
        case "5":
            break
'''
#完全面向对象(改进版)

# 1. 商品实体类：只负责定义“商品是什么”
class Product:
    def __init__(self, name, price, num):
        self.name = name
        self.price = price
        self.num = num


# 2. 购物车管理类：只负责“逻辑怎么做”，不包含任何 input()
class Shopping_Cart:
    def __init__(self):
        # 存储结构：{商品名: Product对象}
        self.cart_dict = {}

    def add_product(self, product_obj):
        """添加商品逻辑"""
        if product_obj.name in self.cart_dict:
            return False  # 返回失败信号，由外部决定打印什么
        self.cart_dict[product_obj.name] = product_obj
        return True

    def modify_product(self, name, new_price, new_num):
        """修改商品逻辑"""
        if name not in self.cart_dict:
            return False
        # 直接修改对象属性
        product_1 = self.cart_dict[name]
        product_1.price = new_price
        product_1.num = new_num
        return True

    def delete_product(self, name):
        """删除商品逻辑"""
        if name in self.cart_dict:
            del self.cart_dict[name]
            return True
        return False

    def get_all_products(self):
        """获取数据逻辑"""
        return self.cart_dict.values()


# --- 3. 交互控制层：负责 input() 和 print() ---
# 这样即便以后要改成网页版，只需要换掉这部分代码，上面的类完全不用动
def main():
    cart_engine = Shopping_Cart()

    while True:
        print("\n" + "=" * 20)
        choice = input("操作: 1.添加 2.修改 3.删除 4.查询 5.退出\n选择：")

        match choice:
            case "1":
                name = input("商品名称:")
                price = int(input("单价:"))
                num = int(input("数量:"))
                # 先造出一个“商品对象”，再塞进“购物车”
                new_item = Product(name, price, num)
                if cart_engine.add_product(new_item):
                    print(" 添加成功")
                else:
                    print(" 错误：商品已存在")

            case "2":
                name = input("要修改的商品名:")
                price = int(input("新单价:"))
                num = int(input("新数量:"))
                if cart_engine.modify_product(name, price, num):
                    print(" 修改成功")
                else:
                    print(" 错误：商品不存在")

            case "3":
                name = input("要删除的商品名:")
                if cart_engine.delete_product(name):
                    print(" 已移除")
                else:
                    print(" 错误：商品不存在")

            case "4":
                print("--- 购物车清单 ---")
                items = cart_engine.get_all_products()
                if not items:
                    print("空空如也")
                for item in items:
                    print(f"商品:{item.name} | 价格:{item.price} | 数量:{item.num}")

            case "5":
                print("退出系统...")
                break


if __name__ == "__main__":
    main()
