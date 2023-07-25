num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')
""" tem que transformar o numero em inteiro ou float se quiser usar ponto"""

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print("Não pude converter os números para realizar contas.")