soma = 0
contMaior = 0
contMenor = 0

for i in range(5):
    idade = int(input(f'Digite a idade do {i+1}° aluno:'))
    if idade>=16:
        contMaior += 1
    else:
        contMenor += 1
        soma += idade
        media = soma/contMenor

print(f'A quantidade de alunos que podem votar é {contMaior}.')
print(f'A média da idade de não eleitores é {media} anos.')