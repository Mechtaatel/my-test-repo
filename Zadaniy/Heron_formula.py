def Heron_f(a,b,c):
	s = (1/2)*(a+b+c)
	A = (s*(s-a)*(s-b)*(s-c))**(0.5)
	print(A)
print(Heron_f(int(input('a: ')),int(input('b: ')),int(input('c: '))))

