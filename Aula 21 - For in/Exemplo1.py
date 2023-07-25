texto = 'Python'
nova_string = ''

# continue = pula para o prox. laço
# break = termina o laço

# for letra in texto:
#     if letra == 't':
#         nova_string = nova_string + letra.upper()
#     elif letra == 'h':
#         nova_string += letra.upper()
#     else:
#         nova_string += letra
#
# print(nova_string)

# for letra in texto:
#     if letra == 't':
#         continue
#         nova_string = nova_string + letra.upper()
#     elif letra == 'h':
#         nova_string += letra.upper()
#     else:
#         nova_string += letra
#
# print(nova_string)

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra

print(nova_string)