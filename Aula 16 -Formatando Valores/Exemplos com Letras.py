"""
Formatando valores com modificadores
:s - texto (String)
:d - Inteiro (Int)
:f - Números de ponto flutuante (float)
:.(Número)f - quantidade de casas decimais (float) :.2f
:(Caractere) (> ou < ou ^) (Quantidade)(Tipo - s, d ou f)
> - Esquerda
< - Direita
^ - Centro
"""
nome = 'Fabiano Alcantara'
sobrenome = 'Dos Santos'
print((50 - len(nome)) / 2)
print(f'{nome:#^50}')
nome_formatado = '{:*>20}'.format(nome)
print(nome_formatado)
nome_formato = '{n:0<20}'.format(n=nome)
print(nome_formato)
nome_formatod = '{1}'.format(nome, sobrenome)
print(nome_formatod)
print(nome.lower())
print(nome.upper())
print(nome.title())
