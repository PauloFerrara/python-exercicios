compra = float(input('Digite o valor da compra para saber se o desconto é válido:'))
desconto = compra*0.2
vfinal = compra - desconto

if compra<200:
    print(f'O desconto não é valido para compras neste valor. Seu valor final é {compra} reais.')
else:
    desconto = compra*0.2
    vfinal = compra - desconto
    print(f'Muito bem! Você obteve um desconto de {desconto} reais. Agora o valor total de sua compra é {vfinal} reais.')
