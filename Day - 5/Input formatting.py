Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#input formatting
#int float complex str list tuple set dict bool
a=input()
Ranjith kumar
a
'Ranjith kumar'
a=input()
a=4362
a
'a=4362'
a=input("enter the value:")
enter the value:43
a
'43'
a=input("enter the value:")
enter the value:rk@436
a
'rk@436'
marks=input("enter the marks:")
enter the marks:850
marks
'850'
price=float(input("enter the price"))
enter the price1499
price
1499.0
cgpa=flpat(iput("enter the cgpa:")
cgpa=float(iput("enter the cgpa:")
           
SyntaxError: invalid syntax. Perhaps you forgot a comma?
cgpa=float(input("enter the cgpa:")
           9.30
           
SyntaxError: '(' was never closed
cgpa=float(input("enter the cgpa:"))
           
enter the cgpa:8.90
cgpa
           
8.9
#split
           
#.Split list of strings
           
#.Spli0t & list of strings
           
name.split()
           
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    name.split()
NameError: name 'name' is not defined
names.split()
           
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    names.split()
NameError: name 'names' is not defined
names = ('RAnjith,games,ETS')
           
names.split()
           
['RAnjith,games,ETS']
names.split
           
<built-in method split of str object at 0x00000249AAD0A150>
0j884bb4mw97664>
           
SyntaxError: invalid imaginary literal
0x884bb4mw97664>
           
SyntaxError: invalid hexadecimal literal
0x0000020B1ECD7730>
           
SyntaxError: invalid syntax
names
           
'RAnjith,games,ETS'
names.split(',')
           
['RAnjith', 'games', 'ETS']
course='python,java,c++,flask'
           
course
           
'python,java,c++,flask'
course.split(',')
           
['python', 'java', 'c++', 'flask']
softskills = 'communication quicklearner'
           
softskills
           
'communication quicklearner'
softskills.split()
           
['communication', 'quicklearner']
sofyskills.split(',')
           
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    sofyskills.split(',')
NameError: name 'sofyskills' is not defined. Did you mean: 'softskills'?
softskills.split(',')
           
['communication quicklearner']
names=tuple(input("enter the names:").split())
           
enter the names:Ranjith Kumar Yaramothu
names
           
('Ranjith', 'Kumar', 'Yaramothu')
names = set(input("Enter the names:").split())
           
Enter the names:Ranjith Kumar Yaramothu
names
           
{'Ranjith', 'Kumar', 'Yaramothu'}
#list of integers
           
#Maps uses to iterate the vlue
           
#Float to replace the value
           
marks=value().split()
           
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    marks=value().split()
NameError: name 'value' is not defined. Did you mean: 'False'?
marks = value().split()
           
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    marks = value().split()
NameError: name 'value' is not defined. Did you mean: 'False'?
marks=('11,22,33,44,55')
           
marks
           
'11,22,33,44,55'
marks=input().split()
           
marks
11,4,32,56,78
           
(11, 4, 32, 56, 78)
marks
           
['marks']
map(int,marks)
           
<map object at 0x00000249AAE2E0E0>
list(map(int,marks))
           
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    list(map(int,marks))
ValueError: invalid literal for int() with base 10: 'marks'
list(map(int,marks))
           
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    list(map(int,marks))
ValueError: invalid literal for int() with base 10: 'marks'
marks=list(map(int,input("Enter the marks").split()))
           
Enter the marks22 33 44 55 66
marks
           
[22, 33, 44, 55, 66]
marks=tuple(map(int,input("Enter the marks").split()))
           
Enter the marks22 33 44 55 66
marks
           
(22, 33, 44, 55, 66)
marks
           
(22, 33, 44, 55, 66)
marks=set(map(float,input("Enter the marks").split()))
           
Enter the marks675839765
marks
           
{675839765.0}
marks=bool(map(float,input("Enter the marks").split()))
           
Enter the marks775 775 43 322
marks
           
True
marks=complex(map(float,input("Enter the marks").split()))
           
Enter the marks55 90 67 89
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    marks=complex(map(float,input("Enter the marks").split()))
TypeError: complex() first argument must be a string or a number, not 'map'
marks
           
True
#Packinng and unpacking
           
a,b=[1,2]
           
a
           
1
b
           
2
a,b,c=(1,12.3,"str")
           
a
           
1
b
           
12.3
c
           
'str'
email,password=input("Enter the email,password:").split()
           
Enter the email,password:Ranjith
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    email,password=input("Enter the email,password:").split()
ValueError: not enough values to unpack (expected 2, got 1)
email,password=input("Enter the email,password:").split()
           
Enter the email,password:ranjith@3456
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    email,password=input("Enter the email,password:").split()
ValueError: not enough values to unpack (expected 2, got 1)
KeyboardInterrupt
email,password=input("Enter the email,password:").split()
           
Enter the email,password:ranjith@1234 kumar345
email
           
'ranjith@1234'
password
           
'kumar345'
name,marks=input("Enter the name and marks:").split()
           
Enter the name and marks:ranjith 84
name
           
'ranjith'
marks
           
'84'

a,b,c=list(map(int,input().split()))
           

Traceback (most recent call last):
  File "<pyshell#86>", line 2, in <module>
    a,b,c=list(map(int,input().split()))
ValueError: not enough values to unpack (expected 3, got 0)
int(marks)
           
84

a,b,c=list(map(int,input().split()))
           
33 44 55 
a
           
33
b
           
44
c
           
55
#Eval function for the boolen value only
           
status=eval(input())
           
True
status
           
True
type(status)
           
<class 'bool'>
status=eval(input())
...            
2+7j
>>> status
...            
(2+7j)
>>> type(status)
...            
<class 'complex'>
>>> status=eval(input())
...            
400
>>> status
...            
400
>>> status=eval(input())
...            
[1,3,5,7]
>>> status
...            
[1, 3, 5, 7]
>>> status=eval(input())
...            
status=eval(input())
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    status=eval(input())
  File "<string>", line 1
    status=eval(input())
          ^
SyntaxError: invalid syntax
>>> status=eval(input())
...            
{1:1,2:2,3:3,4:4,5:5}
>>> status
...            
{1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
>>> type(status)
...            
<class 'dict'>
