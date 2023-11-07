data = {'testlog': 'testpasswd'}
a = 42

while True:
	q1 = input('Vhod or registraciy (reg)')
	if q1 == 'Vhod':
	 	log = input('vvedi login: ')
	 	psswd = input('vvelbnt passwd: ')
	 	if log in data.keys():
	 		if data[log] == passwd:
	 			print('ti zashol')
	 			print(a)

	 	else:
	 		print('govno vse. Oi toest neverno')
	elif q1 == 'reg':
	 	log = input('Vvedi login: ')
	 	passwd = input('Vvedi passwd: ')
	 	if log in data.keys():
	 		print('login zanyt')
	 	else:
	 		data[log] = passwd
	 		print('Registraciy gotova')