"""
Formatando valores com modificadores
:s - texto (String)
:d - Inteiro (Int)
:f - Números de ponto flutuante (float)
:.(Número)f - quantidade de casas decimais (float) :.2f
:(Caractere) (> ou < ou ^) (Quantidade)(Tipo - s, d ou f)
> - Esquerda
< - Direita
^ - Centro
"""
num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0<10}')

num_3 = 5874
print(f'{num_3:0^10}')
num_4 = 3684
print(f'{num_4:.2f}')
num_5 = 1694
print(f'{num_5:0>10.2f}')
