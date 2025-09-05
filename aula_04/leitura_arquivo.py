# with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# with open('pg1232.txt', 'r', encoding='utf-8') as arquivo:
#     for linha in arquivo:
#         print(linha.rstrip())

with open('pg1232.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

print(type(linhas))
print(linhas)