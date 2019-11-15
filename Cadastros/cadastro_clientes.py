import pycep_correios   # Importando modulo PyCEP para busca do CEP na base dos Correios
clientes = []
ano_atual = 2019
clnt_cdg = 1000  # Padrao codigo clientes, iniciando no 1000.


def clnt_insere_nome():
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


def clnt_insere_cpf():
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


def clnt_insere_rg():
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


def clnt_insere_data():
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


def clnt_insere_cep():
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


def clnt_insere_telefone():
    """
    Função para inserção do telefone do cliente, verificando possíveis erros.
    Verifica se o telefone possui alguma letra.
    """
    while True:
        clnt_telefone = int(input('Digite o telefone com DDD (apenas numeros): '))
        if clnt_telefone < 11:
            print('Telefone incorreto. Verifique e tente novamente.')
        else:
            return clnt_telefone


def clnt_insere_email():
    """
    Função para inserção do email do cliente.
    """
    clnt_email = input('Insira o e-mail do cliente:')
    return clnt_email


def cadastro_cliente():
    """
    Função para o cadastro do cliente, adicionando um código único a cada cliente.
    Utilizando funcoes definidas anteriormente para o cadastramento.
    """
    global clnt_cdg
    clnt_cdg += 1
    print(f'Cadastrando usuario {clnt_cdg}')
    clnt_nome = clnt_insere_nome()  # 1
    clnt_cpf = clnt_insere_cpf()   # 2
    clnt_rg = clnt_insere_rg()    # 3
    clnt_idade = clnt_insere_data()  # 4
    clnt_endereco = clnt_insere_cep()   # 5
    clnt_telefone = clnt_insere_telefone()  # 6
    clnt_email = clnt_insere_email()  # 7
    clientes.append([clnt_cdg, clnt_nome, clnt_cpf, clnt_rg, clnt_idade, clnt_endereco, clnt_telefone, clnt_email])
