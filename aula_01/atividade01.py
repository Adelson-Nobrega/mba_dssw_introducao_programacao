mensagem = 'Eu amo programar em Python'
print(mensagem)
print(mensagem.title()) # Primeira letra de cada palavra em caixa alta
print(mensagem.upper()) # Caixa alta
print(mensagem.lower()) # Caixa baixa

print("Adelson Nóbrega")
print("\tAdelson Nóbrega") # Tabulação
print("Adelson\nNóbrega") # Quebra de linha

nome = "         Adelson          "
print(nome)
print(nome.lstrip()) # Remoção de espaços em branco
print(nome.strip())

pi = 3.14141414141414
print("O valor de PI é {:0.2f}".format(pi))
print(f"O valor de PI é {pi}")
print(f"O valor de PI é {pi:0.2f}")

idade = 18
print('Eu tenho %d anos' % idade)

nome = 'adelson'
print('Meu nome é %s' % nome)

fruta = 3.75
print('O abacate custa R$ %.2f' % fruta)
