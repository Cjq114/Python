Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Ball:
	def setname(elf,name):
		self.name = name

		
>>> class Ball:
	def setname(elf,name):
		self.name = name
	def kick(self):
		print('我叫%s，该死的，谁踢我...' % self.name)

		
>>> a = Ball()
>>> a.setname('球A')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.setname('球A')
  File "<pyshell#7>", line 3, in setname
    self.name = name
NameError: name 'self' is not defined
>>> class Ball:
	def setname(self,name):
		self.name = name
	def kick(self):
		print('我叫%s，该死的，谁踢我...' % self.name)

		
>>> a = Ball()
>>> a.setname('球A')
>>> b.setname('球B')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    b.setname('球B')
NameError: name 'b' is not defined
>>> b = Ball()
>>> b.setname('球B')
>>> c = Ball()
>>> c.setname('土豆')
>>> a.kick
<bound method Ball.kick of <__main__.Ball object at 0x000000762B2187F0>>
>>> a.kick()
我叫球A，该死的，谁踢我...
>>> c.kick()
我叫土豆，该死的，谁踢我...
>>> 
>>> 
>>> class Ball:
	def __init__(self,name):
		self.name = name
	def kick(self):
		print('我叫%s，该死的，谁踢我...' % self.name)

		
>>> b = Ball('土豆'）
	     
SyntaxError: invalid character in identifier
>>> b = Ball('土豆')
	     
>>> b.kick()
	     
我叫土豆，该死的，谁踢我...
>>> b = Ball()
	     
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    b = Ball()
TypeError: __init__() missing 1 required positional argument: 'name'
>>> #必须要有一个初始的参数
	     
>>> class Person:
	     name = '小甲鱼'

	     
>>> p = Person()
	     
>>> p.name()
	     
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    p.name()
TypeError: 'str' object is not callable
>>> p.name
	     
'小甲鱼'
>>> #name 不是函数，不需要加（）
	     
>>> class Person:
	 __name = '小甲鱼'

	     
>>> p = Person()
	     
>>> p.__name
	     
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    p.__name
AttributeError: 'Person' object has no attribute '__name'
>>> p.name
	     
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    p.name
AttributeError: 'Person' object has no attribute 'name'
>>> class Person:
	 __name = '小甲鱼'
	def getname(self):
	     
SyntaxError: unindent does not match any outer indentation level
>>> class Person:
	 __name = '小甲鱼'
	def getname(self):
	     
SyntaxError: unindent does not match any outer indentation level
>>> class Person:
	     __name = '小甲鱼'
	     def getname(self):
	            return self.__name

	     
>>> p = Person()
	     
>>> p.__name
	     
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    p.__name
AttributeError: 'Person' object has no attribute '__name'
>>> p.getname()
	     
'小甲鱼'
>>> p._Person__name
	     
'小甲鱼'
>>> #类中的变量可以被外部访问
