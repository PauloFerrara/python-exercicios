turno = input('Considere que:\n D = Diurno\n N = Noturno\nQual é o seu turno de trabalho? ')
horas = float(input('Qual é a sua quantidade de horas trabalhadas? '))

if turno == 'N' or turno =='n':
    print(f'Seu salário é R${horas*45:.2f}')
elif turno == 'D' or turno =='d': 
    print(f'Seu salário é R${horas*37.50:.2f}')
else:
    print('Digite seu turno corretamente!')