Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # STRINGS
>>> 
>>> s = "python"
>>> 
>>> type(s)
<class 'str'>
>>> 
>>> # ------------------------------- immutability
>>> 
>>> s[0]
'p'
>>> s[1]
'y'
>>> s[0] = 'k'
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s[0] = 'k'
TypeError: 'str' object does not support item assignment
>>> 
>>> # ----------------------------------- subscripting
>>> 
>>> s = "computer"
>>> s[0]
'c'
>>> s[1]
'o'
>>> s[-1]
'r'
>>> s[-2]
'e'
>>> 
>>> 
>>> s[4:6]
'ut'
>>> s[3:5]
'pu'
>>> s[3:6]
'put'
>>> s[0:4]
'comp'
>>> s[:4]
'comp'
>>> 
>>> 
>>> s[5:8]
'ter'
>>> s[5:]
'ter'
>>> 
>>> 
>>> s[:]
'computer'
>>> 
>>> 
>>> s[1:7]
'ompute'
>>> s[1:7:2]
'opt'
>>> s[:]
'computer'
>>> s[::2]
'cmue'
>>> s[1::2]
'optr'
>>> 
>>> 
>>> s[::-1]
'retupmoc'
>>> 
>>> 
>>> # --------------------------------- operators
>>> 
>>> 'abc' + 'def'
'abcdef'
>>> 
>>> 'abc' * 3
'abcabcabc'
>>> 
>>> len(s)
8
>>> s
'computer'
>>> 'put' in s
True
>>> 'app' in s
False
>>> 
>>> type(s) == str
True
>>> type(s) == int
False
>>> isinstance(s, int)
False
>>> isinstance(s, str)
True
>>> 
>>> 
>>> del s
>>> s
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> 
>>> s = "python"
>>> s[:3] == 'pyt'
True
>>> s = 'computer'
>>> s
'computer'
>>> 
>>> 
>>> # ---------------------------------- string functions
>>> 
>>> # CAse related functions
>>> 
>>> s
'computer'
>>> s.upper()
'COMPUTER'
>>> s
'computer'
>>> s1 = s.upper()
>>> s
'computer'
>>> s`
SyntaxError: invalid syntax
>>> s1
'COMPUTER'
>>> 
>>> 
>>> s.lower()
'computer'
>>> s.capitalize()
'Computer'
>>> 
>>> 
>>> # checking the functions
>>> 
>>> # checking the strings
>>> 
>>> s = '123'
>>> int(s)
123
>>> s = '123a'
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: '123a'
>>> 
>>> '123'.isdigit()
True
>>> '123a'.isdigit()
False
>>> 
>>> '123a'.isalpha()
False
>>> 'abc'.isalpha()
True
>>> '123a'.isalnum()
True
>>> ' '.isspace()
True
>>> s
'123a'
>>> 
>>> s = "python"
>>> s.isupper()
False
>>> s.islower()
True
>>> s.istitle()
False
>>> m = 'This Is A Title'
>>> m.istitle()
True
>>> 
>>> site = "www.google.com"
>>> site.startswith('https')
False
>>> site.endswith('com')
True
>>> 
>>> 
>>> # ---------------- search with in strings
>>> s
'python'
>>> 
>>> 123.isdigit()
SyntaxError: invalid syntax
>>> '123'.isdigit()
True
>>> 'abd^%$'.isdigit()
False
>>> 'abc&^%'.isalnum()
False
>>> 
>>> # ----------------------
>>> 
>>> s
'python'
>>> 'th' in s
True
>>> s.find('th')
2
>>> s = 'mississippi'
>>> s.find('ss')
2
>>> 
>>> s.count('ss')
2
>>> s.count('s')
4
>>> 
>>> 
>>> # ------------------------------ string modification functions
>>> 
>>> ip = '127-1-1-1"
SyntaxError: EOL while scanning string literal
>>> ip = '127-1-1-1'
>>> newip = ip.replace('-', '.')
>>> newip
'127.1.1.1'
>>> ip
'127-1-1-1'
>>> 
>>> 
>>> 
>>> text = "mary had a little lamb"
>>> words = text.split()
>>> words
['mary', 'had', 'a', 'little', 'lamb']
>>> text.split('a')
['m', 'ry h', 'd ', ' little l', 'mb']
>>> 
>>> 
>>> 
>>> L = ['mary', 'had', 'a', 'little', 'lamb']['mary', 'had', 'a', 'little', 'lamb']
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    L = ['mary', 'had', 'a', 'little', 'lamb']['mary', 'had', 'a', 'little', 'lamb']
TypeError: list indices must be integers or slices, not tuple
>>> L = v
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    L = v
NameError: name 'v' is not defined
>>> L= ['mary', 'had', 'a', 'little', 'lamb']
>>> '-'.join(L)
'mary-had-a-little-lamb'
>>> 
>>> 
>>> 
>>> 
>>> s
'mississippi'
>>> s.ljust(30)
'mississippi                   '
>>> s.rjust(30, '>')
'>>>>>>>>>>>>>>>>>>>mississippi'
>>> 
>>> 
>>> 
>>> t = '    123.456  '
>>> t.strip()
'123.456'
>>> t.lstrip()
'123.456  '
>>> t.rstrip()
'    123.456'
>>> 
>>> 
>>> 
>>> # ----------------------------- string formatting
>>> 
>>> # format
>>> 
>>> 'My name is {} and age is {}'.format('Anil', 35')
				     
SyntaxError: EOL while scanning string literal
>>> 'My name is {} and age is {}'.format('Anil', 35)
'My name is Anil and age is 35'
>>> 'My name is {0} and age is {1}'.format('Anil', 35)
'My name is Anil and age is 35'
>>> 'My name is {1} and age is {0}'.format('Anil', 35)
'My name is 35 and age is Anil'
>>> 'My name is {0:20} and age is {1:10}'.format('Anil', 35)
'My name is Anil                 and age is         35'
>>> 'My name is {0:>20} and age is {1:<10}'.format('Anil', 35)
'My name is                 Anil and age is 35        '
>>> 'My name is {0:^20} and age is {1:^10}'.format('Anil', 35)
'My name is         Anil         and age is     35    '
>>> 
>>> 
>>> template = 'My name is {0:^20} and age is {1:^10}'
>>> template.format('Anil', 35)
'My name is         Anil         and age is     35    '
>>> template.format('Sunil', 36)
'My name is        Sunil         and age is     36    '
>>> 
>>> 
>>> # ----------------------------- advanced concept: translations
>>> 
>>> s = 'computer'
>>> # p -> pp, t -> tt
>>> tt = s.translate({'p':'pp', 't':'tt'})
>>> tt
'computer'
>>>  tt = s.maketrans({'p':'pp', 't':'tt'})
 
SyntaxError: unexpected indent
>>> tt = s.maketrans({'p':'pp', 't':'tt'})
>>> tt
{112: 'pp', 116: 'tt'}
>>> s.translate(tt)
'compputter'
>>> 
>>> 
>>> s1 = "concept"
>>> s1.translate(tt)
'concepptt'
>>> 
