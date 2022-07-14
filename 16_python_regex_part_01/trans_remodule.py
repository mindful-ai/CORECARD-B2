Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "This line 6.784 consists of 8.334 floating point numbers"
>>> p = r"\d+\.\d+"
>>> import re
>>> re.match(p, text)
>>> re.search(p, text)
<re.Match object; span=(10, 15), match='6.784'>
>>> text[10:15]
'6.784'
>>> re.findall(p, text)
['6.784', '8.334']
>>> for m in finditer(p, text):
	print(m.group(), ' --> ', m.span())

	
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    for m in finditer(p, text):
NameError: name 'finditer' is not defined
>>> for m in re.finditer(p, text):
	print(m.group(), ' --> ', m.span())

	
6.784  -->  (10, 15)
8.334  -->  (28, 33)
>>> m = re.search(p, text)
>>> m.group()
'6.784'
>>> m.span()
(10, 15)
>>> m.start()
10
>>> m.end()
15
>>> re.sub('line', 'statement', text)
'This statement 6.784 consists of 8.334 floating point numbers'
>>> 
>>> 
>>> p = r"(\d+)\.(\d+)"
>>> m = re.search(p, text)
>>> m.group()
'6.784'
>>> m.groups()
('6', '784')
>>> 
>>> 
>>> p = r"(?P<integer>\d+)\.(?P<decimal>\d+)"
>>> m = re.search(p, text)
>>> m.group()
'6.784'
>>> m.groups()
('6', '784')
>>> m.groupdict()
{'integer': '6', 'decimal': '784'}
>>> 
