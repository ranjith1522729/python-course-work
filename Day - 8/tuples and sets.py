Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
t=()
t=tuple()
t=1,4,3,6,
t
(1, 4, 3, 6)
t=(1)
t
1
t=(1,@)
SyntaxError: invalid syntax
t=(1,2)
t
(1, 2)
y(1,1,1,1,1)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    y(1,1,1,1,1)
NameError: name 'y' is not defined
t=(1,1,1,1,1)
t
(1, 1, 1, 1, 1)
t=(1,24.3,"str",[1,2,3],(4,3,6),{45,34,23},{1:@,2:!},True)
SyntaxError: invalid syntax
t=(1,24.3,"str",[1,2,3],(4,3,6),{45,34,23},{1:2,2:1},True)
t
(1, 24.3, 'str', [1, 2, 3], (4, 3, 6), {34, 45, 23}, {1: 2, 2: 1}, True)
type(t)
<class 'tuple'>
 (1,2,3)+(4,5,6)
 
SyntaxError: unexpected indent
(1,2,3)+(4,5,6)
(1, 2, 3, 4, 5, 6)
(1,2,3)*4
(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
t
(1, 24.3, 'str', [1, 2, 3], (4, 3, 6), {34, 45, 23}, {1: 2, 2: 1}, True)
t[1]
24.3
t[4]
(4, 3, 6)
t[-4]
(4, 3, 6)
t
(1, 24.3, 'str', [1, 2, 3], (4, 3, 6), {34, 45, 23}, {1: 2, 2: 1}, True)
t[3:6]
([1, 2, 3], (4, 3, 6), {34, 45, 23})
t[-1:-3;-1]
SyntaxError: invalid syntax
t[-1:-3:-1]
(True, {1: 2, 2: 1})
t[-1:-4:-1]
(True, {1: 2, 2: 1}, {34, 45, 23})
t[-2:-5:-1]
({1: 2, 2: 1}, {34, 45, 23}, (4, 3, 6))
t
(1, 24.3, 'str', [1, 2, 3], (4, 3, 6), {34, 45, 23}, {1: 2, 2: 1}, True)
23 in t
False
'str' in t
True
2 in t
False
1 in t
True
 t=(1,2,34,56,78,9123,4567,345,678,4362)
 
SyntaxError: unexpected indent
t=(1,2,34,56,78,9123,4567,345,678,4362)
t
(1, 2, 34, 56, 78, 9123, 4567, 345, 678, 4362)
sorted(t)
[1, 2, 34, 56, 78, 345, 678, 4362, 4567, 9123]
min(t)
1
max(t)
9123
len(t)
10
sum(t)
19246
t.index(34)
2
t.count(78)
1
del (2)
SyntaxError: cannot delete literal
all(1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    all(1,2,3,4,5)
TypeError: all() takes exactly one argument (5 given)
all((1,2,3,4,5))
True
any((1,2,3,4,00,09))
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
any((1,2,3,4,00,9))
True
all(1,2,0,3,00)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    all(1,2,0,3,00)
TypeError: all() takes exactly one argument (5 given)
all((1,2,0,3,00))
False
t
(1, 2, 34, 56, 78, 9123, 4567, 345, 678, 4362)
t[3]
56
t[3].append(3)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    t[3].append(3)
AttributeError: 'int' object has no attribute 'append'
append(5)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    append(5)
NameError: name 'append' is not defined
t=(1,2,3,4)
t
(1, 2, 3, 4)
t(3).append(5)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    t(3).append(5)
TypeError: 'tuple' object is not callable
t(3)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    t(3)
TypeError: 'tuple' object is not callable
t
(1, 2, 3, 4)
t(2)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    t(2)
TypeError: 'tuple' object is not callable
#set
s=set()
type(s)
<class 'set'>
S={1,2,3,4,55,6,78,34566,3345,5678}
s
set()
s
set()
s={1,2,3,1,2,3}
s
{1, 2, 3}
s=set()
s.add(12)
a.add(23.4)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a.add(23.4)
NameError: name 'a' is not defined
s.add(23.4)
s.add("str")
s.add(t)
a.add(tuple)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    a.add(tuple)
NameError: name 'a' is not defined
s.add({1:1})
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    s.add({1:1})
TypeError: unhashable type: 'dict'
s.add(False)
s
{False, 'str', 12, (1, 2, 3, 4), 23.4}
a={1,2,3,4,5}
b={2,5,6,7,8}
2 in a
True
10 not in a
True
a|b
{1, 2, 3, 4, 5, 6, 7, 8}
a&b
{2, 5}
a-b
{1, 3, 4}
b-a
{8, 6, 7}
a^b
{1, 3, 4, 6, 7, 8}
a={1,2,3,4,6,7,9}
a
{1, 2, 3, 4, 6, 7, 9}
{1}<=a
True
{4}<=a
True
{6}<=a
True
{5}<=a
False
a>={3}
True
a.={8}
SyntaxError: invalid syntax
a>={3}
True
x={1,3,5,7}
y={4,3,6,2}
n.isdisjoint(m)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    n.isdisjoint(m)
NameError: name 'n' is not defined
x.isdisjoint(m)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    x.isdisjoint(m)
NameError: name 'm' is not defined
x.isdisjoint(y)
False
a.isdisjoint(b)
False
a={12,34,56,78,90,123,4362}
a
{34, 90, 56, 4362, 123, 12, 78}
sorted(a)
[12, 34, 56, 78, 90, 123, 4362]
min(a)
12
max(a)
4362
len(a)
7
sum(a)
4755
a.index(a)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    a.index(a)
AttributeError: 'set' object has no attribute 'index'
all({1,2,3,43,43,12})
True
any({,10})
SyntaxError: invalid syntax
any({1,10})
True
a
{34, 90, 56, 4362, 123, 12, 78}
a={1,2,3}
a
{1, 2, 3}
d=a
d.add(4)
d
{1, 2, 3, 4}
c=a.copy()
c
{1, 2, 3, 4}
>>> c.add(5)
>>> c
{1, 2, 3, 4, 5}
>>> c.add(70)
>>> c
{1, 2, 3, 4, 5, 70}
>>> c.add(45)
>>> c
{1, 2, 3, 4, 5, 70, 45}
>>> c.update(34)
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    c.update(34)
TypeError: 'int' object is not iterable
>>> c.update(70,34)
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    c.update(70,34)
TypeError: 'int' object is not iterable
>>> a.pop()
1
>>> a.pop()
2
>>> a.remove(3)
>>> a
{4}
>>> c
{1, 2, 3, 4, 5, 70, 45}
>>> a.discard(3)
>>> c
{1, 2, 3, 4, 5, 70, 45}
>>> a.clear()
>>> c
{1, 2, 3, 4, 5, 70, 45}
>>> a
set()
>>> a=frozenset({1,2,3,4})
>>> a
frozenset({1, 2, 3, 4})
