import json
#data_pizza = {'margarita': 400, 'carbonara': 500}
#data_user = {'Admin': '0000'}
#with open('pizza.json', 'w') as f:
#  json.dump(data_pizza, f)


def add_pizza(name, price):
  with open('pizza.json','r') as f:
    data_pizza = json.load(f)
  if name not in data_pizza.keys():
    data_pizza[name] = price
    with open('pizza.json','w') as f:
      json.dump(data_pizza, f)
  else:
    print('Pizza already exists')
def del_pizza(name):
  with open('pizza.json','r') as f:
    data_pizza = json.load(f)
  if name in data_pizza.keys():
    del data_pizza[name]
    with open('pizza.json','w') as f:
      json.dump(data_pizza, f)
  else:
    print('Pizza not exists')
def order_pizza():
  order = []
  cost = 0
  while True:
    with open('pizza.json','r') as f:
      data_pizza = json.load(f)
    q1 = input('Continue?: ')
    if q1 == 'no':
      break

    pizza_name = input()
    if pizza_name in data_pizza.keys():
      order.append(pizza_name)
      cost += data_pizza[pizza_name]
      print('pizza added')
  return {'order': order, 'cost': cost}
while True:
  print('login or registration?')
  print('(log)      (reg)')
  print('exit is exit')
  q1 = input()
  if q1 == 'log':
    login = input()
    passwd = input()
    with open('pizza.json','r') as f:
      data_user = json.load(f)
    if login in data_user.keys():
      if data_user[login] == passwd:
        if login == 'Admin':
          q2 = input('Add or delete: ')
          if q2 == 'del':
            del_pizza(input('Pizza name?: '))
          elif q2 == 'add':
            add_pizza(input('Pizza name?: '), int(input('Price')))
        else:
          print(order_pizza())
  if q1 == 'reg':
    login = input('login: ')
    passwd = input('password: ')
    with open('pizza.json','r') as f:
      data_user = json.load(f)
    if login in data_user.keys():
      print('Login busy')
    else:
      data_user[login] = passwd
      print('Successful registration')
      with open('pizza.json','w') as f:
        json.dump(data_user, f)
  if q1 == 'exit':
    break