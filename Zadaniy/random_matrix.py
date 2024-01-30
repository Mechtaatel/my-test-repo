from random import randint


n=5
m = [[randint(0,99) for i in range(n)] for j in range(n)]

while True:
	vv = input('Spisok(s) or Element(e): ')
	if vv == 's':
		Q = 0
		q = []
		for i in range(len(m)):
			for l in m[i]:
				if l > Q:
					Q = l
					q = m[i]
		break
		
	else: 
		q = 0
		for i in range(len(m)):
			for l in m[i]:
				if l > q:
					q = l

		break


print(q)

