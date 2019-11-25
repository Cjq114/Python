import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        self.x -= 1
        print('我的位置：', self.x, self.y)

class Goldfish(Fish):
    pass

class Carp(Fish):w
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        Fish.__init__(self)  #调用父类的方法 （未绑定的父类方法）
        #或者为 super().__init__()
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('吃货的梦想就是天天有的吃')
            self.hungry = False

        else:
            print('太撑了，吃不下了！')
            
        
