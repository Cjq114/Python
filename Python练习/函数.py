Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def MyFirstFunction():
	print('这是我创建的第一个函数！')
	print('我表示很鸡冻.....')
	print('在此我要感谢TVB，感谢CCAV，感谢小甲鱼，感谢各位鱼油.....')

	
>>> MyFirstFunction()
这是我创建的第一个函数！
我表示很鸡冻.....
在此我要感谢TVB，感谢CCAV，感谢小甲鱼，感谢各位鱼油.....
>>> MySceondFunction()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    MySceondFunction()
NameError: name 'MySceondFunction' is not defined
>>> def MySecondFunction(name)
SyntaxError: invalid syntax
>>> print(name+'我爱你‘）
	  
SyntaxError: EOL while scanning string literal
>>> 
	  
>>> def MySecondFunction(name)
	  
SyntaxError: invalid syntax
>>> def MySecondFunction(name)：
	  
SyntaxError: invalid character in identifier
>>> def MySecondFunction(name):
	  print(name+'我爱你‘）
		
SyntaxError: EOL while scanning string literal
>>> def MySecondFunction(name)
		
SyntaxError: invalid syntax
>>> def MySecondFunction(name):
		print(name+'我爱你!')

		
>>> MySecondFunction('傻环')
		
傻环我爱你!
>>> def add(num1, num2):
		result = num1 + num2
		print(result)

		
>>> add(1,2)
		
3
>>> def add(num1, num2):
	return(num1 + num2)

		
>>> print(add(5,6))
		
11
>>> 
		
>>> 
		
>>> def MyFirstFunction(name):
	print('传递进来的’+ name + '叫做实参，因为ta是具体的参数值！')
	      
SyntaxError: invalid character in identifier
>>> def MyFirstFunction(name):
	print('传递进来的'+ name + '叫做实参，因为ta是具体的参数值！')

	      
>>> MyFirstFunction('谢环')
	      
传递进来的谢环叫做实参，因为ta是具体的参数值！
>>> def MyFirstFunction(name):
	'函数定义过程中的name是叫形参'
	#因为ta知识一个形式，表示占据一个参数位置
	print('传递进来的'+ name + '叫做实参，因为ta是具体的参数值！')

	      
>>> MyFirstFunction.__doc__
	      
'函数定义过程中的name是叫形参'
>>> help(MyFirstFunction)
	      
Help on function MyFirstFunction in module __main__:

MyFirstFunction(name)
    函数定义过程中的name是叫形参

>>> def SaySome(name, words):
	print(name + '->' +words)

	      
>>> SaySome('小甲鱼' + '让编程改变世界！')
	      
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    SaySome('小甲鱼' + '让编程改变世界！')
TypeError: SaySome() missing 1 required positional argument: 'words'
>>> SaySome('小甲鱼' ,'让编程改变世界！')
	      
小甲鱼->让编程改变世界！
>>> def SaySome(name='小甲鱼', words='让编程改变世界'):
	print(name + '->' +words)

	      
>>> SaySome()
	      
小甲鱼->让编程改变世界
>>> SaySome('傻环')
	      
傻环->让编程改变世界
>>> SaySome('傻环', '我爱你！')
	      
傻环->我爱你！
>>> def test(*params):
	print('参数的长度是：',len(params));
	print('第二个参数是：',params[1]);

	      
>>> test(1,'傻环',4,16.34,55,7,9)
	      
参数的长度是： 7
第二个参数是： 傻环
>>> def test(*params, exp):
	print('参数的长度是：',len(params),exp);
	print('第二个参数是：',params[1]);

	      
>>> test(1,'傻环',4, 16.34, 55, 7, 9, exp = 8)
	      
参数的长度是： 7 8
第二个参数是： 傻环
>>> 
	      
>>> 
	      
>>> 
	      
>>> def hello():
	print('Hello fishC!')

	      
>>> temp = hello()
	      
Hello fishC!
>>> temp
	      
>>> print(temp)
	      
None
>>> type(temp)
	      
<class 'NoneType'>
>>> 
	      
>>> def back():
	return[1,'傻环', 3.14]

	      
>>> back()
	      
[1, '傻环', 3.14]
>>> def back():
	return 1,'傻环', 3.14

>>> back()
	      
(1, '傻环', 3.14)
>>> 
