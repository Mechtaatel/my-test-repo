import pickle
tabl = open('Reiting.txt','r+')
R = tabl.read()
R
print(tabl.read())
print('go - nachat programmu')

i = str(input('Cto delaem:'))
while True:
    if i == 'go':
        a = input('Reitig igtoka A:')
        b = input('Reitig igtoka B:')

        
        A = data[a]
        B = data[b]
        print(A, B)

        data[a] = A + B
        print(data[a])
        break




