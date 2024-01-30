x = int(input("Vklad v Banke: "))
y = int(input('Procentnai stavka: ')) / 100
p = int(input('Skolko negno ctobi bilo?: '))
ya = 0

while p >= x:
	z = x*y
	x = x+z
	ya += 1
print(f'need {ya} years')
