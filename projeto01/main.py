def listar_sh(lista):
    tam_sh = len(lista)
    for i in range(tam_sh):
        print(f'[{i}] - {lista[i][0]} - {lista[i][1]}')

lista_sh = [
    ['Hulk', 'Super força'],
    ['Homem de ferro', 'Traje especial'],
    ['Capitão América', 'Escudo indestrutível'],
    ['Thor', 'Martelo de poder'],
    ['Gavião Arqueiro', 'Arco e flechas explosivas']
]

while True:
    print('\n#### SISTEMA DE SUPER HERO ####')
    print('1 - Cadastrar')
    print('2 - Alterar')
    print('3 - Deletar')
    print('4 - Listar')
    print('0 - Sair')

    op = int(input('\nDigite a opção desejada: '))

    if op == 1:
        print('#### CADASTRO DE SUPER HEROS ####')
        nome = input('Digite o nome do Super Hero: ')
        poder = input('Digite o poder do Super Hero: ')
        lista_sh.append([nome, poder])

    elif op == 2:
        print('#### ALTERAR UM SUPER HERO ####')
        listar_sh(lista_sh)

        op_alt = int(input('Digite o herói a ser alterado: '))
        nome = input('Digite o novo nome do Super Hero: ')
        poder = input('Digite o novo poder do Super Hero: ')
        lista_sh[op_alt] = [nome, poder]

    elif op == 3:
        print('#### DELETAR UM SUPER HERO ####')
        listar_sh(lista_sh)

        op_del = int(input('Digite o herói a ser deletado: '))

        del lista_sh[op_del]

    elif op == 4:
        print('#### LISTA DE SUPER HEROS ####')
        listar_sh(lista_sh)

    elif op == 0:
        print('Sistema finalizado!')
        break

    else:
        print('Opção inválida!')
