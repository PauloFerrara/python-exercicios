cont = 0

while True:
    resp = input('Você já dormiu s/n? ')
    if resp in 'Nn':
        cont += 1
    elif resp in 'Ss':
        break
    else:
        print('Digite um caractere válido!')
print(f'Você contou {cont} carneirinhos!')
