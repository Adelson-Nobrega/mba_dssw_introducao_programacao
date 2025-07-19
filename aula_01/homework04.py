print('CÁLCULO DE IMC(Índice de Massa Corporal)')

altura = float(input('\nDigite sua altura em metros: '))
massa = float(input('\nDigite sua massa em quilogramas: '))

imc = massa / (altura ** 2)

print(f'\nSeu IMC é: {imc:0.2f} km/m²')
