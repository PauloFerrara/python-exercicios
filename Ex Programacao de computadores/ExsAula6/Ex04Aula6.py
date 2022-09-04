alt = float(input('Digite a sua altura em metros:'))
sexo = input('Ago, informe o seu sexo(M/F):')

if sexo == 'm' or sexo == 'M':
    print(f'O seu peso ideal é {(72.7*alt)-58:.2f}kg.')
elif sexo == 'f' or sexo == 'F':
    print(f'O seu peso ideal é {(62.1*alt)-44.7:.2f}kg.')
else:
    print('Informe o sexo corretamente!')