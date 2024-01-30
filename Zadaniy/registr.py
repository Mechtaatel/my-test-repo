import json
def register(login, password):
	data = json.load(open('reg.json'))
	if login in data.keys():
		print('Логин уже занят')
	elif:
		new = {login: password}
		with open('reg.json','w') as f:
			json.dump(new,f)
		print('вы успешно зарегестрировались')
def login_function(login, password):
	data = json.load(open('reg.json'))
	if login in data.keys():
		if data[login] == password:
			print("вы успешно вошли в систему")
		else:
			print("Пороль неверен")
	else:
		print("Такой пользователь не зарегестрирован")