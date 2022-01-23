Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a + 1, a - 1
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a + 1, a - 1
NameError: name 'a' is not defined
a = 3
a + 1, a - 1
(4, 2)
b = 4
b * 3, b / 2
(12, 2.0)
a % 2, b ** 2
(1, 16)
2 + 4.0, 2.0 ** b
(6.0, 16.0)
c * 2
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    c * 2
NameError: name 'c' is not defined
b / 2 + a
5.0
print(b / (2.0 + a))
0.8
b / (2.0 + a)
0.8
float(b / (2.0 + a))
0.8
print(b / (2.0 + a))
0.8
b / (2.0 + a)
0.8
1 / 2.0
0.5
num = 1 / 3.0
num
0.3333333333333333
print num
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print numSyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print (num)
0.3333333333333333
"%e" % num
'3.333333e-01'
'%4.2f' % num
'0.33'
num = 1/3
repr(num)
'0.3333333333333333'
str(num)
'0.3333333333333333'
1 < 2
True
2.0 >=1
True
2.0 == 2.0
True
2.0 != 2.0
False
X = 2
Y = 4
Z = 6
X < Y < Z
True
X < Y and Y< Z
True
X < Y > Z
False
X < Y and Y > Z
False
1 < 2 < 3.0 < 4
True
1 > 2 > 3.0 > 4
False
1 == 2 < 3
False
X / Y
0.5
X // Y
0
10 / 4
2.5
10 // 4
2
110 / 4.0
27.5
10 / 4.0
2.5
10 // 4.0
2.0
import math
math.floor(2.5)
2
math.floor(-2.5)
-3
math.trunc(2.5)
2
math.trunc(-2.5)
-2
5 / 2, 5 / -2
(2.5, -2.5)
5 // 2, 5 // -2
(2, -3)
5 / 2.0, 5 /-2.0
(2.5, -2.5)
5 // 2.0, 5 // -2.0
(2.0, -3.0)

999999999999999999999999999999 + 1
1000000000000000000000000000000
999999999999999999999999999999 + 1
1000000000000000000000000000000



2 ** 200
1606938044258990275541962092341162602522202993782792835301376


0o1, 0o20, 0o377
(1, 16, 255)
0x01, 0x10, 0xFF
(1, 16, 255)
0b1, 0b100000, 0b1111111
(1, 32, 127)
0b1, 0b10000, 0b1111111
(1, 16, 127)
0b1, 0b10000, 0b111111
(1, 16, 63)
0b1, 0b10000, 0b1111111
(1, 16, 127)
0b1, 0b10000, 0b11111111
(1, 16, 255)


oct(64), hex(64), bin(64)
('0o100', '0x40', '0b1000000')


def multiply(a, b):
    a * b

    
def multiply(a, b):
    return a * b


def multiply(a, b):
    self.a = a
    self.b = b
    a * b

    

multiply(4, 5)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    multiply(4, 5)
  File "<pyshell#81>", line 2, in multiply
    self.a = a
NameError: name 'self' is not defined
def multiply(a, b):
    return a * b

multiply(4, 5)
20
20
20





'hello'
'hello'
'hello'
'hello'
'hello' + 'hola'
'hellohola'
'hello' + dict('hola')
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    'hello' + dict('hola')
ValueError: dictionary update sequence element #0 has length 1; 2 is required
ValueError: dictionary update sequence element #0 has length 1; 2 is required
SyntaxError: invalid syntax
int(‘64’), int(‘100’, 8), int(‘40’, 16), int(‘1000000’, 2)
SyntaxError: invalid character '‘' (U+2018)
int('64'), int('100', 8), int('40', 16), int('1000000', 2)
(64, 64, 64, 64)
X = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFF
X
5192296858534827628530496329220095
oct(X)
'0o17777777777777777777777777777777777777'
hex(X)
'0xffffffffffffffffffffffffffff'
bit(X)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    bit(X)
NameError: name 'bit' is not defined. Did you mean: 'bin'?
bin(X)
'0b1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
x =1
x << 2
4
x | 2
3
x & 1
1
]
X = 0b0001
X << 2
4
bin(X << 2)
'0b100'
bin(X  2)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
bin(X | 0b010)
'0b11'
bin(X & 0b1)
'0b1'
X = 0xFF
bin(X)
'0b11111111'
X ^ 0b10101010
85
int('1010101',2)
85
hex(85)
'0x55'
X = 99
bin(X), X.bit_length()
('0b1100011', 7)
bin(256), (256).bit.length()
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    bin(256), (256).bit.length()
AttributeError: 'int' object has no attribute 'bit'
bin(256), (256).bit_length()
('0b100000000', 9)
len(bin(256)) - 2
9
import math
math.pi, math.e
(3.141592653589793, 2.718281828459045)
math.sin(2 * math.pi /180)
0.03489949670250097

math.sqrt(144), math.sqrt(2)
(12.0, 1.4142135623730951)
pow(2, 4), 2 ** 4
(16, 16)
abs (-42.0), sum((1,2,3,4))
(42.0, 10)
min(3,5,2,1), max(1,2,3,5,6)
(1, 6)


math.floor(2.567), math.floor(-2.567)
(2, -3)
math.trunc(2.567), math.trunc(-2.567)
(2, -2)


round(2.567), round(2.467), round(2.567, 2)
(3, 2, 2.57)


import math
math.sqrt(144)
12.0

144 ** .5
12.0
pow(144, .5)
12.0
import random
random.random()
0.7471166334605402
0.7471166334605402
0.7471166334605402
random.random()
0.09142457701487505
random.random()
0.10755875120162384
random.randint(1, 10)
1
random.randint(1, 10)
7
random.randint(1, 10)
4
random.randint(1, 10)
2
random.randint(1, 10)
3
random.randint(1, 10)
3
random.randint(1, 10)
6
random.choice(['live of america', "oltyGraidal', 'asdfasd'])
               
SyntaxError: unterminated string literal (detected at line 1)
random.choice(['live of america', "oltyGraidal", 'asdfasd'])
               
'asdfasd'

random.choice(['live of america', "oltyGraidal", 'asdfasd'])
               
'oltyGraidal'
random.choice(['live of america', "oltyGraidal", 'asdfasd'])
               
'asdfasd'
'oltyGraidal'
               
'oltyGraidal'
random.choice(['live of america', "oltyGraidal", 'asdfasd'])
               
'asdfasd'
random.choice(['live of america', "oltyGraidal", 'asdfasd'])
               
'asdfasd'
random.choice(['live of america', "oltyGraidal", 'asdfasd'])
               
'asdfasd'
random.choice(['live of america', "oltyGraidal", 'asdfasd'])
               
'oltyGraidal'
random.choice(['live of america', "oltyGraidal", 'asdfasd'])
               
'asdfasd'
random.choice(['live of america', "oltyGraidal", 'asdfasd'])
               
'asdfasd'
random.randint(0, 1)
               
1
random.randint(0, 1)
               
0
random.randint(0, 1)
               
1
random.randint(0, 1)
               
1
random.randint(0, 1)
               
0
random.randint(0, 1)
               
1
random.randint(0, 1)
               
0
random.randint(0, 1)
               
0
random.randint(0, 1)
               
0
random.randint(0, 1)
               
0
random.randint(0, 1)
               
0
random.randint(0, 1)
               
1
random.randint(0, 1)
               
1
random.randint(0, 1)
               
0
random.randint(0, 1)
               
1



 0.1 + 0.1 + 0.1 - 0.3
               
SyntaxError: unexpected indent
0.1 + 0.1 + 0.1 - 0.3
               
5.551115123125783e-17
0.1 + 0.1 + 0.1
               
0.30000000000000004
0.1 + 0.1 + 0.1 ** 2
               
0.21000000000000002
0.1 + 0.1 + 0.1 - 0.3
               
5.551115123125783e-17
from decimal import Decimal
               
Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
               
Decimal('0.0')
decimal.getcontext().prec = 2
               
Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    decimal.getcontext().prec = 2
NameError: name 'decimal' is not defined. Did you mean: 'Decimal'?
decimal.getcontext().prec = 2
               
Traceback (most recent call last):
  File "<pyshell#197>", line 1, in <module>
    decimal.getcontext().prec = 2
NameError: name 'decimal' is not defined. Did you mean: 'Decimal'?
Decimal.getcontext().prec = 2
               
Traceback (most recent call last):
  File "<pyshell#198>", line 1, in <module>
    Decimal.getcontext().prec = 2
AttributeError: type object 'decimal.Decimal' has no attribute 'getcontext'


import decimal
decimal.Decimal('1.00') / decimal.Decimal("3.00")
Decimal('0.3333333333333333333333333333')
1.00 / 3.00
0.3333333333333333

with decimal.localcontext() as ctx:
    ctx.prec = 2
    decimal.Decimal("1.00") / decimal.Decimal('3.00')

    
Decimal('0.33')
decimal.Decimal('1.00') / decimal.Decimal('3.00')
Decimal('0.3333333333333333333333333333')


from fractions import Franctions
Traceback (most recent call last):
  File "<pyshell#212>", line 1, in <module>
    from fractions import Franctions
ImportError: cannot import name 'Franctions' from 'fractions' (C:\Users\satipoff\AppData\Local\Programs\Python\Python310\lib\fractions.py)
from fractions import Fractions
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    from fractions import Fractions
ImportError: cannot import name 'Fractions' from 'fractions' (C:\Users\satipoff\AppData\Local\Programs\Python\Python310\lib\fractions.py)
from fractions import Fraction
x = Fraction(1,3)
y = Fraction(4,6)
x
Fraction(1, 3)
y
Fraction(2, 3)
print(y)
2/3
x + y
Fraction(1, 1)
x - y
Fraction(-1, 3)
x * y
Fraction(2, 9)
Fraction(1, 1)
Fraction(1, 1)


Fraction('.25')
Fraction(1, 4)
Fraction('1.25')
Fraction(5, 4)
Fraction('.25') + Fraction('1.25')
Fraction(3, 2)
a = 1 / 3.0
b = 4 / 6.0
a
0.3333333333333333
b
0.6666666666666666
a + b
1.0
a - b
-0.3333333333333333
a * b
0.2222222222222222


0.1 + 0.1 + 0.1 - 0.3
5.551115123125783e-17

from fractions import Fraction
Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10)
Fraction(0, 1)

from decimal import Decimal
Decimal('0.1') + Decimal("0.1") + Decimal('0.1') - Decimal('0.3')
Decimal('0.0')
1 / 4
0.25
1/3
0.3333333333333333
Fraction(1 , 3)
Fraction(1, 3)

import decimal
decimal.getcontext().prec = 2
decimal.Decimal(1) decimal.Decimal(3)
SyntaxError: invalid syntax
decimal.Decimal(1) / decimal.Decimal(3)
Decimal('0.33')
(2.5).as_integer_ratio()
(5, 2)

f = 2.5
z = Fraction(*f.as_integer_ratio())
z
Fraction(5, 2)
x
Fraction(1, 3)
x + z
Fraction(17, 6)
float(x)
0.3333333333333333

float(z)
2.5
float(x + z)
2.8333333333333335
x
Fraction(1, 3)
x + 2
Fraction(7, 3)
x + 2.0
2.3333333333333335
x + (1./3)
0.6666666666666666
x + (4./3)
1.6666666666666665


x + Fraction(4, 3)
Fraction(5, 3)
set([1,2,3,4])
{1, 2, 3, 4}
set('spam')
{'m', 's', 'p', 'a'}
set('spam')
{'m', 's', 'p', 'a'}
set('spam')
{'m', 's', 'p', 'a'}
set('spam')
{'m', 's', 'p', 'a'}
set('spam')
{'m', 's', 'p', 'a'}
set('spam')
{'m', 's', 'p', 'a'}
set('spam')
{'m', 's', 'p', 'a'}
set('spam')
{'m', 's', 'p', 'a'}
set('spam')
{'m', 's', 'p', 'a'}
set('spam')
{'m', 's', 'p', 'a'}
{'m', 's', 'p', 'a'}
{'m', 's', 'p', 'a'}
{'m', 's', 'p', 'a'}
{'m', 's', 'p', 'a'}
set('spam')
{'m', 's', 'p', 'a'}
set('spam')
{'m', 's', 'p', 'a'}
set('spam')
{'m', 's', 'p', 'a'}
set('spam')
{'m', 's', 'p', 'a'}
set('spam')
{'m', 's', 'p', 'a'}
set('spam')
{'m', 's', 'p', 'a'}

S = {'s', 'p', 'a', 'm'}
S.add('alot')

s
Traceback (most recent call last):
  File "<pyshell#295>", line 1, in <module>
    s
NameError: name 's' is not defined. Did you mean: 'S'?
S
{'a', 'alot', 's', 'm', 'p'}
S
{'a', 'alot', 's', 'm', 'p'}
S
{'a', 'alot', 's', 'm', 'p'}
S
{'a', 'alot', 's', 'm', 'p'}
S1 = {1,2,3,4}
S1 & {1, 3}
{1, 3}
{1, 5, 3, 6} | S1
{1, 2, 3, 4, 5, 6}
{7,4,7,1,3,4,5,1,3,} | S1
{1, 2, 3, 4, 5, 7}
S1 > {1,3}
True
S1 - {1,2,3,4}
set()
type({})
<class 'dict'>
S = set()
S.add(1.23)
S
{1.23}
{1,2,3} | {3,4}
{1, 2, 3, 4}
{1,2,3}.union({3,4})
{1, 2, 3, 4}
{1,2,3}.union(set([3,4]))
{1, 2, 3, 4}
{1,2,3}.intersection((1,3,5))
{1, 3}
{1,2,3}.issubset(range(-5, 5))
True
S
{1.23}
S.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#316>", line 1, in <module>
    S.add([1,2,3])
TypeError: unhashable type: 'list'
S.add({'a':1})
Traceback (most recent call last):
  File "<pyshell#317>", line 1, in <module>
    S.add({'a':1})
TypeError: unhashable type: 'dict'
S.add((1,2,3,))
S
{1.23, (1, 2, 3)}
S | {(4,5,6),(1,2,3)}
{1.23, (1, 2, 3), (4, 5, 6)}
(1,4,3) in S
False
{x ** 2 for x in [1,2,3,4]}
{16, 1, 4, 9}
{x for x in 'stap'}
{'s', 'p', 't', 'a'}
{c * 4 for c in 'spam'}
{'pppp', 'aaaa', 'mmmm', 'ssss'}
S = {c * 4 for c in 'spam'}
S | {'mmmm', 'xxxx'}
{'pppp', 'aaaa', 'mmmm', 'xxxx', 'ssss'}
S & {'mmmm', 'xxxx'}
{'mmmm'}
L
Traceback (most recent call last):
  File "<pyshell#328>", line 1, in <module>
    L
NameError: name 'L' is not defined
L = [1,2,1,3,2,4,5]
set{L}
SyntaxError: invalid syntax
set(L)
{1, 2, 3, 4, 5}
L = list(set(L))

L
[1, 2, 3, 4, 5]


engineers = {'bob', 'sue', 'ann', 'vic'}
managers = {'tom', sue}
Traceback (most recent call last):
  File "<pyshell#338>", line 1, in <module>
    managers = {'tom', sue}
NameError: name 'sue' is not defined. Did you mean: 'sum'?
managers = {'tom', 'sue'}
               
'bob' in engineers
               
True
engineers & managers
               
{'sue'}
engineers | managers
               
{'ann', 'tom', 'bob', 'sue', 'vic'}
engineers - managers
               
{'vic', 'ann', 'bob'}
managers - engineers
               
{'tom'}
engineers > managers
               
False
{'bob', 'sue'} < engineers
               
True
(managers | engineers)> managers
               
True
managers ^ engineers
               
{'tom', 'bob', 'vic', 'ann'}
(managers | engineers) - ( managers ^ engineers )
               
{'sue'}
type(True)
               
<class 'bool'>
isinstance(True, int)
               
True


True == 1
               
True
True is 1
               
False
True or False
               
True
True or False
               
True
True or False
               
True
True or False
               
True
True or False
               
True
True + 4
               
5
