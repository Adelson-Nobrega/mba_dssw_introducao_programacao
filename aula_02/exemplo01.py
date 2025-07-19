print('VERIFICAÇÃO DE MAIORIDADE')

idade = int(input('\nDigite a sua idade: '))
ingresso = input('Ingresso VIP ou PISTA: ').upper()

if idade >= 18 and ingresso == 'VIP':
    print('Siga para o primeiro andar!')
elif idade >= 18 and ingresso == 'PISTA':
    print('Siga pelo corredor!')
else:
    print('Volte para casa!')
