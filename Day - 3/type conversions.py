Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 10
float(a)
10.0
str(a)
'10'
complex(a)
(10+0j)
bool(a)
True
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
se(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    se(a)
NameError: name 'se' is not defined. Did you mean: 'set'?
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
float = 24.0
int(f)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    int(f)
NameError: name 'f' is not defined
float =12

int(f)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    int(f)
NameError: name 'f' is not defined
str(f)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    str(f)
NameError: name 'f' is not defined
f = 23
int(f)
23
str(f)
'23'
complex(f)
(23+0j)
bool(f)
True
list(f)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    list(f)
TypeError: 'int' object is not iterable
tuple(f)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    tuple(f)
TypeError: 'int' object is not iterable
set(f)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    set(f)
TypeError: 'int' object is not iterable
dict(f)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    dict(f)
TypeError: 'int' object is not iterable
c = 10+4j
int(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
str(c)
'(10+4j)'
float(c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    float(c)
TypeError: 'int' object is not callable
bool(c)
True
list(c)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
l = [1,2,3,4,5]
int(l)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
Str(l)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    Str(l)
NameError: name 'Str' is not defined. Did you mean: 'str'?
tuple(l)
(1, 2, 3, 4, 5)
set(l)
{1, 2, 3, 4, 5}
dict(l)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
str(l)
'[1, 2, 3, 4, 5]'
t = [2,4,6,7,]
int(t)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
str(t)
'[2, 4, 6, 7]'
float(t)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    float(t)
TypeError: 'int' object is not callable
list(t)
[2, 4, 6, 7]
set(t)
{2, 4, 6, 7}
dict(t)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> s = [2,3,44,5,2,66,3]
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
>>> str(s)
'[2, 3, 44, 5, 2, 66, 3]'
>>> complex(s)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    complex(s)
TypeError: complex() first argument must be a string or a number, not 'list'
>>> list(s)
[2, 3, 44, 5, 2, 66, 3]
>>> tuple(s)
(2, 3, 44, 5, 2, 66, 3)
>>> dict(s)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    dict(s)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(s)
True
>>> d = {2:3,4:4,66:43}
>>> int(d)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
>>> str(d)
'{2: 3, 4: 4, 66: 43}'
>>> float(d)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    float(d)
TypeError: 'int' object is not callable
>>> bool(d)
True
>>> list(d)
[2, 4, 66]
>>> tuple(d)
(2, 4, 66)
>>> set(d)
{2, 4, 66}
