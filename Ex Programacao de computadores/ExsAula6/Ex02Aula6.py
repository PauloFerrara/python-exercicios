seg = int(input('Digite a quantidade de segundos:'))
horas = seg//3600
min = (seg%3600)// 60
seg = seg%60

print(f'{horas} hora(s), {min} minuto(s) e {seg} segundo(s)')