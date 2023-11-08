import pickle

print('go - nachat programmu')
i = str(input('Cto delaem:'))

#Tut po idei on dolgen bil brat biblioteku
tabl = open('Raiting.txt','wb')
#u can delete
while True:
    if i == 'go':
        a = input('Reitig igtoka A:')
        b = input('Reitig igtoka B:')

        #Tut dolgen brat iz biblioteki to chto sverhu
        A = data[a]
        B = data[b]
        #u can delete
        print(A, B)
            

        Q_a = 10 ** (A / 400)
        Q_b = 10 ** (B / 400)
        E_a = Q_a / (Q_a + Q_b)
        E_b = Q_b / (Q_a + Q_b)

        if A <= 2100:
            K_a = 32
        elif A <= 2400:
            K_a = 24
        else:
            K_a = 16
            
        if B <= 2100:
            K_b = 32
        elif B <= 2400:
            K_b = 24
        else:
            K_b = 16
                
        print('1 - Win  0.5 - 50/50  0 - lose')
        S_a = float(input('Player A:'))
        S_b = float(input('Player B:'))


        if S_a + S_b == 1:
            R_a = A + K_a * (S_a - E_a)
            R_b = B + K_b * (S_b - E_b)
            if R_a < 100:
                R_a = 100
            if R_b < 100:
                R_b = 100
            print('New reitig igroka A')
            print(int(R_a))
            print('New reitig igroka B')
            print(int(R_b))
        else:
            print('skatina, ti vvel ne pravilno')
        i = str(input('go or exit?'))
    elif i == 'exit':
        print('Konez')
        break   
    else:
        i = 'go'
        print('ti napisal chto-to ne to')