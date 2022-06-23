Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # NUMBERS
>>> 
>>> a = 5
>>> b = 7.8
>>> 
>>> type(a)
<class 'int'>
>>> type(b)
<class 'float'>
>>> 
>>> c = +6.7
>>> d = -9.0
>>> # --------------------------- Operators
>>> 
>>> # Arithmetic Operators
>>> 
>>> a = 10
>>> b = 5
>>> c= a + b
>>> print(c)
15
>>> a + b
15
>>> a
10
>>> b
5
>>> c
15
>>> a - b
5
>>> a * b
50
>>> a / b
2.0
>>> 5/3
1.6666666666666667
>>> 5 % 3
2
>>> 5 // 3
1
>>> a ** 3
1000
>>> 
>>> 
>>> # Relational operators
>>> 
>>> a > b # Is a greater than b?
True
>>> a < b
False
>>> a >= b
True
>>> a <= b
False
>>> a == b * 2
True
>>> a != b
True
>>> 
>>> 
>>> # Logical operators
>>> 
>>> a > b and a < 10
False
>>> # && || ! ~
>>> 
>>> a > b or a < 10
True
>>> 
>>> a > b and not a < 10
True
>>> 
>>> # -------------------------- built-in functions
>>> 
>>> a = 100
>>> bin(a)
'0b1100100'
>>> hex(a)
'0x64'
>>> oct(a)
'0o144'
>>> 
>>> type(a)
<class 'int'>
>>> b = float(a)
>>> type(b)
<class 'float'>
>>> 
>>> 
>>> b = '1010'
>>> int(b)
1010
>>> int(b, 2)
10
>>> 
>>> 
>>> n = '12'
>>> type(n)
<class 'str'>
>>> n + 10
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    n + 10
TypeError: can only concatenate str (not "int") to str
>>> int(n) + 10
22
>>> float(n) + 10
22.0
>>> 
>>> 
>>> 
>>> a = 10
>>> b = 5
>>> a- b
5
>>> b - a
-5
>>> abs(a - b)
5
>>> abs(b - a)
5
>>> # --------------------------------------- built-in modules
>>> 
>>> angle = 90
>>> # I want to calculate the sine of 90
>>> 
>>> sin(a)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    sin(a)
NameError: name 'sin' is not defined
>>> 
>>> import math
>>> math.sin(a)
-0.5440211108893698
>>> a
10
>>> math.sin(angle)
0.8939966636005579
>>> math.sin(angle * 3.14/180)
0.9999996829318346
>>> math.sin(angle * 3.14159/180)
0.9999999999991198
>>> math.sin(angle * math.pi/180)
1.0
>>> math.sin(math.radians(angle))
1.0
>>> 
