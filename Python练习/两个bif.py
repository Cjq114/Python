Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def ds(x):
	return 2 * x + 1

>>> ds(5)
11
>>> lambda x : 2 * x + 1
<function <lambda> at 0x000000BAB9FA1EA0>
>>> g = lambda x : 2 * x + 1
>>> g(s)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    g(s)
NameError: name 's' is not defined
>>> g(5)
11
>>> lambda x, y : x + y
<function <lambda> at 0x000000BAB9FA1EA0>
>>> g(3,4)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    g(3,4)
TypeError: <lambda>() takes 1 positional argument but 2 were given
>>> g = lambda x, y : x + y
>>> g(3,4)
7
>>> help(filter)
Help on class filter in module builtins:

class filter(object)
 |  filter(function or None, iterable) --> filter object
 |  
 |  Return an iterator yielding those items of iterable for which function(item)
 |  is true. If function is None, return the items that are true.
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.

>>> filter(none, [1,2,False,True])
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    filter(none, [1,2,False,True])
NameError: name 'none' is not defined
>>> filter(None, [1,2,False,True])
<filter object at 0x000000BABAAF76D8>
>>> list(filter(None, [1,2,False,True]))
[1, 2, True]
>>> def odd(x):
	return x % 2

>>> temp = range(10)
>>> show = filter(odd,temp)
>>> list(show)
[1, 3, 5, 7, 9]
>>> list(filter(lambda x : x%2,range(10)))
[1, 3, 5, 7, 9]
>>> list(map(lambda x : x * 2, range(10)))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> 
