Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # TUPLES
>>> 
>>> L = ["red", "green", "blue"]
>>> type(L)
<class 'list'>
>>> T = ("red", "green", "blue")
>>> type(T)
<class 'tuple'>
>>> 
>>> # --------------- immutable
>>> 
>>> L[0]
'red'
>>> L[0] = "golden"
>>> L
['golden', 'green', 'blue']
>>> 
>>> T[0]
'red'
>>> T[0] = "golden"
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    T[0] = "golden"
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> # Tuple -> immutable lists
>>> 
>>> # cannot add, remove, re-arrange, modify elements
>>> 
>>> # -------------------- re-arrange
>>> reversed(T)
<reversed object at 0x0000026EDF9F9BE0>
>>> list(reverse(T))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    list(reverse(T))
NameError: name 'reverse' is not defined
>>> list(reversed(T))
['blue', 'green', 'red']
>>> sorted(T)
['blue', 'green', 'red']
>>> 
>>> 
>>> # --------------------- accessing elements
>>> 
>>> T[0]
'red'
>>> T[1:3]
('green', 'blue')
>>> T[::-1]
('blue', 'green', 'red')
>>> 
>>> # ------------------------ operators
>>> 
>>> (1, 2, 3) + (4, 5, 6)
(1, 2, 3, 4, 5, 6)
>>> 
>>> (1, 2, 3) * 3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> 
>>> len(T)
3
>>> 'red' in T
True
>>> 
>>> type(T) == tuple
True
>>> isinstance(T, tuple)
True
>>> del T
>>> 
>>> T = ["red", "green", "blue"]
>>> a, b, c = T # Can use with both lists and tuples
>>> a
'red'
>>> b
'green'
>>> c
'blue'
>>> # unpacking a tuple/list
>>> 
>>> T = ["red", "green", "blue", "Yellow"]
>>> a, b, c = T
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a, b, c = T
ValueError: too many values to unpack (expected 3)
>>> 
>>> a, b, *x = T
>>> a
'red'
>>> b
'green'
>>> x
['blue', 'Yellow']
>>> 
>>> 
>>> # ----------------------------- example
>>> 
>>> user = ("Anil Kumar", 35, "CoreCard", "anil@corecard.com", "anil4443!")
>>> user[-]
SyntaxError: invalid syntax
>>> usre[-1]
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    usre[-1]
NameError: name 'usre' is not defined
>>> user[-1]
'anil4443!'
>>> user[-1] = "skdljf"
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    user[-1] = "skdljf"
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> # What is the user changed the password?
>>> # How do we update the tuple?
>>> 
>>> temp = list(user)
>>> temp
['Anil Kumar', 35, 'CoreCard', 'anil@corecard.com', 'anil4443!']
>>> temp[-1] = 'kuma345!'
>>> temp
['Anil Kumar', 35, 'CoreCard', 'anil@corecard.com', 'kuma345!']
>>> user = tuple(temp)
>>> user
('Anil Kumar', 35, 'CoreCard', 'anil@corecard.com', 'kuma345!')
>>> 
