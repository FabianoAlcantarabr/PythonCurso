x = 0  # Coluna
y = 0  # Linha

"""while x < 10:
    print(x)
    x += 1  # x = x +1

print('Acabou!')"""

while x < 10:
    y = 0
    while y < 5:
        print(f'x vale {x} e y vale {y}')
        """ ou print(f'({x},{y})') """
        y += 1
    x += 1  # x = x +1

print('Acabou!')