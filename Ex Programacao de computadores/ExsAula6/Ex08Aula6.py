nome = input('Qual o seu nome?')
h = int(input('Que horas são [0-23]?'))

if h >= 5 and h<=12:
    print(f'Bom dia, {nome}!')
elif h>=13 and h<=18:
    print(f'Boa tarde, {nome}!')
else:
    print(f'Boa noite, {nome}!')