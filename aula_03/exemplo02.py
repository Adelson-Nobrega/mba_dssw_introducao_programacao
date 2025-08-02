import time

alunos = [
    'Adelson',
    'Hugo',
    'Carla',
    'Saulo',
    'Paloma'
]

mensagem = 'Venha para a festa de aniversário de Leticia, mas traga sua comida e bebida!'

for nome in alunos:
    print(f'{nome}, {mensagem}')
    time.sleep(1)
