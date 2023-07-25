
"""//inclui na lista o comando .append"""

lista = ['Fabiano Alcantara', 'João Silva', 'Ana Maria']
lista.append('Pedro Paulo')
print(lista)

"""Insert vc coloca em qual posição você vai inserir """
l2 = [4,5,6]
l2.insert(0,'banana')
print(l2)

""" pop e a função que deleta o elemento do final da lista"""
l3 = [4,5,6]
print(l3)
l3.insert(0,'banana')
print(l3)
l3.pop()
print(l3)

""" del para excluir itens da lista"""
l4 = [1,2,3,4,5,6,7,8,9]
print(l4)
del(l4[3:5])
print(l4)

""" max serve para mostrtar o maior e o mim o menor valor """
l5 = [2,8,9,14,87,58,24,67,1,35,7,42]
print(max(l5))
print(min(l5))

"""range cria uma lista porem não mostra seus elementos"""
l6 = range (1,11)
print(l6)

"""Para mostrar os elementos temos que fazer alguns comandos como:"""
l6 = list(range(1,11))
print(l6)

""" você pode criar uma lista de 0 a 100 pulando de 5 em 5 """
l6 = list(range(1,100, 5))
print(l6)

