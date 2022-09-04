#Feito na Aula 2
import math
from this import d

print('A equação que iremos calcular é: ax² + bx + c')
a = float(input('Digite o valor de a:'))
if a==0:
    print('Se a = 0, não é uma equação de segundo grau.')
else:
    b = float(input('Digite o valor de b:'))
    c = float(input('Digite o valor de c:'))
    d = b*b - 4*a*c
if d<0:
    print('Se delta menor que 0, a equação não possui raízes reais.')
elif d==0:
    x = -b / 2*a
    print(f'A equação possui apenas uma raiz. x é igual a {x}')
else:
    x1 = (- b + math.sqrt(d)) / 2*a
    x2 = (- b - math.sqrt(d)) / 2 * a
    print(f'Se a raiz for positiva, x é igual a:{x1}')
    print(f'Se a raiz for negativa, x é igual a:{x2}')

