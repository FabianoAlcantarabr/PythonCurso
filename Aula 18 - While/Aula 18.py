"""
While
utilizado para realizar ações enquanto uma condição for verdadeira.
Requisitos: entender condições e operadores
"""
"""while True: # Loop infinito
    nome = input("Qual o seu nome? ")
    print(f'Olá{nome}!')"""
x = 0
while x < 10:
    print(x)
    x = x + 2
print('Acabou!')

# usando a palavra continue, ele não executa as demais funções
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue
    print(x)
    x = x + 1
print('Acabou!')
# break ela termina o looping
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        break
    print(x)
    x = x + 1
print('Acabou!')