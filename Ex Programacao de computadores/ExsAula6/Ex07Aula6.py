print('Considere as coordenadas de um ponto P(x,y)')
x = float(input('Digite a coordenada x:'))
y = float(input('Digite a coordenada y:'))

if x>0 and y>0:
    print(f'O ponto P({x}, {y}) pertence ao 1° quarante.')
elif x<0 and y>0:
    print(f'O ponto P({x}, {y}) pertence ao 2° quarante.')
elif x<0 and y<0:
    print(f'O ponto P({x}, {y}) pertence ao 3° quarante.')
else:
    print(f'O ponto P({x}, {y}) pertence ao 4° quarante.')
