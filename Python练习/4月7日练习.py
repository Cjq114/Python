Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
======================= RESTART: D:/Python/日常练习/汉诺塔.py =======================
请输入汉诺塔的层数：3
x --> z
y --> z
x --> z
>>> 
======================= RESTART: D:/Python/日常练习/汉诺塔.py =======================
请输入汉诺塔的层数：3
x --> z
x --> y
z --> y
x --> z
y --> x
y --> z
x --> z
>>> brand = ['李宁', '耐克', '阿迪达斯', '鱼c工作室']
>>> slogan = ['一切皆有可能', 'Just do it', 'Impossible is nothing', '让编程改变世界']
>>> print('鱼c工作室的口号是：'， slogan[brand.index('鱼c工作室')])
SyntaxError: invalid character in identifier
>>> print('鱼c工作室的口号是：', slogan[brand.index('鱼c工作室')])
鱼c工作室的口号是： 让编程改变世界
>>> dict1 = {'李宁':'一切皆有可能', '耐克';'Just do it', '阿迪达斯':'Impossible is nothing', '鱼c工作室':'让编程改变世界'}
SyntaxError: invalid syntax
>>> dict1 = {'李宁':'一切皆有可能', '耐克':'Just do it', '阿迪达斯':'Impossible is nothing', '鱼c工作室':'让编程改变世界'}
>>> print('鱼c工作室的口号是：'， dict1['鱼c工作室'])
SyntaxError: invalid character in identifier
>>> print('鱼c工作室的口号是：', dict1['鱼c工作室'])
鱼c工作室的口号是： 让编程改变世界
>>> dict2 = {1:'one',2:'two',3:'three' }
>>> dict2
{1: 'one', 2: 'two', 3: 'three'}
>>> dict2[2]
'two'
>>> dict3{}
SyntaxError: invalid syntax
>>> dict3 = {}
>>> dict3
{}
>>> dict()
{}
>>> dict3 = dict((('F',70),('i',105),('s'115),('h',184),('C',67)))
SyntaxError: invalid syntax
>>> dict3 = dict((('F',70),('i',105),('s',115),('h',184),('C',67)))
>>> dict3
{'F': 70, 'i': 105, 's': 115, 'h': 184, 'C': 67}
>>> 
>>> 
>>> 
>>> 
>>> num = {]
SyntaxError: invalid syntax
>>> num = {}
>>> type(num)
<class 'dict'>
>>> num2 = {1, 2, 3, 4, 5}
>>> type(num2)
<class 'set'>
>>> num2 = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
>>> num2
{1, 2, 3, 4, 5}
>>> set1 = set([1, 2, 3, 4, 5, 5])
>>> set1
{1, 2, 3, 4, 5}
>>> set3 = set([1, 2, 3, 4, 5, 5, 3, 1,0])
>>> set3
{0, 1, 2, 3, 4, 5}
>>> num2
{1, 2, 3, 4, 5}
>>> num2.add(6)
>>> num2
{1, 2, 3, 4, 5, 6}
>>> num2.remove(5)
>>> num5
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    num5
NameError: name 'num5' is not defined
>>> num2
{1, 2, 3, 4, 6}
>>> num3 = frozenset([1, 2, 3, 4, 5])
>>> num3
frozenset({1, 2, 3, 4, 5})
>>> num3.add(6)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    num3.add(6)
AttributeError: 'frozenset' object has no attribute 'add'
>>> 
