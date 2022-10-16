print('=' * 30)
print('CADASTRO DE PESSOAS')
print('=' * 30)
print('''[ 1 ] - CADASTRAR PESSOA 
[ 2 ] - REMOVER PESSOA
[ 3 ] - VER LISTA
[ 4 ] - LOCALIZAR
[ 5 ] - SAIR''')
print('=' * 30)

lista_pessoas = []

while True:
    opcao = input('ESCOLHE UMA OPÇÃO: ')

    if not opcao.isdigit():
        print('ACEITAMOS APENAS NÚMERO')
        continue
    opcao = int(opcao)

    if opcao == 1:
        entrada = input('DIGITE O NOME: ').upper()
        lista_pessoas.append(entrada)

    elif opcao == 2:
        remover = int(input('ID QUE DESEJA REMOVER: '))
        del(lista_pessoas[remover])

    elif opcao == 3:
        for ordem, lista in enumerate(lista_pessoas):
            print(f'{ordem} - {lista}')

    elif opcao == 4:
        while True:
            localizar_usuario = input('VOCÊ DESEJA OCALIZAR POR [ID/NOME]: ').upper()

            if localizar_usuario == 'ID':
                localizar_id = int(input('ID QUE DESEJA LOCALIZAR: '))
                print(lista_pessoas[localizar_id])
                break

            else:
                print('OPÇÃO ERRADA')

    elif opcao == 5:
        print('FIM')
        break

    else:
        print('ESCOLHA APENAS UMA DAS OPÇÃO ACIMA')