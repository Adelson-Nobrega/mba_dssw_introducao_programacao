print('CONVERSOR DE TEMPERATURA ºC <> ºF')

temp = int(input('\nDigite a temperatura: '))
escala = input('Qual a escala (C = Celsius ou F = Fahrenheit)? ').upper()

if escala == 'C':
    temp = temp * 1.8 + 32
    print(f'\nA temperatura em graus Fahrenheit é: {temp:.0f} ºF')
elif escala == 'F':
    temp = (temp - 32) / 1.8
    print(f'\nA temperatura em graus Celsius é: {temp:.0f} ºC')
else:
    print('\nEscala não reconhecida!')
