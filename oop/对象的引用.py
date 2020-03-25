class Cat:
    def eat(self):
        print("小猫吃鱼")
    def drink(self):
        print("小猫喝水")
def main():
    tom=Cat()
    print("print函数直接输出接受对象的变量：")
    print(tom)
    addr=id(tom)
    print("通过id函数获得十进制形式的引用地址：%d" % addr)
    print("通过id函数获得十六进制形式的引用地址：%x" % addr)



if __name__ == "__main__":
    main()
