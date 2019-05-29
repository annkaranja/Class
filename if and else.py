Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=range(0,10)
>>> for a in x:
	if a % 3 ==0:
		print("{} is divisible by 3 ".format(a))
	else:
		print(" {} is not divisible by 3 ".format(a))

		
0 is divisible by 3 
 1 is not divisible by 3 
 2 is not divisible by 3 
3 is divisible by 3 
 4 is not divisible by 3 
 5 is not divisible by 3 
6 is divisible by 3 
 7 is not divisible by 3 
 8 is not divisible by 3 
9 is divisible by 3 
>>> x = range(0,20)
>>> for a in x:
	if a % 3 ==0:
		print("{} is divisible by 3 ".format(a))
        elif a % 5 == 0:
              print("{} is divisible by 5 ".format(a))  
	else:
		print(" {} is not divisible by 3 or 5".format(a))
		
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for a in x:
	if a % 3 ==0:
	       print("{} is divisible by 3 ".format(a))
        elif a % 5 == 0:
               print("{} is divisible by 5 ".format(a))
	else:
	       print(" {} is not divisible by 3 or 5".format(a))
	       
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
>>> 
>>> 
>>> 
>>> for a in x:
	if a % 3 ==0:
	       print("{} is divisible by 3 ".format(a))
        elif a % 5 == 0:
               print("{} is divisible by 5 ".format(a))
	else:
	       print(" {} is not divisible by 3 or 5".format(a
							     
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for a in x:
	if a % 3 == 0:
							     print("{} is divisible by 3 ".format(a))
	elif a % 5 == 0:
							     print("{} is divisible by 5 ".format(a))
	else:
							     print(" {} is not divisible by 3 or 5".format(a))

							     
0 is divisible by 3 
 1 is not divisible by 3 or 5
 2 is not divisible by 3 or 5
3 is divisible by 3 
 4 is not divisible by 3 or 5
5 is divisible by 5 
6 is divisible by 3 
 7 is not divisible by 3 or 5
 8 is not divisible by 3 or 5
9 is divisible by 3 
10 is divisible by 5 
 11 is not divisible by 3 or 5
12 is divisible by 3 
 13 is not divisible by 3 or 5
 14 is not divisible by 3 or 5
15 is divisible by 3 
 16 is not divisible by 3 or 5
 17 is not divisible by 3 or 5
18 is divisible by 3 
 19 is not divisible by 3 or 5
>>> for a in x:
	if a % 3 == 0:
							     print("{} is divisible by 3 ".format(a))
	elif a % 5 == 0:
							     print("{} is divisible by 5 ".format(a))

	elif a % 7 == 0:
							     print("{} is divisible by 7 ".format(a))
	else:
							     print(" {} is not divisible by 3 or 5".format(a))

							     
0 is divisible by 3 
 1 is not divisible by 3 or 5
 2 is not divisible by 3 or 5
3 is divisible by 3 
 4 is not divisible by 3 or 5
5 is divisible by 5 
6 is divisible by 3 
7 is divisible by 7 
 8 is not divisible by 3 or 5
9 is divisible by 3 
10 is divisible by 5 
 11 is not divisible by 3 or 5
12 is divisible by 3 
 13 is not divisible by 3 or 5
14 is divisible by 7 
15 is divisible by 3 
 16 is not divisible by 3 or 5
 17 is not divisible by 3 or 5
18 is divisible by 3 
 19 is not divisible by 3 or 5
>>> true and true
							     
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    true and true
NameError: name 'true' is not defined
>>> True and True
							     
True
>>> False and True
							     
False
>>> True or False
							     
True
>>> for a in x:
							     if a % 3 == 0 or a % 5 == 0:
							     print(a)
							     
SyntaxError: expected an indented block
>>> 
							     
>>> 
							     
>>> 
							     
>>> False or True
							     
True
>>> True or True
							     
True
>>> True and True
							     
True
>>> False and True
							     
False
>>> False and False
							     
False
>>> True and False
							     
False
>>> for a in x:
							     if a % 3 == 0 or a % 5 == 0:
							                  print(a)

							     
0
3
5
6
9
10
12
15
18
>>> for a in x:
							     if a % 3 == 0 and a % 5 == 0:
							                  print(a)

							     
0
15
>>> ++
							     
SyntaxError: invalid syntax
>>> for a in x:
							     if a % 3 == 0 and a % 5 == 0:
							                  print(a)

							     
0
15
>>> for a in x:
							     if a % 3 == 0 or a % 5 == 0:
							                  print(a)

							     
0
3
5
6
9
10
12
15
18
>>> efor a in x:
	if a % 3 < 0:
							     print("{} is divisible by 3 ".format(a))
	elif a % 5 > 2:
							     print("{} is divisible by 5 ".format(a))
	else:
							     print(" {} is not divisible by 3 or 5".format(a))
							     
SyntaxError: invalid syntax
>>> efor a in x:
	if a % 3 < 3:
							     print("{} is divisible by 3 ".format(a))
	elif a % 5 > 2:
							     print("{} is divisible by 5 ".format(a))
	else:
							     print(" {} is not divisible by 3 or 5".format(a))
							     
SyntaxError: invalid syntax
>>> for a in x:
	if a % 3 < 3:
							     print("{} is divisible by 3 ".format(a))
	elif a % 5 > 2:
							     print("{} is divisible by 5 ".format(a))
	else:
							     print(" {} is not divisible by 3 or 5".format(a))

							     
0 is divisible by 3 
1 is divisible by 3 
2 is divisible by 3 
3 is divisible by 3 
4 is divisible by 3 
5 is divisible by 3 
6 is divisible by 3 
7 is divisible by 3 
8 is divisible by 3 
9 is divisible by 3 
10 is divisible by 3 
11 is divisible by 3 
12 is divisible by 3 
13 is divisible by 3 
14 is divisible by 3 
15 is divisible by 3 
16 is divisible by 3 
17 is divisible by 3 
18 is divisible by 3 
19 is divisible by 3 
>>> for a in x:
	if a % 3 < 2:
							     print("{} is divisible by 3 ".format(a))
	elif a % 5 > 2:
							     print("{} is divisible by 5 ".format(a))
	else:
							     print(" {} is not divisible by 3 or 5".format(a))

							     
0 is divisible by 3 
1 is divisible by 3 
 2 is not divisible by 3 or 5
3 is divisible by 3 
4 is divisible by 3 
 5 is not divisible by 3 or 5
6 is divisible by 3 
7 is divisible by 3 
8 is divisible by 5 
9 is divisible by 3 
10 is divisible by 3 
 11 is not divisible by 3 or 5
12 is divisible by 3 
13 is divisible by 3 
14 is divisible by 5 
15 is divisible by 3 
16 is divisible by 3 
 17 is not divisible by 3 or 5
18 is divisible by 3 
19 is divisible by 3 
>>> a = range(0,100)
							     
>>> for a in x:
	if a % 9 == 0:
		print("{} is divisible by 9 ".format(a))
	else:
		print(" {} is not divisible by 11".format(a))

							     
0 is divisible by 9 
 1 is not divisible by 11
 2 is not divisible by 11
 3 is not divisible by 11
 4 is not divisible by 11
 5 is not divisible by 11
 6 is not divisible by 11
 7 is not divisible by 11
 8 is not divisible by 11
9 is divisible by 9 
 10 is not divisible by 11
 11 is not divisible by 11
 12 is not divisible by 11
 13 is not divisible by 11
 14 is not divisible by 11
 15 is not divisible by 11
 16 is not divisible by 11
 17 is not divisible by 11
18 is divisible by 9 
 19 is not divisible by 11
>>> b = range(0,100)
							     
>>> for b in x:
	if a % 11 == 0:
		print("{} is divisible by 11".format(a))
	else:
		print(" {} is not divisible by 11".format(a))

							     
 19 is not divisible by 11
 19 is not divisible by 11
 19 is not divisible by 11
 19 is not divisible by 11
 19 is not divisible by 11
 19 is not divisible by 11
 19 is not divisible by 11
 19 is not divisible by 11
 19 is not divisible by 11
 19 is not divisible by 11
 19 is not divisible by 11
 19 is not divisible by 11
 19 is not divisible by 11
 19 is not divisible by 11
 19 is not divisible by 11
 19 is not divisible by 11
 19 is not divisible by 11
 19 is not divisible by 11
 19 is not divisible by 11
 19 is not divisible by 11
>>> a
							     
19
>>> b
							     
19
>>> x = range (0,100)
							     
>>> a = []
							     
>>> b =[]
							     
>>> for a and b in x:
	if a % 9 == 0:
							     print("{} is divisible by 9 ".format(a))
	elif b % 11 == 0:
							     print("{} is divisible by 11 ".format(a))
	else:
							     print(" {} is not divisible by 9  or 11".format(a))
							     
SyntaxError: invalid syntax
>>> 
							     
>>> for a in x:
	if a % 9 == 0:
							     print("{} is divisible by 9 ".format(a))
	elif b % 11 == 0:
							     print("{} is divisible by 11 ".format(a))
	else:
							     print(" {} is not divisible by 9  or 11".format(a))

							     
0 is divisible by 9 
Traceback (most recent call last):
  File "<pyshell#73>", line 4, in <module>
    elif b % 11 == 0:
TypeError: unsupported operand type(s) for %: 'list' and 'int'
>>> x = range (0,100)
							     
>>> a = []
							     
>>> b =[]
							     
>>> 
							     

>>> 
							     
>>> 
							     
>>> a.append(x)
							     
>>> a
							     
[range(0, 100)]
>>> b.append(x)
							     
>>> b
							     
[range(0, 100)]
>>> for a in x:
	if a % 11 == 0:
		a.append("{} is divisible by 9".format(a))
	else:
		b.append("is divisible by 11".format(a))

							     
Traceback (most recent call last):
  File "<pyshell#85>", line 3, in <module>
    a.append("{} is divisible by 9".format(a))
AttributeError: 'int' object has no attribute 'append'
>>> for a in x:
	if a % 11 == 0:
		a.append("{} is divisible by 9".format(a))
	elif:
		b.append("is divisible by 11".format(a))
							     
SyntaxError: invalid syntax
>>> for a in x:
	if a % 9 == 0:
							     a.append(x)
	elif b % 11 == 0:
							     b.append(x)
	else:
							     append("".format(a))

							     
Traceback (most recent call last):
  File "<pyshell#88>", line 3, in <module>
    a.append(x)
AttributeError: 'int' object has no attribute 'append'
>>> for a in x:
	if a % 9 == 0:
							     a.append(x)
	elif b % 11 == 0:
							     b.append(x)
	else:
							     append("".format(a))

							     
Traceback (most recent call last):
  File "<pyshell#90>", line 3, in <module>
    a.append(x)
AttributeError: 'int' object has no attribute 'append'
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
							     


>>> x = range (0,100)
							     
>>> a = []
							     
>>> b = []
							     
>>> for a in x:
	if a % 9 == 0:
							     a.append(x)
	elif b % 11 == 0:
							     b.append(x)

							     
Traceback (most recent call last):
  File "<pyshell#106>", line 3, in <module>
    a.append(x)
AttributeError: 'int' object has no attribute 'append'
>>> for a in x:
	if a % 9 == 0:
	   a.append(x)
	elif b % 11 == 0:
	    b.append(x)

							     
Traceback (most recent call last):
  File "<pyshell#108>", line 3, in <module>
    a.append(x)
AttributeError: 'int' object has no attribute 'append'
>>> z = range (0,100)
							     
>>> a = []
							     
>>> b = []
							     
>>> for a in z:
							     if a % 9 == 0:
							     a.append(z)
							     
SyntaxError: expected an indented block
>>> for a in z:
							     if a % 9 == 0:
							     a.append(z)
							     
SyntaxError: expected an indented block
>>> 
