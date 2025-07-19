print('CLASSIFICADOR DE TRIÂNGULOS')

l1 = float(input('\nInforme o lado 1 do triângulo: '))
l2 = float(input('Informe o lado 2 do triângulo: '))
l3 = float(input('Informe o lado 3 do triângulo: '))

if l1 == l2 and l1 == l3:
    print('\nO triângulo é equilátero!')
elif l1 != l2 and l1 != l3 and l2 != l3:
    print('\nO triângulo é escaleno!')
else:
    print('\nO triângulo é isósceles!')
