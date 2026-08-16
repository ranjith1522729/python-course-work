Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#mut ord het dyn unidu
d={}
type(d)
<class 'dict'>
d={1:2,3:4,5:5,8:9}
d
{1: 2, 3: 4, 5: 5, 8: 9}
d={}
d
{}
d[1]=1
d[13.4]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    d[13.4]
KeyError: 13.4
d[13.4]=1
d['str']=1
d[1,2,3,4]=1
d[2+8j]=1
d[True}=1
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
d[True]=1
d[[1,2,3,4]]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    d[[1,2,3,4]]
TypeError: unhashable type: 'list'
d[{2,3,4,5}]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    d[{2,3,4,5}]
TypeError: unhashable type: 'set'
d
{1: 1, 13.4: 1, 'str': 1, (1, 2, 3, 4): 1, (2+8j): 1}
d[False]=1
d
{1: 1, 13.4: 1, 'str': 1, (1, 2, 3, 4): 1, (2+8j): 1, False: 1}
d[1]=1
d[23.5]=1
d['str']=1
d[4,3,6,2]=1
d[2+6j]=1
d[1]=1
d
{1: 1, 13.4: 1, 'str': 1, (1, 2, 3, 4): 1, (2+8j): 1, False: 1, 23.5: 1, (4, 3, 6, 2): 1, (2+6j): 1}
d[1]=1
d[2]=23.4
d[3]='str'
d[4]=2+4j
d[5]=True
d[6]=1,2,3
d[7]='forzenset'
d[8]='none
SyntaxError: unterminated string literal (detected at line 1)
d[8]='none'
d[9]={1:2,3:4]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
d[9]={1:2,3:4}
d
{1: 1, 13.4: 1, 'str': 1, (1, 2, 3, 4): 1, (2+8j): 1, False: 1, 23.5: 1, (4, 3, 6, 2): 1, (2+6j): 1, 2: 23.4, 3: 'str', 4: (2+4j), 5: True, 6: (1, 2, 3), 7: 'forzenset', 8: 'none', 9: {1: 2, 3: 4}}
d={}
d[1]=2
d
{1: 2}
d[1]=3
d
{1: 3}
data
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    data
NameError: name 'data' is not defined
data={'name':'ranjith kumar','batch':'65','course':'pfs']
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
data={'name':'ranjith kumar','batch':'65','course':'pfs'}
data
{'name': 'ranjith kumar', 'batch': '65', 'course': 'pfs'}
data.get('name')
'ranjith kumar'
data.get('batch'0
         
SyntaxError: '(' was never closed
data.get('batch')
         
'65'
'course' in data
         
True
'batch' in data
         
True
'ranjith kumar' in data
         
False
data.get('age')
         
date.get('batch','key is not present')
         
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    date.get('batch','key is not present')
NameError: name 'date' is not defined. Did you mean: 'data'?
date.get('age','key is not present')
         
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    date.get('age','key is not present')
NameError: name 'date' is not defined. Did you mean: 'data'?
data
         
{'name': 'ranjith kumar', 'batch': '65', 'course': 'pfs'}

data['age']=12
         
data
         
{'name': 'ranjith kumar', 'batch': '65', 'course': 'pfs', 'age': 12}
data['phonum']=9876543210
         
data
         
{'name': 'ranjith kumar', 'batch': '65', 'course': 'pfs', 'age': 12, 'phonum': 9876543210}
dat.update({'email':'ranjith@gmail.com','py':2026})
         
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    dat.update({'email':'ranjith@gmail.com','py':2026})
NameError: name 'dat' is not defined. Did you mean: 'data'?
data.update({'email':'ranjith@gmail.com','py':2026})
         
data
         
{'name': 'ranjith kumar', 'batch': '65', 'course': 'pfs', 'age': 12, 'phonum': 9876543210, 'email': 'ranjith@gmail.com', 'py': 2026}
id(data)
         
1915466694272
data['py']
         
2026
data['py']=2027
         
data
         
{'name': 'ranjith kumar', 'batch': '65', 'course': 'pfs', 'age': 12, 'phonum': 9876543210, 'email': 'ranjith@gmail.com', 'py': 2027}
data['age']=22
         
id(data)
         
1915466694272
data.pop('course')
         
'pfs'
data
         
{'name': 'ranjith kumar', 'batch': '65', 'age': 22, 'phonum': 9876543210, 'email': 'ranjith@gmail.com', 'py': 2027}
data.pop(22)
         
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    data.pop(22)
KeyError: 22
data.pop('age')
         
22
data.clear()
         
data
         
{}
len(data)
         
0
data.keys()
         
dict_keys([])
data
         
{}
data={'name': 'ranjith kumar', 'batch': '65', 'age': 22, 'phonum': 9876543210, 'email': 'ranjith@gmail.com', 'py': 2027}
         
len(data)
         
6
data.keys()
         
dict_keys(['name', 'batch', 'age', 'phonum', 'email', 'py'])
data.values()
         
dict_values(['ranjith kumar', '65', 22, 9876543210, 'ranjith@gmail.com', 2027])
data.items()
         
dict_items([('name', 'ranjith kumar'), ('batch', '65'), ('age', 22), ('phonum', 9876543210), ('email', 'ranjith@gmail.com'), ('py', 2027)])
sorted(data)
         
['age', 'batch', 'email', 'name', 'phonum', 'py']
min(data)
         
'age'
max(data)
         
'py'
len(data)
         
6
d={1:1,2:2}
         
m=d
         
m
         
{1: 1, 2: 2}
d
         
{1: 1, 2: 2}
n=d.copy()
         
n[5]=5
         
n
         
{1: 1, 2: 2, 5: 5}
>>> d
...          
{1: 1, 2: 2}
>>> data
...          
{'name': 'ranjith kumar', 'batch': '65', 'age': 22, 'phonum': 9876543210, 'email': 'ranjith@gmail.com', 'py': 2027}
>>> dataget('py')
...          
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    dataget('py')
NameError: name 'dataget' is not defined
>>> data.get('py')
...          
2027
>>> data
...          
{'name': 'ranjith kumar', 'batch': '65', 'age': 22, 'phonum': 9876543210, 'email': 'ranjith@gmail.com', 'py': 2027}
>>> data.setdefault('name',2026)
...          
'ranjith kumar'
>>> data.setdefault('email',2026)
...          
'ranjith@gmail.com'
>>> data.setdefault('key',2026)
...          
2026
>>> data
...          
{'name': 'ranjith kumar', 'batch': '65', 'age': 22, 'phonum': 9876543210, 'email': 'ranjith@gmail.com', 'py': 2027, 'key': 2026}
>>>  dict.fromkeys9["python","mysqi","java"],0)
SyntaxError: unexpected indent
>>> dict.fromkeys9["python","mysqi","java"],0)
SyntaxError: unmatched ')'
>>> dict.fromkeys(["python","mysqi","java"],0)
{'python': 0, 'mysqi': 0, 'java': 0}
