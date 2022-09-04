import math
a = float(input('Digite a área a ser pintada em m²:'))
qlitros = a/3
qlatas = qlitros/18
qlatas = math.ceil(qlatas)
custo = qlatas*80

print(f'Para pintar {a}m², será necessário comprar {qlatas} latas, que custarão R${custo:.2f}')