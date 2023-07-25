"""
Tipos de Dados
str = string - textos 'Assim' ou "Assim"
int = inteiro - 123456 0 -10 -20 -50
float = real/ponto flutuante - 10.50 1.5 -10.10 0.0
bool = booleano/lógico - True/False
"""

print(type('Luiz'))
print(type('12345'))
print(type(12345))
print(type(123.45))
print(100 == 100, type(100 == 100))
print('l' == 'l', type('l' == 'l'))
print('Luiz', type('Luiz'), bool('Luiz'))  # Boleano
print('10', type('10'), type(int('10')))  # type casting, converteu o 10 para inteiro


