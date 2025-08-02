# ESTRUTURAS DE REPETIÇÃO

spam = 0
# While é usado para repetir enquanto uma condição é verdadeira
while spam < 5:
    print('Mensagem enviada com sucesso!')
    spam = spam + 1

# For é usado para percorrer uma coleção, limitando-se a quantidade de objetos.
# Indicado para se repetir um bloco de código quando se tem uma quantidade de vezes definida
for spam in range(5):
    print(f'Teste {spam} de for!')

print('\nNúmeros pares de 0 a 10')
for par in range(0, 11, 2): # Metodo range cria uma lista de números começando no argumento 1, terminando no argumento 2 (sem incluí-lo) com o incremento do argumento 3
    print(par)
