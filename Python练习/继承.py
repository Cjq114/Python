Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class parent:
	def hello(self):
		print('正在调用父类的方法...')

		
>>> class Child(parent):
	pass

>>> P = parent()
>>> p.hello()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    p.hello()
NameError: name 'p' is not defined
>>> P.hello()
正在调用父类的方法...
>>> c = Child()
>>> c.hello()
正在调用父类的方法...
>>> class Child(parent):
	def hello(self):
		print('正在调用子类的方法...')

		
>>> c = Child()
>>> c.hello()
正在调用子类的方法...
>>> P.hello()
正在调用父类的方法...
>>> 
======================== RESTART: D:/Python/日常练习/鱼.py ========================
>>> fish = Fish()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    fish = Fish()
  File "D:/Python/日常练习/鱼.py", line 5, in __init__
    self.x = r.random(0,10)
TypeError: random() takes no arguments (2 given)
>>> 
======================== RESTART: D:/Python/日常练习/鱼.py ========================
>>> fish = Fish()
>>> fish.move()
我的位置： 6 4
>>> fish.move()
我的位置： 5 4
>>> goldfish = Goldfish()
>>> goldfish.move()
我的位置： 5 9
>>> shark = Shrak()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    shark = Shrak()
NameError: name 'Shrak' is not defined
>>> shark = Shark()
>>> shark.hungry()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    shark.hungry()
TypeError: 'bool' object is not callable
>>> 
======================== RESTART: D:/Python/日常练习/鱼.py ========================
>>> shark = Shark()
>>> shark.move()
我的位置： 4 10
>>> shark.eat()
吃货的梦想就是天天有的吃
>>> shark.eat()
太撑了，吃不下了！
>>> shark.move()
我的位置： 3 10
>>> 
>>> 
>>> class Base1:
	def fool(self):
		print('1')

		
>>> class Base2:
	def fool2(self):
		print('2')

		
>>> class C(Base1, Base2):
	pass

>>> c = C()
>>> c.fool()
1
>>> c.fool2()
2
>>> 
