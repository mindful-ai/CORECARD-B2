Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # PYTHON FEATURES
>>> 
>>> # Lambda expressions
>>> # It's an expression that can produce a function object
>>> 
>>> f = lambda a, b : a + b
>>> f
<function <lambda> at 0x000001F4CA87C6A8>
>>> # lambda <input> : <output>
>>> 
>>> f(10, 20)
30
>>> f("abc", "def")
'abcdef'
>>> f([1,2,3], [4, 5, 6])
[1, 2, 3, 4, 5, 6]
>>> 
>>> cm2inches = lambda cm : cm / 2.9
>>> cm2inches(100)
34.48275862068966
>>> cm2inches(34)
11.724137931034484
>>> cm2inches(29)
10.0
>>> 
>>> 
>>> L = ["red", "greeb", "blue", "yellow", "pink"]
>>> L.sort()
>>> L
['blue', 'greeb', 'pink', 'red', 'yellow']
>>> L.sort(key=lambda s : s[-1])
>>> L
['greeb', 'red', 'blue', 'pink', 'yellow']
>>> 
>>> 
>>> # ---------------------------------- map()
>>> 
>>> T = [12, 34, 56, 78, 99, 100] # TEmperatures in celcuiius
>>> F = []
>>> for t in T:
	tf = t * 1.8 + 32
	F.append(tf)

	
>>> F
[53.6, 93.2, 132.8, 172.4, 210.20000000000002, 212.0]
>>> 

>>> F1 = map(lambda t : t * 1.8 + 32, T)
>>> F1
<map object at 0x000001F4CA88F278>
>>> list(F1)
[53.6, 93.2, 132.8, 172.4, 210.20000000000002, 212.0]
>>> 
>>> 
>>> L
['greeb', 'red', 'blue', 'pink', 'yellow']
>>> L2 = [5, 3, 4, 4, 6]
>>> 
>>> L2 = map(lambda s : len(s), L)
>>> list(L2)
[5, 3, 4, 4, 6]
>>> 
>>> 
>>> # --------------------------------- filter()
>>> 
>>> import random
>>> random.randint(1, 100)
52
>>> random.randint(1, 100)
50
>>> random.randint(1, 100)
67
>>> random.randint(1, 100)
76
>>> random.randint(1, 100)
73
>>> random.randint(1, 100)
24
>>> R = []
>>> for i in range(100):
	R.append(random.randint(1, 100))

	
>>> R
[43, 18, 66, 79, 66, 17, 64, 46, 67, 80, 74, 56, 29, 94, 36, 20, 98, 82, 71, 83, 27, 2, 32, 11, 37, 88, 88, 81, 71, 7, 66, 83, 51, 34, 86, 6, 66, 86, 45, 83, 79, 70, 93, 58, 9, 65, 85, 45, 87, 22, 31, 91, 76, 62, 72, 28, 86, 2, 82, 1, 47, 14, 14, 68, 49, 34, 23, 58, 73, 27, 57, 33, 94, 92, 52, 21, 64, 62, 67, 68, 73, 19, 5, 40, 48, 44, 87, 32, 25, 9, 70, 96, 42, 71, 47, 71, 24, 28, 79, 83]
>>> 
>>> 
>>> # List of all numbers extracted from R
>>> # which are divisible by 13
>>> 
>>> R = []
>>> R
[]
>>> for i in range(100):
	R.append(random.randint(1, 100))

	
>>> R
[26, 8, 29, 70, 10, 87, 4, 7, 62, 42, 35, 8, 77, 34, 14, 43, 79, 66, 9, 80, 5, 6, 37, 15, 86, 39, 24, 51, 98, 92, 73, 41, 6, 9, 1, 22, 80, 2, 85, 5, 27, 76, 41, 12, 99, 16, 83, 16, 14, 70, 91, 24, 73, 12, 49, 23, 18, 34, 56, 73, 15, 74, 87, 93, 73, 41, 15, 14, 73, 92, 27, 97, 36, 16, 56, 55, 70, 22, 79, 7, 61, 25, 52, 80, 86, 45, 65, 75, 26, 40, 67, 49, 9, 23, 50, 91, 20, 74, 9, 68]
>>> 
>>> R1 = []
>>> for n in R:
	if(n % 13 == 0):
		R1.append(n)

		
>>> R1
[26, 39, 91, 52, 65, 26, 91]
>>> 
>>> R2 = filter(lambda n : n%13 == 0, R)
>>> R2
<filter object at 0x000001F4CA8A9828>
>>> list(R2)
[26, 39, 91, 52, 65, 26, 91]
>>> 
>>> R3 = map(lambda n : n%13 == 0, R)
>>> R3
<map object at 0x000001F4CA8A99B0>
>>> list(R3)
[True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, False, True, False, False, False, False, False, False, True, False, False, False, False]
>>> 
>>> 
>>> 
>>> # ------------------------------------- zip()
>>> 
>>> T1 = ["anil", "sunil", "raj"]
>>> T2 = (24, 25, 26)
>>> zip(T1, T2)
<zip object at 0x000001F4CA8AC588>
>>> list(zip(T1, T2))
[('anil', 24), ('sunil', 25), ('raj', 26)]
>>> dict(zip(T1, T2))
{'anil': 24, 'sunil': 25, 'raj': 26}
>>> 
>>> 
>>> D = {'anil': 24, 'sunil': 25, 'raj': 26}
>>> D.keys()
dict_keys(['anil', 'sunil', 'raj'])
>>> D.value()
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    D.value()
AttributeError: 'dict' object has no attribute 'value'
>>> D.values()
dict_values([24, 25, 26])
>>> 
>>> 
>>> list(zip(*D.items()))
[('anil', 'sunil', 'raj'), (24, 25, 26)]
>>> 
>>> # ----------------------------- LAB
>>> 
>>> R
[26, 8, 29, 70, 10, 87, 4, 7, 62, 42, 35, 8, 77, 34, 14, 43, 79, 66, 9, 80, 5, 6, 37, 15, 86, 39, 24, 51, 98, 92, 73, 41, 6, 9, 1, 22, 80, 2, 85, 5, 27, 76, 41, 12, 99, 16, 83, 16, 14, 70, 91, 24, 73, 12, 49, 23, 18, 34, 56, 73, 15, 74, 87, 93, 73, 41, 15, 14, 73, 92, 27, 97, 36, 16, 56, 55, 70, 22, 79, 7, 61, 25, 52, 80, 86, 45, 65, 75, 26, 40, 67, 49, 9, 23, 50, 91, 20, 74, 9, 68]
>>> 
>>> 
>>> 
>>> R = []
>>> for i in range(100):
	R.append(random.randint(1, 100))

	
>>> R
[43, 23, 97, 57, 93, 6, 15, 7, 83, 78, 12, 9, 83, 7, 37, 8, 5, 27, 2, 30, 43, 97, 12, 73, 84, 7, 59, 28, 73, 76, 19, 4, 17, 64, 80, 78, 3, 92, 16, 86, 16, 87, 82, 82, 40, 100, 59, 92, 86, 21, 45, 33, 34, 81, 41, 90, 87, 37, 6, 82, 21, 69, 89, 5, 84, 91, 73, 89, 94, 96, 90, 40, 61, 15, 23, 14, 39, 44, 100, 89, 9, 83, 23, 21, 44, 100, 27, 52, 37, 68, 82, 37, 83, 21, 1, 58, 78, 37, 79, 52]
>>> 
>>> 
>>> # filter all two digit values
>>> # filter all two digit values from R whose sum of individual digits is 10
>>> # [19, 28, 37, ... 91]
>>> 
