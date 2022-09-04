cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0

while True:
    n = int(input('Digite um numero positivo(-1 para sair):'))
    if n < 0:
        break
    elif n <= 25:
        cont1 += 1
    elif n <= 50:
        cont2 += 1
    elif n <= 75:
        cont3 += 1
    elif n <= 100:
        cont4 += 1

print(f'[0-25]:{cont1} números.')
print(f'[25-50]:{cont2} números.')
print(f'[50-75]:{cont3} números.')
print(f'[75-100]:{cont4} números.')