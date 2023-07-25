""" Iniciar com letra, pode conter números, separar por _, letrtas minusculas"""
nome = 'Fabiano'
print(nome, type(nome))
idade = 45
altura = 1.83
peso = 92.200
e_maior = idade > 18
imc = (peso / (altura * altura))
imc2 = (peso / (altura ** 2))
print('Nome:', nome, type(nome))
print('Idade:', idade)
print('Altura:', altura)
print('Seu peso é:', peso)
print('É maior:', e_maior)
print('Seu IMC é:', imc)
print('Seu IMC é:', imc2)
print(idade * altura)
print()
print(nome, 'tem', idade, 'anos de idade e seu IMC é:', imc)
