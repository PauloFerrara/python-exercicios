fixo = float(input('Digite o salário fixo:'))
vendas = float(input('Digite o valor das vendas:'))
comissao = vendas*0.04

print(f'Comissão:R${comissao:.2f}')
print(f'Salário final:R${fixo+comissao:.2f}')