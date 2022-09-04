ti = int(input('Digite a temperatura inicial em °C:'))
tf = int(input('Digite a temperatura final em °C:'))

tc = tf - ti
TF = tc * 1.8

print(f'Variação de temperatura em °C: {tc}°C')
print(f'Variação de temperatura em °F: {TF}°F')