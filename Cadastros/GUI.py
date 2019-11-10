from Cadastro.cadastro_clientes import consulta_cliente, cadastro_cliente
from Testes.listar import listar_clientes

while True:
    print("""1- Usuario: Gerente
2- Usuario: Funcionario""")
    user = int(input('Opcao de usuario: '))
    if user == 1:
        print('Funcionalidade em desenvolvimento...')
        print('Voltando para o menu...')
    elif user == 2:
        print('Logando como funcionario.')
        while True:
            print("""1 - Cadastrar cliente
2- Consultar cliente
3- Listar todos clientes
4- Editar dados de clientes
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
                print('Listando todos os dados cadastrados...')
                listar_clientes()
                print('Voltando para o menu...')
            elif op == 4:
                print('Funcionalidade em desenvolvimento...')
                print('Voltando para o menu...')
            elif op == 5:
                print('Saindo...')
                break
            else:
                print('Funcao nao encontrada. Tente novamente.')
