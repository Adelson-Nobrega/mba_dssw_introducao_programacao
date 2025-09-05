from datetime import datetime

hora = int(datetime.now().timestamp())

print(hora)

with open(f'ling_prog_{hora}.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Eu amo programar em Python!\n')
    arquivo.write('Eu amo programar em PySpark!\n')
    arquivo.write('Eu amo programar em SQL!\n')