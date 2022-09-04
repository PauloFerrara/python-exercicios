print('Vamos calcular o volume do tronco de uma pirâmide!')
h = float(input('Digite o valor da altura:'))
bmenor = float(input('Digite o valor da sua base menor:'))
bmaior = float(input('Digite o valor da sua base maior:'))
volume = h/3 * (bmaior**2 + bmenor**2 + (bmaior**2 * bmenor**2)**0.5)

print(f'O volume do tronco da pirâmide é: {volume:.2f}')