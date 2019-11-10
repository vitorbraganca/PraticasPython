import pycep_correios   # Importando modulo PyCEP para busca do CEP na base dos Correios
clientes = []
ano_atual = 2019
clnt_cdg = 1000  # Padrao codigo clientes, iniciando no 1000.


def insere_nome():
    """
    Função para inserção do nome do cliente, verificando possíveis erros.
    Verifica se o nome possui algum numero.
    """
    while True:
        clnt_nome = input('Nome: ')
        if (clnt_nome.isnumeric()) or (not clnt_nome.isalpha()):
            print('Nome não pode conter numeros, tente novamente.')
        else:
            return clnt_nome


def insere_cpf():
    """
    Função para inserção do CPF do cliente, verificando possíveis erros.
    Verifica se o CPF possui letras ou menos de 11 digitos, padrao no BR.
    """
    while True:
        clnt_cpf = input('CPF: (Apenas numeros)')
        if not (clnt_cpf.isnumeric()) or (len(clnt_cpf) != 11):
            print('CPF inválido. Tente novamente.')
        else:
            return clnt_cpf


def insere_rg():
    """
    Função para inserção do RG do cliente, verificando possíveis erros.
    Verifica se o RG possui alguma letra.
    """
    while True:
        clnt_rg = input('RG: (Apenas numeros)')
        if not clnt_rg.isnumeric():
            print('RG nao pode conter letras')
        else:
            return clnt_rg


def insere_data():
    """
    Função para inserção da data de nascimento do cliente, verificando possíveis erros.
    Obtém a idade a partir da subtração do ano atual com o ano de nascimento.
    """
    while True:
        clnt_dt_nasc = input('Data de nascimento: ').split('/' or ' ')
        if not (clnt_dt_nasc[0].isnumeric()) or (clnt_dt_nasc[1].isnumeric()) or (clnt_dt_nasc[2].isnumeric()):
            clnt_idade = ano_atual - int(clnt_dt_nasc[2])
            return clnt_idade
        else:
            print('Data de nascimento inválida. Tente novamente.')


def insere_cep():
    """
    Função para inserção do CEP do cliente, verificando possíveis erros.
    Verifica se o RG possui alguma letra.
    """
    while True:
        clnt_cep = input('Digite o CEP (Apenas numeros): ')
        if not clnt_cep.isnumeric():
            print('CEP incorreto. Verifique e tente novamente.')
        else:
            clnt_endereco = pycep_correios.consultar_cep(clnt_cep)
            return clnt_endereco


def cadastro_cliente():
    """
    Função para o cadastro do cliente, adicionando um código único a cada cliente.
    Utilizando funcoes definidas anteriormente para o cadastramento.
    """
    global clnt_cdg
    clnt_cdg += 1
    print(f'Cadastrando usuario {clnt_cdg}')
    clnt_nome = insere_nome()  # 1
    clnt_cpf = insere_cpf()   # 2
    clnt_rg = insere_rg()    # 3
    clnt_idade = insere_data()  # 4
    clnt_endereco = insere_cep()   # 5
    clientes.append([clnt_cdg, clnt_nome, clnt_cpf, clnt_rg, clnt_idade, clnt_endereco])


def consulta_cliente():
    """
    Função para a consulta do cliente a partir do código único.
    """
    global clnt_cdg, clientes
    consulta = int(input('Codigo: '))
    if consulta in clientes:
        print('Cadastrado')
        print(f"""  
Codigo: {clientes[0]}
Nome: {clientes[1]}
RG: {clientes[2]}
CPF: {clientes[3]}
Idade: {clientes[4]}
Endereco:""")  # Impressão dos dados do cliente consultado
        for key in clientes[5]:  # Estrutura deee repeticao para impressao formatada do dicionario ENDEREÇO
            print("{0}\t\t{1}".format(key, clientes[5][key]))
    else:
        print('O usuario com este codigo nao consta na base de dados.')
