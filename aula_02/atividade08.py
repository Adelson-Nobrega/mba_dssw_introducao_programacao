print('COMPARADOR DE NÚMEROS')

n1 = float(input('\nDigite o primeiro número real: '))
n2 = float(input('Digite o segundo número real: '))

if n1 > n2:
    print(f'{n1:0.2f} é maior que {n2:0.2f}')
elif n1 == n2:
    print(f'{n1:0.2f} é igual a {n2:0.2f}')
else:
    print(f'{n1:0.2f} é menor que {n2:0.2f}')
