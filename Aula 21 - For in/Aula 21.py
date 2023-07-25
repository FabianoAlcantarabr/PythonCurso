"""
For in
Iterando strings com for
Função range(start=0, stop, step=1)
"""

texto = "Python"

#  Comparação do While e for para o mesmo uso.
# c = 0
# while c < len(texto):
#     print(texto[c])
#     c += 1

for letra in texto:
    print(letra)

for n in range(10):
    print(n)

for n in range(0, 10, 3):
    print(n)

for n in range(20, 10, -2):
    print(n)