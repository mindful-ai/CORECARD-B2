Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # LIST

>>> L = ["red", "green", "blue", 3, 4.5, -67, [1,2,3]]
>>> L
['red', 'green', 'blue', 3, 4.5, -67, [1, 2, 3]]
>>> type(L)
<class 'list'>
>>> 
>>> # ----------------------------- Multable aspect
>>> 
>>> L[0]
'red'
>>> L[0] = "golden"
>>> L
['golden', 'green', 'blue', 3, 4.5, -67, [1, 2, 3]]
>>> 
>>> L[1]
'green'
>>> L[1][2]
'e'
>>> L[1][2] = 'x'
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    L[1][2] = 'x'
TypeError: 'str' object does not support item assignment
>>> 
>>> # ------------------------------ subscripting
>>> 
>>> L
['golden', 'green', 'blue', 3, 4.5, -67, [1, 2, 3]]
>>> L[0]
'golden'
>>> L[1]
'green'
>>> L[-1]
[1, 2, 3]
>>> L[-1[-1]



  ;
  
SyntaxError: invalid syntax
>>> L[-1][-1]
3
>>> L[::2]
['golden', 'blue', 4.5, [1, 2, 3]]
>>> L[::-1]
[[1, 2, 3], -67, 4.5, 3, 'blue', 'green', 'golden']
>>> 
>>> 
>>> # ------------------------------------ operators
>>> 
>>> [1,2,3] +[4,5,6]
[1, 2, 3, 4, 5, 6]
>>> [1, 2, 3] * 2
[1, 2, 3, 1, 2, 3]
>>> L
['golden', 'green', 'blue', 3, 4.5, -67, [1, 2, 3]]
>>> "red" in L
False
>>> type(L) == list
True
>>> isinstance(L, list)
True
>>> len(L)
7
>>> del L
>>> L
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    L
NameError: name 'L' is not defined
>>> 
>>> 
>>> # ---------------------------------- MOdifiy lists
>>> 
>>> L = ["red", "green", "blue"]
>>> L[1] = "yellow"
>>> L
['red', 'yellow', 'blue']
>>> 
>>> 
>>> # ------------------------------- Adding to a list
>>> 
>>> L
['red', 'yellow', 'blue']
>>> L.append('green')
>>> L
['red', 'yellow', 'blue', 'green']
>>> L.append('pink')
>>> L
['red', 'yellow', 'blue', 'green', 'pink']
>>> 
>>> L.insert(1, 'orange')
>>> L
['red', 'orange', 'yellow', 'blue', 'green', 'pink']
>>> 
>>> 
>>> L1 = ['black', 'white', 'grey']
>>> L.extend(L1)
>>> L
['red', 'orange', 'yellow', 'blue', 'green', 'pink', 'black', 'white', 'grey']
>>> 
>>> 
>>> L = ['red', 'yellow', 'blue']
>>> L1
['black', 'white', 'grey']
>>> L[1]
'yellow'
>>> L[1] = L1
>>> L
['red', ['black', 'white', 'grey'], 'blue']
>>> 
>>> 
>>> L = ['red', 'yellow', 'blue']
>>> L[1:2]
['yellow']
>>> L[1:2] = L1
>>> L
['red', 'black', 'white', 'grey', 'blue']
>>> 
>>> 
>>> L
['red', 'black', 'white', 'grey', 'blue']
>>> L.append('red')
>>> L
['red', 'black', 'white', 'grey', 'blue', 'red']
>>> 
>>> 
>>> # ------------------------------------------- removing elements from a list
>>> 
>>> L
['red', 'black', 'white', 'grey', 'blue', 'red']
>>> L.pop()
'red'
>>> L
['red', 'black', 'white', 'grey', 'blue']
>>> L.pop(1)
'black'
>>> L
['red', 'white', 'grey', 'blue']
>>> L.remove('grey')
>>> L
['red', 'white', 'blue']
>>> 
>>> 
>>> # -------------------------------------- search in a list
>>> 
>>> L = ['red', 'black', 'white', 'grey', 'blue', 'red']
>>> 'red' in L
True
>>> L.index('black')
1
>>> L.index('red')
0
>>> L.count("red")
2
>>> # ---------------------------------- re-arrangement of elements
>>> # sorting and reversing
>>> 
>>> L
['red', 'black', 'white', 'grey', 'blue', 'red']
>>> L[::-1]
['red', 'blue', 'grey', 'white', 'black', 'red']
>>> reversed(L)
<list_reverseiterator object at 0x000002137FC3BDA0>
>>> list(reversed(L))
['red', 'blue', 'grey', 'white', 'black', 'red']
>>> sorted(L)
['black', 'blue', 'grey', 'red', 'red', 'white']
>>> L
['red', 'black', 'white', 'grey', 'blue', 'red']
>>> # The original list remains as is
>>> 
>>> 
>>> # OO functions for sorting and reversing
>>> L.sort()
>>> L
['black', 'blue', 'grey', 'red', 'red', 'white']
>>> L.sort(reverse=True)
>>> L
['white', 'red', 'red', 'grey', 'blue', 'black']
>>> L.reverse()
>>> L
['black', 'blue', 'grey', 'red', 'red', 'white']
>>> 
>>> 
>>> # ---------------------------- iterating on a list
>>> 
>>> for item in L
SyntaxError: invalid syntax
>>> for item in L:
	print(item)

	
black
blue
grey
red
red
white
>>> for item in L:
	print(item, ' ---> ', len(item))

	
black  --->  5
blue  --->  4
grey  --->  4
red  --->  3
red  --->  3
white  --->  5
>>> 
>>> 
>>> # ------------------------------- in-built functions for numeric arrays
>>> 
>>> L = [2, 3, 4, 5, 6, 7, 8]
>>> max(L)
8
>>> min(L)
2
>>> sum(L)
35
>>> any(L)
True
>>> all(L)
True
>>> L.append(0)
>>> all(L)
False
>>> 
>>> 
>>> # --------------------------- generate array of numbers
>>> 
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(10, 20))
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> list(range(1, 30, 3))
[1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
>>> list(range(10, 0, -1))
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> 
