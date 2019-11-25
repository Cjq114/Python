Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def myGen():
	print('生成器被执行！')
	yield 1
	yield 2

	
>>> myG = myGen()
>>> next(myG)
生成器被执行！
1
>>> next(nyG)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    next(nyG)
NameError: name 'nyG' is not defined
>>> next(myG)
2
>>> next(myG)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    next(myG)
StopIteration
>>> 
>>> def fibs():
	a = 0
	b = 1
	while True:
		a, b = b, a + b
		yield a

		
>>> for each in fibs():
	if each > 100:
		break
	print(each, end = '')

	
1123581321345589
>>>  for each in fibs():
	if each > 100:
		break
	print(each, end = ' ')
	
SyntaxError: unexpected indent
>>> for each in fibs():
	if each > 100:
		break
	print(each, end = ' ')

	
1 1 2 3 5 8 13 21 34 55 89 
>>> a = [i for i in range(100) if not(i % 2) and i % 3]
>>> a
[2, 4, 8, 10, 14, 16, 20, 22, 26, 28, 32, 34, 38, 40, 44, 46, 50, 52, 56, 58, 62, 64, 68, 70, 74, 76, 80, 82, 86, 88, 92, 94, 98]
>>> b = [i:i % 2 == 0 for i in range(10)]
SyntaxError: invalid syntax
>>>  b = [i;i % 2 == 0 for i in range(10)]
SyntaxError: unexpected indent
>>> b = [i;i % 2 == 0 for i in range(10)]
SyntaxError: invalid syntax
>>> sum(i for i in range(100) if i % 2)
2500
>>> 
