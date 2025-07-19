print('CÁLCULO DE TEMPO DE VIAGEM')

distancia = float(input('\nQual a distância em km da sua viagem: '))
velocidade = float(input('\nQual sua velocidade média em km/h: '))
tempo = distancia / velocidade

print(f'\nO tempo de viagem foi {tempo:0.1f} horas')
