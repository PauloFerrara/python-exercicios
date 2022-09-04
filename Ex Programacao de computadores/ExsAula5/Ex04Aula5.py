x = float(input('Digite um valor:'))
y = float(input('Digite outro valor:'))
op = input('Considere:\n1 = soma\n2 = subtração\n3 = multiplicação\n4 = divisâo\nQual operação deseja realizar?')

if op == '1':
    print(f'{x} + {y} = {x+y}')
elif op == '2':
    print(f'{x} - {y} = {x-y}')
elif op == '3':
    print(f'{x} x {y} = {x*y}')
elif op == '4':
    print(f'{x} / {y} = {x/y}')
else:
    print('Insira os valores corretamente!')