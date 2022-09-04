soma = 0
maior = 0
nomeMaior = ''

for i in range(3):
    nome = input(f'Digite o nome do {i+1}° aluno:')
    h = int(input(f'Digite a altura do(a) {nome} em cm:'))
    soma += h
    media = soma/3

    if h > maior:
        maior = h
        nomeMaior = nome

print(f'A média das alturas é: {media} cm')
print(f'A altura maior é do(a) {nome}: {maior} cm')
    