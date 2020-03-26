class Cat:
    def __init__(self, name):
        self.name = name
        print("%s我来了" % self.name)

    def __del__(self):
        print("我走了")

    def __str__(self):
        return "我是小猫【%s】" % self.name


tom = Cat("tom")
print(tom)
