Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#data types
#int float complex
a =12

type(a)
<class 'int'>
b =12.6
type(b)
<class 'float'>
c = 14+3j
type(c)
<class 'complex'>
c 23+5J
SyntaxError: invalid syntax
c = 34+2J
c
(34+2j)
# str list tuple
a = 'Ranjith'
id(s)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    id(s)
NameError: name 's' is not defined
id(a)
2192753978480
s += 'kumar'
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s += 'kumar'
NameError: name 's' is not defined
l = [1,2,3,5]
type(l)
<class 'list'>
id(l)
2192743833472
1.append(12)
SyntaxError: invalid decimal literal
l.append(12)
l
[1, 2, 3, 5, 12]
id(l)
2192743833472
l = [1,23.4,"str",[1.45]]
l
[1, 23.4, 'str', [1.45]]
type(l)
<class 'list'>
t = (1,4,6,78)
type(t)
<class 'tuple'>
t
(1, 4, 6, 78)
t = (2,2,2,2)
t
(2, 2, 2, 2)
s = {34,56,78,34,67,23,66,}
s
{34, 67, 66, 23, 56, 78}
id(S)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    id(S)
NameError: name 'S' is not defined. Did you mean: 's'?
type(s)
<class 'set'>
id(s)
2192752360608
s.add(20)
s
{34, 67, 66, 20, 23, 56, 78}
id(s)
2192752360608
a ={1,2,4.55,"str}
    
SyntaxError: unterminated string literal (detected at line 1)
a ={1,2,4.55,"str"}
    
a
    
{1, 2, 4.55, 'str'}
set(s)
    
{34, 67, 66, 20, 23, 56, 78}
type(s)
    
<class 'set'>
d = {"productname':'xyz','price':456}
     
SyntaxError: unterminated string literal (detected at line 1)
d = {'productname':'xyz','price':456}
     
d
     
{'productname': 'xyz', 'price': 456}
s={1,2,4,5}
     
s = frozenset({2,2,4,4,87,45})
     
s
     
frozenset({2, 4, 45, 87})
a =ture
...      
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a =ture
NameError: name 'ture' is not defined. Did you mean: 'tuple'?
>>> a =Ture
...      
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a =Ture
NameError: name 'Ture' is not defined
>>> type(S)
...      
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    type(S)
NameError: name 'S' is not defined. Did you mean: 's'?
>>> a =True
...      
>>> b =False
...      
>>> type(a)
...      
<class 'bool'>
>>> a={}
...      
>>> l={}
...      
>>> t={}
...      
>>> s=''
...      
>>> s = None
...      
>>> s
...      
>>> type(s)
...      
<class 'NoneType'>
