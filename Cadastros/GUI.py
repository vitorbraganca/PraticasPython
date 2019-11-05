from Cadastro import cadastro_clientes
while True:
    print("""1 - Cadastrar
2- Consultar
3- Listar todos
4- Editar dados
5- Sair""")
    op = int(input('OPCAO: '))
    if op == 1:
        cadastro_cliente()
    elif op == 2:
        while True:
            consulta_cliente()
            resp = input('Deseja consultar novamente? ').upper()  # Deixando em caixa alta para reduzir possibilidades
            if resp.startswith('N'):
                print('Consulta encerrada ')
                break
            else:
                print('Nova consulta... ')
    elif op == 3:
        print('Funcionalidade em desenvolvimento...')
        print('Voltando para o menu...')
    elif op == 4:
        print('Funcionalidade em desenvolvimento...')
        print('Voltando para o menu...')
    elif op == 5:
        print('Saindo...')
        break
    else:
        print('Funcao nao encontrada. Tente novamente.')
input('Pressione qualquer tecla para sair...')
