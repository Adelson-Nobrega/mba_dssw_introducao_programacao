import requests

URL = ('https://api.adviceslip.com/advice',)
conselhos = []

qtd = int(input('Quantos conselhos você deseja (1-10): '))

try:
    for i in range(qtd):
        resultado = requests.get(URL[0])
        conselho = resultado.json()['slip']['advice']
        conselhos.append(conselho)

except Exception as error:
    print(f'ERROR: {error}')

try:
    with open('conselhos.txt', 'w', encoding='utf-8') as arquivo:
        for conselho in conselhos:
            arquivo.write(f'{conselho}\n')
            print(f'CONSELHO SALVO -> {conselho}')

except Exception as error:
    print(f'ERROR: {error}')