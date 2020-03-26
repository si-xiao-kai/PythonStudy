class Cat:
    def eat(self):
        print("小猫爱吃鱼")
    def drink(self):
        print("小猫要喝水")


tom=Cat()
tom.eat()
addr=id(tom)
print("tom的十进制地址%d"%addr)
print("tom的十六进制地址%x"%addr)
print("直接打印接受对象的变量：")
print(tom)