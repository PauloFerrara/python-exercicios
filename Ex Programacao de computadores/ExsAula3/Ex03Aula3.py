print('Vamos calcular o seu tempo de vida em dias! Para isso, precisamos do seu tempo de vida exato(anos, meses e dias).')
anos = int(input('Quantos anos você tem? '))
meses = int(input('E quantos meses? '))
dias = int(input('E quantos dias? '))
diastotais = anos*365 + meses*30 + dias

print(f'{anos} anos {meses} meses e {dias} dias são equivalentes a {diastotais} dias.')