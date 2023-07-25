""" Exercicio para dizer se é Par ou Ímpar"""

numero_int = input('Digite um número inteiro: ')

if numero_int.isdigit():
    numero_int = int(numero_int)
    if numero_int % 2 ==0:
        print(f"{numero_int} é par")
    else:
        print(f"{numero_int} é ímpar")
else:
    print('Isso não é um número inteiro.')

""" outra maneira de se verificar 
if not numero_int.isdigit():
      print('Isso não é um número inteiro.')
else:
    numero_int = int(numero_int)
    if  not numero_int % 2 ==0:
        print(f"{numero_int} é ímpar")
    else:
        print(f"{numero_int} é par")
        """

