Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> student1 = {"name":"joy","age":21}
>>> student2 = {"name":"nat","age":16}
>>> student3 = {"name":"rehema","age":17}
>>> student4 = {"name":"salome","age":18}
>>> student5 = {"name":"maureen","age":19}
>>> 
>>> students=[student1,student2.student3,student4,student5]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    students=[student1,student2.student3,student4,student5]
AttributeError: 'dict' object has no attribute 'student3'
>>> students=[student1,student2,student3,student4,student5]
>>> 
>>> students
[{'name': 'joy', 'age': 21}, {'name': 'nat', 'age': 16}, {'name': 'rehema', 'age': 17}, {'name': 'salome', 'age': 18}, {'name': 'maureen', 'age': 19}]
>>> for student in students:
	print(student["name"])

	
joy
nat
rehema
salome
maureen
>>> for student in students:
	print(student["age"])

	
21
16
17
18
19
>>> for student in students:
	print(2019-student["age"])

	
1998
2003
2002
2001
2000
>>> customer1 = {"name":"chesang","balance":1000}
>>> customer2 = {"name":"charity","balance":2000}
>>> customer3 = {"name":"lucian","balance":2400}
>>> customer4 = {"name":"asha","balance":3600}
>>> 
>>> customers=[customer1,customer2,customer3,customer4]
>>> 
>>> customers
[{'name': 'chesang', 'balance': 1000}, {'name': 'charity', 'balance': 2000}, {'name': 'lucian', 'balance': 2400}, {'name': 'asha', 'balance': 3600}]
>>> for customer in customers:
	print("hello" {} "your current balance is" {} ).format[ (customer1("name") , customer1("balance") ]
								
SyntaxError: invalid syntax
>>> 
								
>>> for customer in customers:
	print("hello" {} "your current balance is" {}).format[ (customer1("name") , customer1("balance") ]
							       
SyntaxError: invalid syntax
>>> for customer in customers:
	print("hello {} your current balance is {})".format[ (customer1("name") , customer1("balance") ]
							     
SyntaxError: invalid syntax
>>> for customer in customers:
	print"hello {} your current balance is {})".format[ (customer1("name") , customer1("balance") ]
							    
SyntaxError: invalid syntax
>>> for customer in customers:
	print("hello {} your current balance is {})").format[ (customer1("name") , customer1("balance") ]
							      
SyntaxError: invalid syntax
>>> for customer in customers:
	print("hello {} your current balance is {})").format( (customer1("name") , customer1("balance") )


							      print
							      
SyntaxError: invalid syntax
>>> for customer in customers:
	print("hello" {} "your current balance is" {}).format( (customer1[("name")] , customer1[("balance")] )
							       
SyntaxError: invalid syntax
>>> for customer in customers:
	print("hello" {} "your current balance is" {}) .format( (customer1("name") , customer1("balance") )
								
SyntaxError: invalid syntax
>>> for customer in customers:
	message="hello {}, your current balance is {}" .format( (customer1("name") , customer1("balance") )
								print(message)
								
SyntaxError: invalid syntax
>>> for customer in customers:
	message = "hello {}, your current balance is {}." .format( (customer1["name"] , customer1["balance"] )
								   print(message)
								   
SyntaxError: invalid syntax
>>> 
								   
>>> 
								   
>>> for customer in customers:
	message = "hello {}, your current balance is {}." .format( (customer1["name"] , customer1["balance"] )
								   print(message)
								   
SyntaxError: invalid syntax
for customer in customers:
	message = "hello {}, your current balance is {}." .format( (customer1["name"] , customer1["balance"] )
								   print(message)
>>> 
								   
>>> 
								   

>>> 
								   







>>> 
								   

>>> 
								   




>>> 
								   

>>> 
								   



>>> 
								   

>>> 
								   



>>> for customer in customers:
	message = "hello {}, your current balance is {}." .format( (customer["name"] , customer["balance"] )
								   print(message)
								   
SyntaxError: invalid syntax
>>> for customer in customers:
	message = "hello {}, your current balance is {}." .format (customer["name"] , customer["balance"]

								   )


								   
