Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # SETS
>>> 
>>> s = "mississippi"
>>> list(s)
['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
>>> tuple(s)
('m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i')
>>> set(s)
{'m', 's', 'p', 'i'}
>>> 
>>> 
>>> s1 = set("abcdefg")
>>> s1
{'f', 'c', 'b', 'd', 'g', 'e', 'a'}
>>> s2 = {'d', 'e', 'f', 'g', 'h', 'i', 'j'}
>>> s2
{'i', 'j', 'f', 'h', 'd', 'g', 'e'}
>>> s1[0]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s1[0]
TypeError: 'set' object is not subscriptable
>>> 
>>> # -------- sets are not subscriptable, meaning they cannot be accessed
>>> # via indexes
>>> 
>>> 
>>> s1
{'f', 'c', 'b', 'd', 'g', 'e', 'a'}
>>> s2
{'i', 'j', 'f', 'h', 'd', 'g', 'e'}
>>> 
>>> 
>>> s1 | s2
{'i', 'j', 'f', 'c', 'b', 'd', 'g', 'e', 'h', 'a'}
>>> s1 & s2
{'g', 'e', 'f', 'd'}
>>> s1 ^ s2
{'i', 'j', 'c', 'h', 'b', 'a'}
>>> 
>>> 
>>> 
>>> s1.add('x')
>>> s1
{'f', 'c', 'b', 'd', 'g', 'e', 'x', 'a'}
>>> s1.update({'y', 'z'})
>>> s1
{'f', 'z', 'y', 'c', 'b', 'd', 'g', 'e', 'x', 'a'}
>>> s1.intersection(s2)
{'g', 'e', 'f', 'd'}
>>> s1.union(s2)
{'i', 'j', 'f', 'z', 'y', 'c', 'b', 'd', 'g', 'e', 'x', 'h', 'a'}
>>> 
>>> 
>>> 'x' in s1
True
>>> s1.remove('x')
>>> s1
{'f', 'z', 'y', 'c', 'b', 'd', 'g', 'e', 'a'}
>>> 
