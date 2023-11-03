x = float(input())
y = float(input())

if x ** 2 + y ** 2 < 25:
    print(100)
elif x ** 2 + y ** 2 <100:
    print(50)
elif x ** 2 + y ** 2 < 225:
    print(10)
else:
    print(0)