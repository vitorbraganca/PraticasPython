clientes = []
ano_atual = 2019
clnt_cdg = 1000  # Padrao codigo clientes, iniciando no 1000.


def cadastro_cliente():
    global clnt_cdg
    clnt_cdg += 1
    print(f'Cadastrando usuario {clnt_cdg}')
    clnt_nome = input('Nome: ')
    clnt_cpf = input('CPF (Apenas numeros): ')
    clnt_rg = input('RG (Apenas numeros): ')
    clnt_dt_nasc = input('Data de nascimento: ').split('/' or ' ')
    clnt_idade = ano_atual - int(clnt_dt_nasc[2])
    clientes.append(clnt_cdg)  # 0
    clientes.append(clnt_nome)  # 1
    clientes.append(clnt_rg)  # 2
    clientes.append(clnt_cpf)  # 3
    clientes.append(clnt_idade)  # 4


def consulta_cliente():
    global clnt_cdg, clientes
    consulta = int(input('Codigo: '))
    if consulta in clientes:
        print('Cadastrado')
        print(f"""
    Codigo: {clientes[0]}
    Nome: {clientes[1]}
    RG: {clientes[2]}
    CPF: {clientes[3]}
    Idade: {clientes[4]}""")
    else:
        print('O usuario com este codigo nao consta na base de dados.')


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
        consulta_cliente()
        resp = input('Deseja consultar novamente? ').upper()  # Deixando em caixa alta para reduzir possibilidades
        if (resp == 'N') or (resp == 'NAO'):
            print('Consulta encerrada ')
            break
        else:
            print('Nova consulta... ')
            consulta_cliente()
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
