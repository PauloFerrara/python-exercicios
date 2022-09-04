soma = 0
num = input('Digite um número de 4 dígitos:')

for i in num:
    soma += int(num)
dig = soma%10

print(f'Número da conta: 00{num}-{dig}')
