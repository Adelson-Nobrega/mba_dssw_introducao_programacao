"""
Em um contexto corporativo verificou-se a necessidade de enviar uma mensagem repetidas
vezes para lembrar os profissionais que eles precisam atualizar as senhas de acesso.
Desenvolver código que envie 5 mensagens para lembrar o usuário de atualizar a senha.
"""

usuario = 'lopes_nobre'
senha = '123654'

print('SISTEMA CORPORATIVO INTRANET\n')

for acesso in range(1, 7, 1):
    user = input('Digite seu usuário: ')
    password = input('Digite sua senha: ')
    if user == usuario and password == senha:
        if acesso < 6:
            print(f'\nAcesso ou tentativa nº {acesso}! Após 5 acessos ou tentativas será necessário a troca de senha!')
            print('\nMENU PRINCIPAL')
            print('1 - Trocar senha')
            print('2 - Enviar mensagem')
            print('3 - Sair do Menu (Logout)')

            while True:
                try:
                    opcao = int(input('\nDigite a opção do menu: '))
                except ValueError:
                    print('Opção inválida! Por favor, digite um número.')
                    continue  # Volta para o início do loop 'while'

                if opcao == 1:
                    senha = input('Digite sua nova senha: ')
                    print('Senha alterada com sucesso!')
                elif opcao == 2:
                    mensagem = input('\nEscreva a mensagem a ser enviada: ')
                    print(f'\nMensagem {mensagem.upper()} enviada com sucesso!')
                elif opcao == 3:
                    print('\nSaindo do menu principal...\n')
                    break  # Sai do loop do menu
                else:
                    print('Opção inválida!')
        else:
            print('ATENÇÃO! É OBRIGATÓRIO A TROCA DA SENHA!')
            senha = input('Digite sua nova senha: ')
            print('Obrigado! A segurança agradece!')
    else:
        print('Usuário ou senha inválida!')
