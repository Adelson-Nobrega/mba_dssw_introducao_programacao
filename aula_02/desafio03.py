print('CÁLCULO DE IMC(Índice de Massa Corporal) - CONDIÇÃO DE PESO')

altura = float(input('\nDigite sua altura em metros: '))
massa = float(input('Digite sua massa em quilogramas: '))

imc = massa / (altura ** 2)
print(f'\nSeu IMC é: {imc:0.2f} km/m²')

if imc < 18.5:
    condicao = 'ABAIXO DO PESO'
elif 18.5 <= imc < 25:
    condicao = 'PESO NORMAL'
elif 25 <= imc < 30:
    condicao = 'SOBREPESO'
elif 30 <= imc < 35:
    condicao = 'OBESIDADE GRAU I'
elif 35 <= imc < 40:
    condicao = 'OBESIDADE GRAU II'
elif imc >= 40:
    condicao = 'OBESIDADE GRAU I'

print(f'Sua condição de peso atual é {condicao}')
