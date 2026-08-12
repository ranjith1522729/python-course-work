Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#strip
s = '      hello      world         '
s.strip()
'hello      world'
s.lstrip()
'hello      world         '
s.rstrip()
'      hello      world'
s.replace('','')
'      hello      world         '
s.replace(' ','')
'helloworld'
#split and joining method
 s='java-python-mysql-flask-c'
 
SyntaxError: unexpected indent
s='java-python-mysql-flask-c'
s.split('-')
['java', 'python', 'mysql', 'flask', 'c']
s.split('-',2)
['java', 'python', 'mysql-flask-c']
s.rsplit('-',2)
['java-python-mysql', 'flask', 'c']
l='''python'''
l='''python
java
mysql
flask
'''
l
'python\njava\nmysql\nflask\n'
l.splitlines()
['python', 'java', 'mysql', 'flask']
s=['python','java','mysql','flask']
c
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    c
NameError: name 'c' is not defined
s
['python', 'java', 'mysql', 'flask']
#join
''.join(s)
'pythonjavamysqlflask'
' '.join(s)
'python java mysql flask'
', '.join(s)
'python, java, mysql, flask'
'@'.join(s)
'python@java@mysql@flask'
'-'.join(s)
'python-java-mysql-flask'
'-'.join({'1','2','3'})
'1-2-3'
'-'.join({'1','2','3'})
'1-2-3'
a='strings.py
SyntaxError: unterminated string literal (detected at line 1)
a='strings.py'
#partition
a.partition('.')
('strings', '.', 'py')
a='string.py.java.png.txt'
s
['python', 'java', 'mysql', 'flask']
a
'string.py.java.png.txt'
a.partition('.')
('string', '.', 'py.java.png.txt')
a.rpartition('.')
('string.py.java.png', '.', 'txt')
#startwith
a='strings.png'
a.startwith('str')
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a.startwith('str')
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
a.startswith('str')
True
a.stratswith('list')
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a.stratswith('list')
AttributeError: 'str' object has no attribute 'stratswith'. Did you mean: 'startswith'?
a.startswith('list')
False
a.startswith('py')
False
a.endswith('.py')
False
a.endwith('.phg')
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.endwith('.phg')
AttributeError: 'str' object has no attribute 'endwith'. Did you mean: 'endswith'?
a.endwith('.png')
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.endwith('.png')
AttributeError: 'str' object has no attribute 'endwith'. Did you mean: 'endswith'?
a.endswith('.png')
True
'pythonv.13'.islower()
True
'pythonv.1234'.islower()
True
'pythonv!@#$%'.isupper()
False
'PYTHON1234'.isupper()
True
>>> #alpha
>>> 'estyu'.isalpha()
True
>>> 'estyu@234.isalpha()
SyntaxError: unterminated string literal (detected at line 1)
>>> 'estyu@234'.isalpha()
False
>>> 'serdtfhyyevg'.isalnum()
True
>>> 'jcndheund ch'.isalnum()
False
>>> '      '.isspace()
True
>>> '   hello  '.isspace()
False
>>> 'hell'.istitle()
False
>>> 'hlo wor'.istitle()
False
>>> 'my_var'.isidentifier()
True
>>> 'my@var'.isidentifier()
False
>>> a.partition('.')
('strings', '.', 'png')
>>> '2334567'.isdecimal()
True
>>> 'ENDHUBBUEJ1234'.isdecimal()
False
>>> '45678'.isdigit()
True
>>> '4563'.isnumerics()
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    '4563'.isnumerics()
AttributeError: 'str' object has no attribute 'isnumerics'. Did you mean: 'isnumeric'?
>>> '4563'.isnumeric()
True
