
A = int(input('Reitig igtoka A:'))
B = int(input('Reitig igtoka B:'))

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
    print('New reitig igroka A')
    print(int(R_a))
    print('New reitig igroka B')
    print(int(R_b))
else:
    print('skatina, ti vvel ne pravilno')