# -*- coding: utf-8 -*-
t1 = float(input('say me temperaturu:'))
t2 = t1 * 1.8 + 32
print(t2)

x1 = int(input('vvedi 1-e chislo:'))
x2 = int(input('vvedi 2-e chislo:'))
max1 = (x1 > x2) * x1 + (x2 >= x1) * x2
print('maximalnoe chislo ', max1)