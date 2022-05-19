a = float(input('Введите температуру в комнате '))
b = float(input('Введите желаемую температуру в комнате '))
v = float(input('Введите влажность воздуха в комнате '))
if a > b and v <= 80:
    print('on')
else:
    print('off')
