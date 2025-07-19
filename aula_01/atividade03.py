print('MERCADO DO PROFESSOR MESSI')

# Variáveis
valor = float(input('Qual o valor do produto? '))
desconto = float(input('Qual o percentual de desconto? '))

# Funções e Métodos

# Processamento
valordesc = valor * desconto / 100
valorfinal = valor - valordesc

# Visualização
print(f'Valor do produto com o desconto R$ {valorfinal:.2f}')
