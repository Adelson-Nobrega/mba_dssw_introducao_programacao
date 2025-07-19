print('CÁLCULO DE TEMPO DE VIAGEM')

distancia = float(input('\nQual a distância em km da sua viagem: '))
velocidade = float(input('\nQual sua velocidade média em km/h: '))

tempo_h = distancia // velocidade
tempo_m = (distancia % velocidade) / velocidade * 60

print(f'\nO tempo de viagem foi {tempo_h:0.0f} horas e {tempo_m:0.0f} minutos')
