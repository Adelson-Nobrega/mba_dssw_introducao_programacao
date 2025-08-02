# LISTAS, TUPLAS E DICIONÁRIOS
from operator import index
from os import remove

# LISTAS - Permite modificar os elementos individualmente
cariocao = ['Flamengo', 'Botafogo', 'Fluminense', 'Vasco', 'Bangu', 'Madureira']

print(cariocao)
print(type(cariocao))

print('Bangu foi rebaixado! e o campeão da segundona foi o América')
cariocao[4] = 'América'
print(f'\n{cariocao}')

print('Cariocao recebe um novo time, o Americano')
cariocao.insert(5, 'Americano')
print(f'\n{cariocao}')

print('\n América rebaixado')
del cariocao[4]
print(f'\n{cariocao}')

indice = cariocao.index('Americano')
del cariocao[indice]
print(f'\n{cariocao}')

cariocao.remove('Madureira')
print(f'\n{cariocao}')

cariocao.pop(3)
print(f'\n{cariocao}')

#TUPLAS - Não permite modificar os elementos individualmente, apenas sobrescrever
# com outra tupla de qualquer tamanho
titulos = (39, 21, 32)
print(titulos[0])
print(titulos[2])

print('\nQuantidade de títulos original')
for titulo in titulos:
    print(titulo)

titulos = (42, 23)
print('\nNova quantidade de títulos')
for titulo in titulos:
    print(titulo)

#DICIONÁRIOS - É uma coleção de pares chave-valor
pessoa = {'nome' : 'Adelson', 'idade' : '43', 'rg' : '2447116'}

print(pessoa['nome'])
print(pessoa['rg'])

pessoa['nome'] = 'Davi'
print(pessoa['nome'])

pessoa['cidade'] = 'João Pessoa'
print(pessoa)
del pessoa['rg']
print(pessoa)
