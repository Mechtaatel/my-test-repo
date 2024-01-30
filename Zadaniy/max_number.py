def maxN(a,b,c):
	q=0
	A = a + b + c 
	B = a + c + b
	C = b + c + b
	D = b + b + c
	E = c + b + a 
	F = c + a + b
	MAX = [A,B,C,D,E,F]
	for i in MAX:
		i = int(i)
		if q < i:
			q = i

	print(q)
q = 0
print(maxN(str(input()),str(input()),str(input())))


			
	
