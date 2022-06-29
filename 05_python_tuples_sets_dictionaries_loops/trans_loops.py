Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # LOOPS
>>> 
>>> s = "python"
>>> for c in s:
	print(c)

	
p
y
t
h
o
n
>>> for c in s:
	print(c , end = ' ')

	
p y t h o n 
>>> for c in s:
	print(c, end = '-')

	
p-y-t-h-o-n-
>>> 
>>> 
>>> 
>>> for item in ["red", "green", "blue"]:
	print(item.upper())

	
RED
GREEN
BLUE
>>> 
>>> for item in ("red", "green", "blue"):
	print(item.upper())

	
RED
GREEN
BLUE
>>> 
>>> for key in {"name":"anil", "age":34, "company":"corecard"}:
	print(key)

	
name
age
company
>>> 
>>> D = {"name":"anil", "age":34, "company":"corecard"}
>>> for item in D.items():
	print(item)

	
('name', 'anil')
('age', 34)
('company', 'corecard')
>>> 
>>> 
>>> for key, value in D.item():
	print(key, ' --> ', value)

	
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    for key, value in D.item():
AttributeError: 'dict' object has no attribute 'item'
>>> for key, value in D.items():
	print(key, ' --> ', value)

	
name  -->  anil
age  -->  34
company  -->  corecard
>>> 
>>> 
>>> # -------------------------------------
>>> 
>>> # Multiplication table
>>> 
>>> print(5, ' X ', 1, ' = ', 5 * 1)
5  X  1  =  5
>>> 
>>> 
>>> for i in [1, 2, 3, 4, 5]:
	print(5, ' X ', i, ' = ', 5 * i)

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
>>> 
>>> 
>>> for i in range(1, 11):
	print(5, ' X ', i, ' = ', 5 * i)

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
5  X  6  =  30
5  X  7  =  35
5  X  8  =  40
5  X  9  =  45
5  X  10  =  50
>>> 
>>> 
>>> i = 1
>>> while i <= 10:
	print(5, ' X ', i, ' = ', 5 * i)
	i += 1

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
5  X  6  =  30
5  X  7  =  35
5  X  8  =  40
5  X  9  =  45
5  X  10  =  50
>>> 
>>> 
>>> 
>>> # ----------------------------- Loop control statements
>>> 
>>> # break, continue
>>> 
>>> for i in range(1, 11):
	if(i == 5):
		break
	print(5, ' X ', i, ' = ', 5 * i)

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
>>> 
>>> 
>>> for i in range(1, 11):
	if(i % 3 == 0):
		continue
	print(5, ' X ', i, ' = ', 5 * i)

	
5  X  1  =  5
5  X  2  =  10
5  X  4  =  20
5  X  5  =  25
5  X  7  =  35
5  X  8  =  40
5  X  10  =  50
>>> 
