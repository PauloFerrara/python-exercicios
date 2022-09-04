n1 = float(input('Digite a nota 1:'))
n2 = float(input('Digite a nota 2:'))
media = (n1+n2)/2

if media>=9:
    print('Aprovado!')
    print('Conceito A.') 
elif media>=7.5:
    print('Aprovado!')
    print('Conceito B.') 
elif media>=6:
    print('Aprovado!')
    print('Conceito C.')
elif media>=4: 
    print('Aprovado!')
    print('Conceito D.')
else: 
    print('Aprovado!')
    print('Conceito E.') 