
nome = 'Fabiano'
idade = 45
altura = 1.83
peso = 92.200
ano_atual = 2022
nascimento = ano_atual - idade
imc2 = (peso / (altura ** 2))

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('Seu peso é:', peso)
print('Seu IMC é:', imc2)

print()
print(f'{nome} tem{idade} anos e {altura} de altura.')
print(f'{nome} pesa {peso} e seu IMC é {imc2:.2f}.')
print(f'{nome} nasceu em {nascimento}.')
