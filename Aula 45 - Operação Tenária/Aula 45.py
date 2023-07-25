""" Operador Ternário"""

logger_user = True

if logger_user:
    msg = 'Usuário logado.'
else:
    msg = 'Precisa se logar.'

print(msg)

# outra maneira

logger_users = False
msgs = 'Usuário logado.' if logger_users else 'Precisa se logar.'
print(msgs)

"""Exemplos"""
idade = 18
if idade >= 18:
    print('Pode acessar.')
else:
    print('Não pode acessar.')

""" Outro Exemplo"""
idades = input('Qual a sua idade?')
if not idades.isnumeric():
    print('Você precisa digitar apenas números')
else:
    idades = int(idades)
    e_de_maior = (idades >= 18)
    mens = 'Pode acessar' if e_de_maior else 'Não pode acessar.'

    print(mens)
