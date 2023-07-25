""" Contagem de Caracteres """

nome = input('Digite seu nome: ')
tamanho = len(nome)

if tamanho <= 4:
    print('Seu Nome é curto.')
elif tamanho <= 6 :
    print("Seu Nome é normal.")
else:
    print('Seu Nome é muito grande.')

