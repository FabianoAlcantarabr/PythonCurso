""" OPERADORES ARITMETICOS """

""" +, -, *, /, //, **, %, ()"""  # // e a divisão inteira resultado arredondado, ** Potenciação, % resto da divisão
print('Multiplicação *', 10 * 10)
print('Adição +', 10 + 10)
print('Subtração -', 10 - 5)
print('Divisão /', 10 / 2)

print('Multiplicação *', 10 * '10')  # se refere a repetidor vai aparecer 10 vezes o número 10 ou o que estiver
# entre as aspas

print('Adição +', "10" + '10')  # Se tiver assim ele faz contenação dos alores saindo 55

# print('Adição +', 10 + '10')  # Não pode usar assim, pois apresenta o erro, pois está usando  int com str.

print(10.5 // 3)  # Mostra o resultado inteiro, pois temos numeros flutantes

print(10 / 3)  # Mostra o resultado em números flutuantes

print(2 ** 3)  # Significa 2 elevado a 3

print(10 % 3)  # esse mostra o modulo o resto da divisão

print(5 + 2 * 10)  # Parêntece e para dizer a prioridade da execução
print((5 + 2) * 10)
