import math
soma = 0
t = int(input('Digite a quantidade de turmas:'))

for i in range(t):
    num = int(input(f'Digite o numero de alunos da {i+1}° turma:'))
    soma += num
    media = soma/t 

print(f'As turmas têm em média {math.ceil(media)} alunos.')
