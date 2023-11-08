data = {'testlog':'testpasswd'}
a=42

while True:
	q1=input('Vhod(log) or registraciy (reg): ')
	if q1 == 'log':
	 	log = input('vvedi login: ')
	 	passwd = input('vvelbnt passwd: ')
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
	elif q1 == 'exit':
	 	break