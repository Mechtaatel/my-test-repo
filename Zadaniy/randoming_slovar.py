from random import sample
d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}

l = []

for i in d.keys():
	l.append(d[i])
dd = {}
r = sample(l,len(l))
t = 0
for i in d.keys():
	dd[i] = r[t]
	t +=1
print(dd)




