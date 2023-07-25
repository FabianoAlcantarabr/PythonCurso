"""
Split - Dividir uma string #str
Join - Juntar uma lista #str
Enumerate - Enumerar elementos da lista # iteráveis
"""
string = "O Brasil é o pais do futebol, o Brasil é penta."
lista_1 = string.split(' ')
lista_2 = string.split(',')

palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes foi {palavra} ({contagem}x)')

""" Join junta os elementos"""
string = "O Brasil é penta."
lista = string.split(' ')
string2 = ','.join(lista)
print(string)
print(lista)
print(string2)

"""Enumerate"""
string = "O Brasil é penta."
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])

listas = [
    [1,2],
    [3,4],
    [5,6],
]
for v in listas:
    print(v[0], [1])

lista_3 = [
    [0, 'Luiz'],
    [1, 'João'],
    [2, 'Maria'],
]
for indice, nome in lista_3:
    print(indice, nome)
    print()
lista_4 = ['Luiz','João', 'Maria']
for indice, nome in enumerate(lista_4):
    print(indice, nome)
