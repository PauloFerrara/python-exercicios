import math

n1 = float(input('Digite o primeiro número:'))
n2 = float(input('Digite o segundo número:'))
op = input('Considere que:\n 1-Média\n 2-Diferença maior-menor\n 3-Produto\n 4-Divisão de n1/n2\n Digite a operação que deseja realizar:')

media = (n1+n2)/2
dif = n1 - n2
dif = math.fabs(dif)
produto = n1*n2
div = n1/n2

if op == '1':
    print(f'A média entre {n1} e {n2} é:{media}')
elif op == '2':
    print(f'A diferença entre {n1} e {n2} é:{dif}')
elif op == '3':
    print(f'O produto entre {n1} e {n2} é:{produto}')
elif op == '4':
    if n2 == 0:
        print('O segundo número não pode ser 0.')
    else:
        print(f'A divisão entre {n1} e {n2} é:{div}')
else:
    print('Opção inválida, informe a operação corretamente!')

