Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s 'Ranjith kumar'
SyntaxError: invalid syntax
s='Ranjith kumar'
s
'Ranjith kumar'
type(s)
<class 'str'>
s=''
s
''
a='Ranjith'
b='Kumar'
a+b
'RanjithKumar'
fname='Ranjit'
lname='Kumar'
fname+lname
'RanjitKumar'
a='Ranjith'
a
'Ranjith'
a*10
'RanjithRanjithRanjithRanjithRanjithRanjithRanjithRanjithRanjithRanjith'
'ranjithkumar'*5
'ranjithkumarranjithkumarranjithkumarranjithkumarranjithkumar'
'--ranjith--'*5
'--ranjith----ranjith----ranjith----ranjith----ranjith--'
name='Ranjith Kumar Yaramothu'
names
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    names
NameError: name 'names' is not defined. Did you mean: 'name'?
name
'Ranjith Kumar Yaramothu'
s[6]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s[6]
IndexError: string index out of range
name[6]
'h'
name[9]
'u'
name[16]
'r'
name[-5]
'm'
name
'Ranjith Kumar Yaramothu'
name[:8]
'Ranjith '
name[:14]
'Ranjith Kumar '
name[:19]
'Ranjith Kumar Yaram'
name[-9]
'Y'
name[:-9]
'Ranjith Kumar '
name[::-1]
'uhtomaraY ramuK htijnaR'
name[:18]
'Ranjith Kumar Yara'
name[:23]
'Ranjith Kumar Yaramothu'
name[:1 :9 :1]
SyntaxError: invalid syntax
'ranjith' in name
False
'Ranjith' in name
True
name
'Ranjith Kumar Yaramothu'
len(name)
23
ord('r')
114
ord('j')
106
chr(98)
'b'
chr(108)
'l'
chr('117')
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    chr('117')
TypeError: 'str' object cannot be interpreted as an integer
chr('99')
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    chr('99')
TypeError: 'str' object cannot be interpreted as an integer
chr(9)
'\t'
chr(6)
'\x06'
sorted(names)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    sorted(names)
NameError: name 'names' is not defined. Did you mean: 'name'?
sorted(name)
[' ', ' ', 'K', 'R', 'Y', 'a', 'a', 'a', 'a', 'h', 'h', 'i', 'j', 'm', 'm', 'n', 'o', 'r', 'r', 't', 't', 'u', 'u']
max('names')
's'
min('names')
'a'
#case conversions
s='ranjith Kumar Yaramothu'
s.upper()
'RANJITH KUMAR YARAMOTHU'
s.lower()
'ranjith kumar yaramothu'
s.capitalize()
'Ranjith kumar yaramothu'
s.title()
'Ranjith Kumar Yaramothu'
s.casefold()
'ranjith kumar yaramothu'
s
'ranjith Kumar Yaramothu'
s.center(40,'-')
'--------ranjith Kumar Yaramothu---------'
s.center(45,'*')
'***********ranjith Kumar Yaramothu***********'
s.ljust(38'-')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
s.ljust(38,'-')
'ranjith Kumar Yaramothu---------------'
s.rjust(30,'_')
'_______ranjith Kumar Yaramothu'
'123'.zfill(4)
'0123'
'3478'.zfill(7)
'0003478'
23.zfill(1)
SyntaxError: invalid decimal literal
'23'.zfill(1)
'23'
'6798'.zfill(5)
'06798'
#search&finding methods
s
'ranjith Kumar Yaramothu'
s.find('h')
6
s.find('k')
-1
>>> s.find('K')
8
>>> s.rfind('R')
-1
>>> s.rfind('u')
22
>>> s.rindex('h')
21
>>> s.index('u')
9
>>> s.count('a')
4
>>> s.rcount('n')
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    s.rcount('n')
AttributeError: 'str' object has no attribute 'rcount'. Did you mean: 'count'?
>>> s.count('m')
2
>>> #replace
>>> s
'ranjith Kumar Yaramothu'
>>> s.replace('u','6')
'ranjith K6mar Yaramoth6'
>>> s.replace('ranjith','Ranjith')
'Ranjith Kumar Yaramothu'
>>> s.maketrans('aeiou','#@$%&')
{97: 35, 101: 64, 105: 36, 111: 37, 117: 38}
>>> s.translate(s.maketrans('aeiou','#@$%&'))
'r#nj$th K&m#r Y#r#m%th&'
>>> text="hello world"
>>> text.encode()
b'hello world'
>>> text="Hello 😊"
>>> text.encode()
b'Hello \xf0\x9f\x98\x8a'
>>> b'Hello \xf0\x9f\x98\x8a'.decode()
'Hello 😊'
