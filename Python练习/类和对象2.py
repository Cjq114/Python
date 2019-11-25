Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
====================== RESTART: D:/Python/日常练习/类和对象.py ======================
>>> tt = Turtle()
>>> tt.climb()
我正在很努力的向前爬.....
>>> tt.bite()
咬死你咬死你！！
>>> tt.sleep()
困了，睡了，晚安，Zzzz
>>> list1 = [2, 1, 7, 5, 3]
>>> list1.sort()
>>> list1
[1, 2, 3, 5, 7]
>>> list1.append(9)
>>> list1
[1, 2, 3, 5, 7, 9]
>>> class Mylist(list): #继承list
	pass

>>> list2 = Mylist()
>>> list2.append(5)
>>> list2.append(3)
>>> list2.append(7)
>>> list2
[5, 3, 7]
>>> list2.sort()
>>> list2
[3, 5, 7]
>>> #继承了list的可添加的性质
>>> class A:
	def fun(self):
		print('我是小A..')

		
>>> class B:
	def fun(self):
		print('我是小B...')

		
>>> a = A()
>>> b = B()
>>> a.fun()
我是小A..
>>> b.fun()
我是小B...
>>> #多态，显示的形式不一样
