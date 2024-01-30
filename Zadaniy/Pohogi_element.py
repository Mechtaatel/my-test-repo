I = [10, 10, 'hi' , 23, 10, 123, 66, 'H', 'H', 'L', 'hi', 78, 123]
q = []
l = set()
for i in I:
	if i in q:
		l.add(i)
	else:
		q.append(i)

print(l)