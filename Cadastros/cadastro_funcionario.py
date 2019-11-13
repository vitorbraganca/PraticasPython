import pycep_correios   # Importando modulo PyCEP para busca do CEP na base dos Correios
funcionarios = []
ano_atual = 2019
func_cdg = 5000  # Padrao codigo funcionarios, iniciando no 5000.


def funcionario_insere_nome():
    """
    Função para inserção do nome do funcionario, verificando possíveis erros.
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
    Função para inserção do CPF do funcionario, verificando possíveis erros.
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
    Função para inserção do RG do funcionario, verificando possíveis erros.
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
    Função para inserção da data de nascimento do funcionario, verificando possíveis erros.
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
    Função para inserção do CEP do funcionario, verificando possíveis erros.
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
        func_tel = int(input('Digite o telefone com DDD (somente numeros): '))
        if func_tel < 10:
            print('Telefone invalido. Verifique e tente novamente.')
        else:
            return func_tel

def funcionario_insere_data_ingresso():
    """
    Função para inserção da data de ingresso do funcionario, verificando possíveis erros.
    """
    while True:
        func_dt_ing = input('Data de ingresso: ').split('/' or ' ')
        if not (func_dt_ing[0].isnumeric()) or (func_dt_ing[1].isnumeric()) or (func_dt_ing[2].isnumeric()):
            return func_dt_ing
        else:
            print('Data de nascimento inválida. Tente novamente.')

def funcionario_insere_funcao():
    """
    Função para inserção da funcao do funcionario.
    """
    func_funcao = input('Funcao: ')
    return func_funcao


def funcionario_insere_cargo():
    """
    Função para inserção do cargo do funcionario.
    """
    func_cargo = input('Cargo: ')
    return func_cargo

def funcionario_insere_salario():
    """
    Função para inserção do salario do funcionario, verificando possíveis erros.
    Verifica se o salario e negativo.
    """
    while True:
        func_salario = float(input('Digite o salario bruto (em R$): '))
        if func_salario < 0:
             print('Salario nao pode ser negativo. Tente novamente')
        else:
            return func_salario


def cadastro_funcionario():
    """
    Função para o cadastro do funcionario, adicionando um código único a cada fundionario.
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
    func_tel = funcionario_insere_telefone()   # 6
    func_cargo = funcionario_insere_cargo()  # 7
    func_funcao = funcionario_insere_funcao()  # 8
    func_salario = funcionario_insere_salario()  # 9
    func_dt_ing = funcionario_insere_data_ingresso()
    funcionarios.append([func_cdg, func_nome, func_cpf, func_rg, func_idade, func_endereco, func_tel, func_cargo, func_funcao, func_salario, func_dt_ing])
