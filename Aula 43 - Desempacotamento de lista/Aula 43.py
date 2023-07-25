"""Desempacotamento de Listas"""

lista = ['Luiz', 'João', 'Maria']

n1, n2, n3 = lista

print(n2)
print(n1, n3)
print()
lista_1 = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

n1, n2, n3, *outra_lista, ultimo_valor = lista_1
print(n1, n2, *outra_lista)
print(ultimo_valor)
