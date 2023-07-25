""" Exercicio de horas"""

horario = input('Digite um Horário (0 - 23): ')

if horario.isdigit():
    horario = int(horario)
    if horario < 0 or horario > 23:
        print("Horário de está entre 0 e 23")
    else:
        if horario < 12:
            print('Bom Dia!')
        elif horario <= 17:
            print('Boa Tarde!')
        else:
            print('Boa Noite!')

else:
    print("Por favor, digite um horario entre 0 e 23.")