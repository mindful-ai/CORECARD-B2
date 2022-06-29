Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # DICTIONARIES
>>> 
>>> L = ["Anil", 35, "Corecard", "1500000", "Bhopal", "India"]
>>> L[0]
'Anil'
>>> L[3]
'1500000'
>>> L[4]
'Bhopal'
>>> L[4] + L[5]
'BhopalIndia'
>>> 
>>> D = {"name":"Anil", "age":35, "company":"Corecard"}
>>> type(D)
<class 'dict'>
>>> 
>>> 
>>> D
{'name': 'Anil', 'age': 35, 'company': 'Corecard'}
>>> D['salary'] = "1500000"
>>> D
{'name': 'Anil', 'age': 35, 'company': 'Corecard', 'salary': '1500000'}
>>> D['name'] = "Sunil"
>>> D
{'name': 'Sunil', 'age': 35, 'company': 'Corecard', 'salary': '1500000'}
>>> D['addr']
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    D['addr']
KeyError: 'addr'
>>> D['addr'] = "Bhopal, India"
>>> D
{'name': 'Sunil', 'age': 35, 'company': 'Corecard', 'salary': '1500000', 'addr': 'Bhopal, India'}
>>> D.pop("age")
35
>>> D
{'name': 'Sunil', 'company': 'Corecard', 'salary': '1500000', 'addr': 'Bhopal, India'}
>>> 
>>> D.update({'phone':'3847592823', 'hobbies':['criket', 'music']})
>>> D
{'name': 'Sunil', 'company': 'Corecard', 'salary': '1500000', 'addr': 'Bhopal, India', 'phone': '3847592823', 'hobbies': ['criket', 'music']}
>>> 
>>> 
>>> 
>>> D.keys()
dict_keys(['name', 'company', 'salary', 'addr', 'phone', 'hobbies'])
>>> D.values()
dict_values(['Sunil', 'Corecard', '1500000', 'Bhopal, India', '3847592823', ['criket', 'music']])
>>> D.items()
dict_items([('name', 'Sunil'), ('company', 'Corecard'), ('salary', '1500000'), ('addr', 'Bhopal, India'), ('phone', '3847592823'), ('hobbies', ['criket', 'music'])])
>>> 
