Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> '%c'%97
'a'
>>> '%c %c %c'%(97,98,99)
'a b c'
>>> '%s'% 'I love FishC.com'
'I love FishC.com'
>>> '%d + %d = %d '% (4,5,4+5)
'4 + 5 = 9 '
>>> '%o' % 10
'12'
>>> '%x'% 10
'a'
>>> '%X' % 10
'A'
>>> '%x' % 160
'a0'
>>> '%f' % 27.658
'27.658000'
>>> '%e' % 27.658
'2.765800e+01'
>>> '%E' % 27.658
'2.765800E+01'
>>> '%g' % 27.658
'27.658'
>>> '%f' % 27658
'27658.000000'
>>> '%5.1f' % 27.658
' 27.7'
>>> '%.21f' % 27.658
'27.658000000000001250555'
>>> '%.2e' % 27.658
'2.77e+01'
>>> '%#o' % 10
'0o12'
>>> '%#X' % 108
'0X6C'
>>> '%#d' %  108
'108'
>>> '%010d' % 5
'0000000005'
>>> '%-010d' % 5
'5         '
>>> help(list)
Help on class list in module builtins:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.n
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      L.__reversed__() -- return a reverse iterator over the list
 |  
 |  __rmul__(self, value, /)
 |      Return self*value.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      L.__sizeof__() -- size of L in memory, in bytes
 |  
 |  append(...)
 |      L.append(object) -> None -- append object to end
 |  
 |  clear(...)
 |      L.clear() -> None -- remove all items from L
 |  
 |  copy(...)
 |      L.copy() -> list -- a shallow copy of L
 |  
 |  count(...)
 |      L.count(value) -> integer -- return number of occurrences of value
 |  
 |  extend(...)
 |      L.extend(iterable) -> None -- extend list by appending elements from the iterable
 |  
 |  index(...)
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |  
 |  insert(...)
 |      L.insert(index, object) -- insert object before index
 |  
 |  pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(...)
 |      L.remove(value) -> None -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(...)
 |      L.reverse() -- reverse *IN PLACE*
 |  
 |  sort(...)
 |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> a = list()
>>> a
[]
>>> b
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> b = 'I love FishC.com'
>>> b
'I love FishC.com'
>>> b = list(b)
>>> b
['I', ' ', 'l', 'o', 'v', 'e', ' ', 'F', 'i', 's', 'h', 'C', '.', 'c', 'o', 'm']
>>> c = (1,1,2,3,5,8,13,21,34)
>>> c = list(c)
>>> c
[1, 1, 2, 3, 5, 8, 13, 21, 34]
>>> max(1,2,3,4,5)
5
>>> max(b)
'v'
>>> len(b)
16
>>> chars = '1234567890'
>>> min(chars)
'0'
>>> tuple1 = (1,2,3,4,5,6,7,8,9,0)
>>> max(tuple1)
9
>>> tuple2 = (3.1 ,2.3 ,3.4)
>>> sum(tuple2)
8.8
>>> sum(chars)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    sum(chars)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> sorted(tuple2)
[2.3, 3.1, 3.4]
>>> reversed(tupled2)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    reversed(tupled2)
NameError: name 'tupled2' is not defined
>>> reversed(tuple2)
<reversed object at 0x000000C0DAEC8C88>
>>> list(reversed(tuple2))
[3.4, 2.3, 3.1]
>>> list(enumerate(tuple2))
[(0, 3.1), (1, 2.3), (2, 3.4)]
>>> a = [1,2,3,4,5,6,7,8]
>>> b =[4,5,6,7,8]
>>> zip(a,b)
<zip object at 0x000000C0DAED9648>
>>> list(zip(a,b))
[(1, 4), (2, 5), (3, 6), (4, 7), (5, 8)]
>>> 
