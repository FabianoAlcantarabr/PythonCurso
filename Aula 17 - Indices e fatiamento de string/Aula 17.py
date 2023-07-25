"""
Manipulando strings
*String indices
*Fatiamento de string[inicio:fim:passo]
*funções built-in len. abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.
"""
# positivos [p=0;y=1;...]
texto = 'Python_s2'
print(texto[5])
# negativos [p=-9;y=-8; ...]
print(texto[-9:-3])

# fatiamento de string
nova_string = texto[0:9]  # não inclui o último sempre soma +1
# da parte do texto que se quer cortar
print(nova_string)
print(nova_string[0::2])
print(len(texto))
for letra in texto:
    print(letra)