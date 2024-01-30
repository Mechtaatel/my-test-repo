s="""Govorit idiot. Chto? Da da, idiot. I say its write."""
d = int(input('Dlina: '))
q = ""

while True:
	z = s.find(' ')
	# b = s.find('.')
	# c = s.find(',')
	# r = s.find('?')
	# l = s.find('!')
	# for i in 
	# На будущее сделать так что бы знаки препенания не учитывать как слова
	#  я мог бы и сейчас но я пока могу только гразмозкими if elif прописовать
	#  найди способ избавиться от этого.
	if z == -1:
		break
	elif d >= z:
		q = q + s[:z+1]
		s = s.replace(s[:z+1],'')
	elif d < z:
		s = s.replace(s[:z+1],'')
	
	
print(q)