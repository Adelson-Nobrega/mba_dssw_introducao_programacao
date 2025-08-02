print('GERADOR DE TABUADA')
import time

num = int(input('Escolha um número de 1 a 10: '))
m = 1 # multiplicador

print(f'\nTABUADA DE {num}')
while m < 11:
    r = num * m
    print(f'{num} * {m} = {r}')
    m += 1
    time.sleep(0.5)
