valorPrestacao = float(input('Digite o valor da prestação: '))
multa = float(input('Digite a porcentagem de multa pelo atraso: '))
qtdeDias = int(input('Digite a quantidade de dias de atraso: '))
prestacao = valorPrestacao + (valorPrestacao*(multa/100)*qtdeDias)

print(f'O valor final da prstação em atraso ficará: {prestacao:.2f}')