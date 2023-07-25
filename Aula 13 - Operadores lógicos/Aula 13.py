"""
Operadores Lógicos (and, or, not, in, not in
"""

# Exemplo 1
""" nome = input('Qual o seu nome? ')
# idade = input('Qual a sua idade? ')
# idade = int(idade)
idade_menor = 20
idade_maior = 30

if idade < idade_menor or idade > idade_maior:
    print(f'{nome} Não pode pegar o empréstimo.')
else:
    print(f'{nome} pode pegar o empréstimo.')"""

#Exemplo 2
"""
a = 20
b = 30

if not b > a:
    print('B é maior que A.')
else:
    print('A é maior que B.')"""

# Exemplo 3
"""a = ''
b = 0

if not a:
    print('Por Favor, preencha o valor de A.')"""

# Exemplo 4
"""a = '888'
b = 0
if not b:
    print('Por Favor, preencha o valor de B.')"""

# Exemplo 5
"""nome = 'Fabiano Alcantara'
if 'a' in nome:
    print("Existe a letra A no seu nome.")"""

# Exemplo 6
"""nome = 'Fabiano Alcantara'
if 'kiuhhy' in nome:
    print("Existe a letra A no seu nome.")
else:
    print("Não Existe.")"""

# Exemplo 7
"""nome = 'Fabiano Alcantara'
if 'ara' not in nome:
    print("Existe a letra E no seu nome.")
else:
    print("Existe")"""

# Exemplo 8
usuario = input('Nome de usuário: ')
senha = input('Senha do Usuário: ')

usuario_bd = 'Fabiano'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print('Usuário ou senha inválidos.')
