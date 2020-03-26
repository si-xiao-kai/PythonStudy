class Cat:
    def __init__(self, name):
        self.name = name
        print("%s我来了" % self.name)

    def __del__(self):
        print("我走了")


tom = Cat("tom")
del tom
print("*"*50)
