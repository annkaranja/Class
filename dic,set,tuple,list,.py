Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = (1,2,3,4,5)
>>> x
(1, 2, 3, 4, 5)
>>> x.append(6)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    x.append(6)
AttributeError: 'tuple' object has no attribute 'append'
>>> x.remove(5)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    x.remove(5)
AttributeError: 'tuple' object has no attribute 'remove'
>>> x.sort()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    x.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> x.pop()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x.pop()
AttributeError: 'tuple' object has no attribute 'pop'
>>> sum(x)
15
>>> max()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    max()
TypeError: max expected 1 arguments, got 0
>>> min()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    min()
TypeError: min expected 1 arguments, got 0
>>> min()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    min()
TypeError: min expected 1 arguments, got 0
>>> min(x)
1
>>> max(x)
5
>>> count(x)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    count(x)
NameError: name 'count' is not defined
>>> x.count
<built-in method count of tuple object at 0x01BFA180>
>>> x.count()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x.count()
TypeError: count() takes exactly one argument (0 given)
>>> count(x)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    count(x)
NameError: name 'count' is not defined
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> len()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    len()
TypeError: len() takes exactly one argument (0 given)
>>> len(x)
5
>>> for y in x:
	print(y*10)

	
10
20
30
40
50
>>> y=[6,7,8,9]
>>> y
[6, 7, 8, 9]
>>> z = y + z
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    z = y + z
NameError: name 'z' is not defined
>>> z = y + x
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    z = y + x
TypeError: can only concatenate list (not "tuple") to list
>>> z
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    z
NameError: name 'z' is not defined
>>> r = (6,7,8,9)
>>> r
(6, 7, 8, 9)
>>> z=r+x
>>> z
(6, 7, 8, 9, 1, 2, 3, 4, 5)
>>> z=x+y
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    z=x+y
TypeError: can only concatenate tuple (not "list") to tuple
>>> z=y+r
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    z=y+r
TypeError: can only concatenate list (not "tuple") to list
>>> 
>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 


>>> 
>>> 


>>> 

>>> 

>>> 
>>> 
>>> 5 in x
True
>>> 7 in x
False
>>> x*2
(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
>>> y*10
[6, 7, 8, 9, 6, 7, 8, 9, 6, 7, 8, 9, 6, 7, 8, 9, 6, 7, 8, 9, 6, 7, 8, 9, 6, 7, 8, 9, 6, 7, 8, 9, 6, 7, 8, 9, 6, 7, 8, 9]
>>> x.copy()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    x.copy()
AttributeError: 'tuple' object has no attribute 'copy'
>>> x=copy
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    x=copy
NameError: name 'copy' is not defined
>>> 
>>> 
>>> 

>>> 


>>> 
>>> 



>>> 
>>> 



>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 
>>> 
>>> 
>>> a=set([1,2,3,1,1,2,4,5,4])
>>> 
>>> a
{1, 2, 3, 4, 5}
>>> b={3,3,4,5,6,5,4,6,7}
>>> b
{3, 4, 5, 6, 7}
>>> a.add(6)
>>> a
{1, 2, 3, 4, 5, 6}
>>> b.add(8)
>>> b
{3, 4, 5, 6, 7, 8}
>>> b.remove(1)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    b.remove(1)
KeyError: 1
>>> aremove(1)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    aremove(1)
NameError: name 'aremove' is not defined
>>> a.remove(1)
>>> 
>>> a
{2, 3, 4, 5, 6}
>>> 
>>> 


>>> 

>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a.update({0,4})
>>> a
{0, 2, 3, 4, 5, 6}
>>> b.remove(1)
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    b.remove(1)
KeyError: 1
>>> b.discard(1)
>>> b
{3, 4, 5, 6, 7, 8}
>>> a.different(b)
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    a.different(b)
AttributeError: 'set' object has no attribute 'different'
>>> b.different(a)
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    b.different(a)
AttributeError: 'set' object has no attribute 'different'
>>> b.difference(a)
{8, 7}
>>> a.differenced(b)
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    a.differenced(b)
AttributeError: 'set' object has no attribute 'differenced'
>>> a.differenced(b)
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    a.differenced(b)
AttributeError: 'set' object has no attribute 'differenced'
>>> a.difference(b)
{0, 2}
>>> 
>>> 


>>> 

>>> 

>>> 


>>> 

>>> 



>>> 
>>> 



>>> 

>>> 



>>> 

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 

>>> 


>>> 
>>> 

>>> codes = {"kenya":254,"uganda":256,"tanzania":255}
>>> codes
{'kenya': 254, 'uganda': 256, 'tanzania': 255}
>>> codes["kenya"]
254
>>> codes["uganda"]
256
>>> codes["tanzania"]
255
>>> code{"rwanda"]=250
SyntaxError: invalid syntax
>>> code["rwanda"]=250
Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    code["rwanda"]=250
NameError: name 'code' is not defined
>>> 
>>> 

>>> 


>>> 

>>> 


>>> 
>>> 


>>> 

>>> 



>>> 

>>> 

>>> 

>>> 


>>> 

>>> 

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> codes["rwanda"]=250
>>> codes
{'kenya': 254, 'uganda': 256, 'tanzania': 255, 'rwanda': 250}
>>> "kenya" in codes
True
>>> "KENYA"
'KENYA'
>>> in codes
SyntaxError: invalid syntax
>>> "KENYA" in codes
False
>>> "uganda" in codes
True
>>> "UGANDA" in codes
False
>>> codes.pop("kenya")
254
>>> codes["burundi"]=234
>>> codes
{'uganda': 256, 'tanzania': 255, 'rwanda': 250, 'burundi': 234}
>>> codes
{'uganda': 256, 'tanzania': 255, 'rwanda': 250, 'burundi': 234}
>>> codes[kenya]=254
Traceback (most recent call last):
  File "<pyshell#202>", line 1, in <module>
    codes[kenya]=254
NameError: name 'kenya' is not defined
>>> codes["kenya"]=254
>>> codes
{'uganda': 256, 'tanzania': 255, 'rwanda': 250, 'burundi': 234, 'kenya': 254}
>>> types(codes)
Traceback (most recent call last):
  File "<pyshell#205>", line 1, in <module>
    types(codes)
NameError: name 'types' is not defined
>>> type(code)
Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    type(code)
NameError: name 'code' is not defined
>>> type(codes)
<class 'dict'>
>>> 
>>> 
>>> 



>>> 

>>> 

>>> 


>>> 

>>> 

>>> 

>>> 

>>> 

>>> 


>>> 
>>> 


>>> 


>>> 
>>> 


>>> 

>>> 
>>> squares = dict()
>>> squares
{}
>>> type(squares)
<class 'dict'>
>>> squares[1]=1
>>> squares[2]=4
>>> squares[3]=2
>>> squares[4]=3
>>> squares[5]=6
>>> squares[6]=5
>>> squares[7]=23
>>> squares[8]=7
>>> squares[9]=9
>>> squares[10]=100
>>> squares
{1: 1, 2: 4, 3: 2, 4: 3, 5: 6, 6: 5, 7: 23, 8: 7, 9: 9, 10: 100}
>>> cubes=dict()
>>> numbers=(0,10)
>>> for numbers in numbers:
	cubes[number]=number*number*number

	

>>> for number in numbers:
	cubes[number]=number*number*number

	

>>> for number in numbers:
	cubes[number] = number * number * number

	

>>> cubes
{}
>>> tens = range(0,10)
>>> tens
range(0, 10)
>>> for number in numbers:
	number * 10

	
Traceback (most recent call last):
  File "<pyshell#255>", line 1, in <module>
    for number in numbers:
TypeError: 'int' object is not iterable
>>> tens = range(0,10)
>>> range(0, 10)for number in numbers:
	number * 10
	
SyntaxError: invalid syntax
>>> 


>>> 



>>> 

>>> 



>>> 

>>> 
>>> 


>>> 


>>> 

>>> 


>>> 
>>> 
>>> 
>>> 
>>> tens = range(0,10)
>>> for number
SyntaxError: invalid syntax
>>> tens =(dict)
>>> numbers = (0,10)
>>> for number in numbers
SyntaxError: invalid syntax
>>> for number in numbers:
	number*10

	
0
100
>>> tens number=number*10
SyntaxError: invalid syntax
>>> tens [number]=number*10
Traceback (most recent call last):
  File "<pyshell#281>", line 1, in <module>
    tens [number]=number*10
TypeError: 'type' object does not support item assignment
>>> tens [number]=number*10
Traceback (most recent call last):
  File "<pyshell#282>", line 1, in <module>
    tens [number]=number*10
TypeError: 'type' object does not support item assignment
>>> 

>>> 


>>> 
>>> 


>>> 
>>> 


>>> 
>>> 


>>> 

>>> 

>>> 

>>> 

>>> 

>>> 


>>> 

>>> 

>>> 

>>> 

>>> 


>>> tens=(dict)
>>> numbers = (0,10)
>>> for number in numbers:
	tens[number]=number*10

	

>>> for number in numbers:
	tens[number]=number*10

	
Traceback (most recent call last):
  File "<pyshell#308>", line 2, in <module>
    tens[number]=number*10
TypeError: 'type' object does not support item assignment

>>> 
>>> 
>>> tens
<class 'dict'>
>>> 
>>> 
>>> numbers
(0, 10)

>>> 
>>> 
>>> tens=(dict)
>>> numbers = range(0,10)
>>> for number in numbers:
	tens[number]=number*10

	

>>> for number in numbers:
	tens[numbers]=number*10

	

>>> for number in numbers:
	tens[numbers]=number*10tens
	
SyntaxError: invalid syntax
>>> tens=dict()
>>> numbers = range(0,10)
>>> for number in numbers:
	tens[number]=number*10

	
>>> tens
{0: 0, 1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80, 9: 90}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> tens=dict()
>>> numbers = range(49,59)
>>> for number in numbers:
	tens[number]=number%3

	
>>> tens
{49: 1, 50: 2, 51: 0, 52: 1, 53: 2, 54: 0, 55: 1, 56: 2, 57: 0, 58: 1}
>>> 
