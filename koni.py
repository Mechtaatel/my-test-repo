x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

k2 = (x2, y2)

m1 = (x1 + 2, y1 + 1)
m2 = (x1 + 2, y1 - 1)
m3 = (x1 - 2, y1 + 1)
m4 = (x1 - 2, y1 - 1)
m5 = (x1 + 1, y1 + 2)
m6 = (x1 + 1, y1 - 2)
m7 = (x1 - 1, y1 + 2)
m8 = (x1 - 1, y1 - 2)

m = [m1, m2, m3, m4, m5, m6, m7, m8]

for i in m:
    if i == k2:
        print ('koni biut drug druga')
    else:
        print('koni ne biut drug druga')

# nige otvet k zadachi
if (abs(x1 - x2) == 2) & (abs(y1 - y2) == 1):
    print('da')
elif (abs(x1 - x2) == 1) & (abs(y1 - y2) == 2):
    print('da')
else:
    print('no')