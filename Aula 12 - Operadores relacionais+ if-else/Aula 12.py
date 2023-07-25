"""
Operadores Relacionais (== > >= < <= !=)+ IF, ELIF E ELSE
"""

"""variavel = 'valor'
print(2 == 2)"""

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

idade = int(idade)

# Limite para pegar emprestimo, exemplo 1
"""idade_limite = 18

if idade >= idade_limite:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} Não pode pegar o empréstimo.') """

idade_menor = 20
idade_maior = 30

if idade < idade_menor or idade > idade_maior:
    print(f'{nome} Não pode pegar o empréstimo.')
else:
    print(f'{nome} pode pegar o empréstimo.')

