Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # OUTPUT
>>> 
>>> print("This is a message")
This is a message
>>> a = 10
>>> print("This is a message : ", a)
This is a message :  10
>>> print("This is a message : %d" % (a))
This is a message : 10
>>> 
>>> 
>>> # INPUTS
>>> 
>>> input()
12
'12'
>>> i = input()
34
>>> i
'34'
>>> i = input("Enter a number: ")
Enter a number: 45
>>> i
'45'
>>> 
>>> i + 10
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    i + 10
TypeError: can only concatenate str (not "int") to str
>>> type(i)
<class 'str'>
>>> int(i) + 10
55
>>> 
