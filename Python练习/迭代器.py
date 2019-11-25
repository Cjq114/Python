Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for i in "FishC":
	print(i)

	
F
i
s
h
C
>>> string = "FishC"
>>> it = iter(string)
>>> next(it)
'F'
>>> next(it)
'i'
>>> next(it)
's'
>>> next(it)
'h'
>>> 
>>> next(it)
'C'
>>> class Fibs:
	def __init__(self, n=10):
		self.a = 0
		self.b = 1
		self.n = n

		
>>> class Fibs:
	def __init__(self, n=10):
		self.a = 0
		self.b = 1
		self.n = n
	def __iter__()
	
SyntaxError: invalid syntax
>>> class Fibs:
	def __init__(self, n=10):
		self.a = 0
		self.b = 1
		self.n = n
	def __iter__(self):
		return self
	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > self.n:
			raise StopIteration
		return self.a

	
>>> fisbs = Fibs()
>>> for each in fibs:
	print(each)

	
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    for each in fibs:
NameError: name 'fibs' is not defined
>>> fisbs = Fibs()
>>> for each in fisbs:
	print(each)
	
SyntaxError: multiple statements found while compiling a single statement
>>> fibs = Fibs()
>>> for each in fibs:
	print(each)

	
1
1
2
3
5
8
>>> 
