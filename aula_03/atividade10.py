#JOGO DE ADVINHAÇÃO
import random

number = random.randint(1, 100)
numero = int(input('Tente advinhar um número aleatório entre 1 e 100: '))

while numero != number:
    if numero > number:
        print('\nO número secreto é menor que o escolhido!')
        numero = int(input('\nEscolha um novo número: '))
    elif numero < number:
        print('\nO número secreto é maior que o escolhido!')
        numero = int(input('\nEscolha um novo número: '))

if numero == number:
    print('Parabéns! Você acertou o número!')
