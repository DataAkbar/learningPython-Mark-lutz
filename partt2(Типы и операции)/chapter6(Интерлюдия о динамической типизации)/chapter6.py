Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = 42
x = 'shubby'
x = 3.4564
x = [1, 2, 3]
a = 3
b = a
b
3
a = 'spam'
b
3
a
'spam'
a = a + 2
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a = a + 2
TypeError: can only concatenate str (not "int") to str
a = 3
b= a
a = a + 2
a
5
L1 = [2, 3, 4,]
L2 = L2
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    L2 = L2
NameError: name 'L2' is not defined. Did you mean: 'L1'?
L2 = L1
L1
[2, 3, 4]
L1 = 24
L1
24
L2
[2, 3, 4]
L1 = [2, 3, 4]
L2 = L1[:]
L1[0] = 24
L2
[2, 3, 4]
L1
[24, 3, 4]
import copy
X = copy.copy(Y)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    X = copy.copy(Y)
NameError: name 'Y' is not defined
L == M
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    L == M
NameError: name 'L' is not defined. Did you mean: 'L1'?
L = [1,2,3]
M = L
L ==M
True
L is M
True
L = [1, 2, 3]
M = [1,2,3,]
L = M
L = [1, 2, 3]
M = [1,2,3,]
L == m
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    L == m
NameError: name 'm' is not defined. Did you mean: 'M'?
L == M
True
L is M
False
import sys
sys.getrefcount(1)
805
A = 'spam;
SyntaxError: unterminated string literal (detected at line 1)
A = 'spam'
B = A
B = 'asdfadsf'
A
'spam'
A = ['spam']
B = A
B[0] = 'asdfasdf'
A
['asdfasdf']
A = ['spam']
B = A[:]
B[0] = 'asdfasf'
A
['spam']
B
['asdfasf']
