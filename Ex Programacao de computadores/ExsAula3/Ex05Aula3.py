import math 

angulo = float(input('Digite o valor de um ângulo em graus: '))
angulo = math.radians(angulo)

print(f'O seno do ângulo é:{math.sin(angulo):.2f}')
print(f'O cosseno do ângulo é:{math.cos(angulo):.2f}')
print(f'A tangente do ângulo é:{math.tan(angulo):.2f}')