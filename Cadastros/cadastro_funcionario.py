import pycep_correios   # Importando modulo PyCEP para busca do CEP na base dos Correios
funcionarios = []
ano_atual = 2019
func_cdg = 1000  # Padrao codigo funcionarios, iniciando no 1000.


def funcionario_insere_nome():
    """
    Função para inserção do nome do cliente, verificando possíveis erros.
    Verifica se o nome possui algum numero.
    """
    while True:
        func_nome = input('Nome: ')
        if (func_nome.isnumeric()) or (not func_nome.isalpha()):
            print('Nome não pode conter numeros, tente novamente.')
        else:
            return func_nome


def funcionario_insere_cpf():
    """
    Função para inserção do CPF do cliente, verificando possíveis erros.
    Verifica se o CPF possui letras ou menos de 11 digitos, padrao no BR.
    """
    while True:
        func_cpf = input('CPF: (Apenas numeros)')
        if not (func_cpf.isnumeric()) or (len(func_cpf) != 11):
            print('CPF inválido. Tente novamente.')
        else:
            return func_cpf


def funcionario_insere_rg():
    """
    Função para inserção do RG do cliente, verificando possíveis erros.
    Verifica se o RG possui alguma letra.
    """
    while True:
        func_rg = input('RG: (Apenas numeros)')
        if not func_rg.isnumeric():
            print('RG nao pode conter letras')
        else:
            return func_rg


def funcionario_insere_data():
    """
    Função para inserção da data de nascimento do cliente, verificando possíveis erros.
    Obtém a idade a partir da subtração do ano atual com o ano de nascimento.
    """
    while True:
        func_dt_nasc = input('Data de nascimento: ').split('/' or ' ')
        if not (func_dt_nasc[0].isnumeric()) or (func_dt_nasc[1].isnumeric()) or (func_dt_nasc[2].isnumeric()):
            func_idade = ano_atual - int(func_dt_nasc[2])
            return func_idade
        else:
            print('Data de nascimento inválida. Tente novamente.')


def funcionario_insere_cep():
    """
    Função para inserção do CEP do cliente, verificando possíveis erros.
    Verifica se o CEP possui alguma letra.
    """
    while True:
        func_cep = input('Digite o CEP (Apenas numeros): ')
        if not func_cep.isnumeric():
            print('CEP incorreto. Verifique e tente novamente.')
        else:
            func_endereco = pycep_correios.consultar_cep(func_cep)
            return func_endereco


def funcionario_insere_telefone():
    """
    Função para inserção do telefone do funcionario, verificando possíveis erros.
    Verifica se o telefone possui alguma letra.
    """
    while True:
        func_tel = input('Digite o telefone com DDD (somente numeros): ')
        if not func_tel.isnumeric():
            print('Telefone não pode possuir letras. Verifique e tente novamente.')
        else:
            return func_tel



def cadastro_funcionario():
    """
    Função para o cadastro do cliente, adicionando um código único a cada cliente.
    Utilizando funcoes definidas anteriormente para o cadastramento.
    """
    global func_cdg
    func_cdg += 1
    print(f'Cadastrando funcionario {func_cdg}')
    func_nome = funcionario_insere_nome()  # 1
    func_cpf = funcionario_insere_cpf()   # 2
    func_rg = funcionario_insere_rg()    # 3
    func_idade = funcionario_insere_data()  # 4
    func_endereco = funcionario_insere_cep()   # 5
    func_tel = funcionario_insere_telefone()
    funcionarios.append([[func_cdg], func_nome, func_cpf, func_rg, func_idade, func_endereco, func_tel])


def consulta_funcionario():
    """
    Função para a consulta do cliente a partir do código único.
    """
    global func_cdg, funcionarios
    consulta = int(input('Codigo: '))
    if consulta in funcionarios:
        print('Cadastrado')
        print(f"""  
Codigo: {funcionarios[0]}
Nome: {funcionarios[1]}
RG: {funcionarios[2]}
CPF: {funcionarios[3]}
Idade: {funcionarios[4]}
Endereco:""")  # Impressão dos dados do cliente consultado
        for key in funcionarios[5]:  # Estrutura deee repeticao para impressao formatada do dicionario ENDEREÇO
            print("{0}\t\t{1}".format(key, funcionarios[5][key]))
    else:
        print('O usuario com este codigo nao consta na base de dados.')
