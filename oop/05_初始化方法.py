class Person:
    def __init__(self, name):
        print("初始化方法__init__在创建对象时会被自动调用")
        self.name = name

    def eat(self):
        print("%s吃鱼" % self.name)


kai = Person("kai")
tom = Person("tom")
kai.eat()
tom.eat()
print(kai.name)
