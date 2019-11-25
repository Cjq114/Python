Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> count = 5
>>> def MyFun():
	count = 10
	print(10)

	
>>> MyFun()
10
>>> print(count)
5
>>> def MyFun():
	global count
	count = 10
	print(10)

>>> MyFun()
10
>>> print(count)
10
>>> def fun1():
	print('fun1()正在被调用...')
	def fun2():
		print('fun2正在被调用...')
	fun2()

	
>>> fun1
<function fun1 at 0x000000143A71E9D8>
>>> def fun1():
	print('fun1()正在被调用...')
	def fun2():
		print('fun2()正在被调用...')
	fun2()

	
>>> fun1()
fun1()正在被调用...
fun2()正在被调用...
>>> fun2()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    fun2()
NameError: name 'fun2' is not defined
>>> def FunX(x):
	def FunY(y):
		return x = y
	
SyntaxError: invalid syntax
>>> def FunX(x):
	def FunY(y):
		return x * y
	return FunY

>>> i = FunX(8)
>>> i
<function FunX.<locals>.FunY at 0x000000143A70DF28>
>>> type(i)
<class 'function'>
>>> i(5)
40
>>> FunX(8)(5)
40
>>> def Fun1():
	x = 5
	def Fun2():
		x *= x
		return x
	return Fun2()

>>> Fun1()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    Fun1()
  File "<pyshell#38>", line 6, in Fun1
    return Fun2()
  File "<pyshell#38>", line 4, in Fun2
    x *= x
UnboundLocalError: local variable 'x' referenced before assignment
>>> def Fun1():
	x = [5]
	def Fun2():
		x[0] *= x[0]
		return x[0]
	return Fun2()

>>> Fun1()
25
>>> def Fun1():
	x = 5
	def Fun2():
		nonlocal x
		x *= x
		return x
	return Fun2()

>>> Fun1()
25
>>> 
