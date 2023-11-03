x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

k2 = x2, y2

m1 = (x1 + 2, y1 + 1)
m2 = (x1 + 2, y1 - 1)
m3 = (x1 - 2, y1 + 1)
m4 = (x1 - 2, y1 - 1)
m5 = (x1 + 1, y1 + 2)
m6 = (x1 + 1, y1 - 2)
m7 = (x1 - 1, y1 + 2)
m8 = (x1 - 1, y1 - 2)

if (m1 or m2 or m3 or m4 or m5 or m6 or m7 or m8 == k2):
    print ('koni biut drug druga')
elif (m1 or m2 or m3 or m4 or m5 or m6 or m7 or m8 != k2):
    print ('koni ne biut drug druga')


if (abs(x1 - x2) == 2) & (abs(y1 - y2) == 1):
    print('da')
elif (abs(x1 - x2) == 1) & (abs(y1 - y2) == 2):
    print('da')
else:
    print('no')