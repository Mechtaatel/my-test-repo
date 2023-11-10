import json
import math
#data = {'name': 'reiting'}
#with open('Rating_list.json', 'w') as f:
#    json.dump(data, f)



def elo_rating():
    print('go or exit(e)'+'\n')
    i = input()

    if i == 'go':

        with open('Rating_list.json','r') as f:
            Rating_list = json.load(f)

        player_1 = input('Player 1: ')
        player_2 = input('Player 2: ')

        if player_1 in Rating_list.keys():
            if player_2 in Rating_list.keys():

                A = Rating_list[player_1]
                B = Rating_list[player_2]
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
                else:
                    print('skatina, ti vvel ne pravilno')
                if R_a < 100:
                    R_a = 100
                if R_b < 100:
                    R_b = 100
                R_a = math.ceil(R_a)
                R_b = math.ceil(R_b)
                print(f'New retig player {player_1}')
                print(R_a)
                print(f'New retig player {player_2}')
                print(R_b)

                Rating_list[player_1] = R_a
                Rating_list[player_2] = R_b
                with open('Rating_list.json','w') as f:
                    json.dump(Rating_list, f)
            else:
                print('\n'+f'Name {player_2} not exists')
        else:
            print('\n'+f'Name {player_1} not exists')


            

        
        i = str(input('go or exit(e)?'))
    elif i == 'e':
        print('Konez')
        return()   
    else:
        i = 'go'
        print('ti napisal chto-to ne to')

def RatingManager_add(name, rating):
    
    with open('Rating_list.json','r') as f:
        Rating_list = json.load(f)
    if name not in Rating_list.keys():
        Rating_list[name] = rating
        with open('Rating_list.json', 'w') as f:
            json.dump(Rating_list, f)
        print('Name add.'+'\n')
    else:
        print('\n'+'Name busy. Please repit.'+'\n')
    
    
def RatingManager_dell(name):
    print('press ani key with next')
    print('(e) - exit')
    q2 = input()
    if q2 == 'e':
        return()
    else:
        with open('Rating_list.json','r') as f:
            Rating_list = json.load(f)
        if name in Rating_list.keys():
            del Rating_list[name]
            with open('Rating_list.json', 'w') as f:
                json.dump(Rating_list, f)
            print('Name delete.'+'\n')
        else:
            print('Name no exis'+'\n')
while True:
    print('Menu')
    print('Shitat raiting (r)')
    print('Dobavit/del uchastnika (a/d)')
    print('Exit (e)'+'\n')
    q1 = input()
    if q1 == 'r':
        print(elo_rating())
    elif q1 == 'a':
        RatingManager_add(input('Name: '), int(input('Rating: ')))
    elif q1 == 'd':
        RatingManager_dell(input('Name: '))
    elif q1 == 'e':
        break