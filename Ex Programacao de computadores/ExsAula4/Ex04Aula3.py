luz = float(input('Digite o valor da sua conta de luz:'))
agua = float(input('Digite o valor da sua conta de agua:'))
telefone = float(input('Digite o valor da sua conta de telefone:'))
salario = float(input('Digite o valor do seu salário:'))
soma = agua + luz + telefone

if salario<soma:
    print('Salário insuficiente!')
else:
    print(f'Salário restante após o pagamento das contas:{salario-soma}')