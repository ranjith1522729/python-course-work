Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[]
l=list()
type(l)Type "help", "copyright", "credits" or "license()" for more information.
SyntaxError: invalid syntax
type(l)
<class 'list'>
l=[1,2,3.45,"str",True[1,2,4],{1,4,5},(1,2,3),{1:1,2:2,3:3},3+4j]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    l=[1,2,3.45,"str",True[1,2,4],{1,4,5},(1,2,3),{1:1,2:2,3:3},3+4j]
TypeError: 'bool' object is not subscriptable
l=[1,2,3.45,"str",True,[1,2,4],{1,4,5},(1,2,3),{1:1,2:2,3:3},3+4j]
l
[1, 2, 3.45, 'str', True, [1, 2, 4], {1, 4, 5}, (1, 2, 3), {1: 1, 2: 2, 3: 3}, (3+4j)]
l=[1,1,1,1]
l
[1, 1, 1, 1]
a=[11,2,3]
b=[4,5,7]
a+b
[11, 2, 3, 4, 5, 7]
a*3
[11, 2, 3, 11, 2, 3, 11, 2, 3]
a=[234,67,890,231,465,980]
a
[234, 67, 890, 231, 465, 980]
a[1]
67
a[5]
980
a[-2]
465
a[::-1]
[980, 465, 231, 890, 67, 234]
a[:-1:-4:-1]
SyntaxError: invalid syntax
a[:-1:-4:-1]
SyntaxError: invalid syntax
a[-1:-4:-1]
[980, 465, 231]
a[-1:-3:-1]
[980, 465]
[980, 465, 231]
a[-1:-3:-2]
SyntaxError: multiple statements found while compiling a single statement
KeyboardInterrupt
[980, 465, 231]
a[-2:-3:-2]
SyntaxError: multiple statements found while compiling a single statement
KeyboardInterrupt
[980, 465, 231]
a[-1:-2:-1]
SyntaxError: multiple statements found while compiling a single statement
a[1::2]
[67, 231, 980]
a
[234, 67, 890, 231, 465, 980]
67 in a
True
855 in a
False
980 not in a
False
a=[23,45,67,89,10,43]
max(a)
89
min(a)
10
sorted(a)
[10, 23, 43, 45, 67, 89]
len(a)
6
a
[23, 45, 67, 89, 10, 43]
id(a)
1617252494208
a[0]
23
a[0]=56
a
[56, 45, 67, 89, 10, 43]
a.append(45)
a
[56, 45, 67, 89, 10, 43, 45]
a.append(23)
a
[56, 45, 67, 89, 10, 43, 45, 23]
a
[56, 45, 67, 89, 10, 43, 45, 23]
a.insert(46)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a.insert(46)
TypeError: insert expected 2 arguments, got 1
a.insert(3,46)
a
[56, 45, 67, 46, 89, 10, 43, 45, 23]
a.extend([1,2,3,4])
a
[56, 45, 67, 46, 89, 10, 43, 45, 23, 1, 2, 3, 4]
a.pop(23)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a.pop(23)
IndexError: pop index out of range
a.pop(4)
89
a.pop(6)
45
a.remove(23)
a
[56, 45, 67, 46, 10, 43, 1, 2, 3, 4]
del a[1,3]
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    del a[1,3]
TypeError: list indices must be integers or slices, not tuple
del a[3]
a
[56, 45, 67, 10, 43, 1, 2, 3, 4]
a.clear()
a
[]
a
[]
a=[56, 45, 67, 10, 43, 1, 2, 3, 4]
a.index(67)
2
 a
 
SyntaxError: unexpected indent
a
[56, 45, 67, 10, 43, 1, 2, 3, 4]
a.count(40)
0
a=[1,2,3,4]
b=a
b
[1, 2, 3, 4]
b.append(7)
a
[1, 2, 3, 4, 7]
b
[1, 2, 3, 4, 7]
c=a.copy()
c.appemd(12)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    c.appemd(12)
AttributeError: 'list' object has no attribute 'appemd'. Did you mean: 'append'?
c.append(23)
a
[1, 2, 3, 4, 7]
>>> b
[1, 2, 3, 4, 7]
>>> c
[1, 2, 3, 4, 7, 23]
>>> any([1,'',False,[],(),{},set()])
True
>>> any([0,'',False,[],(),{},set()])
False
>>> all[1,2,34,45]
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    all[1,2,34,45]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> all[1,2,3,4]
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    all[1,2,3,4]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> a
[1, 2, 3, 4, 7]
>>> all[1,2,3,4]
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    all[1,2,3,4]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> a
[1, 2, 3, 4, 7]
>>> a=[56, 45, 67, 10, 43, 1, 2, 3, 4]
>>> a
[56, 45, 67, 10, 43, 1, 2, 3, 4]
>>> l.sort()
>>> l
[1, 1, 1, 1]
>>> a.sort()
>>> a
[1, 2, 3, 4, 10, 43, 45, 56, 67]
>>> a.reverse()
>>> a
[67, 56, 45, 43, 10, 4, 3, 2, 1]
