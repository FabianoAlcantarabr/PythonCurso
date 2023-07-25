
x = 10
y = 'Pedro'
"""Mudando os valores """

z = x
x = y
y = z
print(f'x={x} e y={y}')

#  é a mesma coisa
a = 10
b = 'Pedro'
a, b = b, a
print(f'a={a} e b={b}')

