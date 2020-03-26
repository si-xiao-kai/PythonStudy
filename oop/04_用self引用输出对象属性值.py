class Cat:
    def eat(self):
        print("小猫爱吃鱼")
    def drink(self):
        self.printName()
        print("小猫要喝水")
    def printName(self):
        print(self.name)
    def printAddr(self):
        print(self)

tom=Cat()
tom.name="tom"
print(tom)
tom.printAddr()
tom.drink()
# 由哪一个对象调用的方法，方法内的self就是那个对象的引用
kitty=Cat()
kitty.name="kitty"
#tom.printName()
#kitty.printName()


