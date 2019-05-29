Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=[[1,2,3],[4,5,6],[7,8,9]]
>>> n = []
>>> for sublist in x:
	for r in sublist:
		n.append(r)

		
>>> n
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
