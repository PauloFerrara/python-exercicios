tam = int(input('Digite o temanho do arquivo (MB):'))
vel = int(input('Digite a velocidade da internet (Mbps):'))
tempo = tam/vel

print(f'Tempo aproximado para download: {tempo} segundos.')