nome = input('Digite o nome do produto:')
vcompra = float(input('Digite o valor da compra:'))

if vcompra<10:
    print(f'O valor de venda do {nome} deverá ser {vcompra*1.7}')
elif vcompra>=10 and vcompra<30:
    print(f'O valor de venda do {nome} deverá ser {vcompra*1.5}')
elif vcompra>=30 and vcompra<50:
    print(f'O valor de venda do {nome} deverá ser {vcompra*1.4}')
else:
    print(f'O valor de venda do {nome} deverá ser {vcompra*1.3}')
    