Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # COMPREHENSIONS
>>> 
>>> 
>>> L = list(range(1, 11))
>>> L
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> S = []
>>> for n in L:
	S.append(n**2)

	
>>> S
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> 
>>> C = [x**2 for x in L]
>>> C
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> C = [x**2 for x in L if x % 3 == 0]
>>> C
[9, 36, 81]
>>> 
>>> # Syntax:
>>> # Comprehension always produces a collected
>>> 
>>> # [], (), {}
>>> # [<expr> <loop> <condition>]
>>> 
>>> L
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> [(x, x**2, x**3) for x in L]
[(1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125), (6, 36, 216), (7, 49, 343), (8, 64, 512), (9, 81, 729), (10, 100, 1000)]
>>> 
>>> 
>>> S = ["red", "green", "blue", "yellow"]
>>> [len(s) for s in S]
[3, 5, 4, 6]
>>> {key:len(key) for key in S}
{'red': 3, 'green': 5, 'blue': 4, 'yellow': 6}
>>> {key:len(key) for key in S if len(key) > 3}
{'green': 5, 'blue': 4, 'yellow': 6}
>>> 
>>> 
>>> L
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> [x**2 for x in L if(x % 3 == 0)]
[9, 36, 81]
>>> [x**2 if x % 3 == 0 else x for x in L]
[1, 2, 9, 4, 5, 36, 7, 8, 81, 10]
>>> 
