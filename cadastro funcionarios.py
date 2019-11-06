import pycep_correios   # Importando modulo PyCEP para busca do CEP na base dos Correios
funcionarios = []
ano_atual = 2019
func_cdg = 1000  # Padrao codigo funcionario, iniciando no 1000.


def insere_nome():
    """
    Função para inserção do nome do funcionario, verificando possíveis erros.
    Verifica se o nome possui algum numero.
    """
    while True:
        func_nome = input('Nome: ')
        if (func_nome.isnumeric()) or (not func_nome.isalpha()):
            print('Nome não pode conter numeros, tente novamente.')
        else:
            funcionarios.append(func_nome)  # 1
            break


def insere_cpf():
    """
    Função para inserção do CPF do funcionario, verificando possíveis erros.
    Verifica se o CPF possui letras ou menos de 11 digitos, padrao no BR.
    """
    while True:
        func_cpf = input('CPF: (Apenas numeros)')
        if not (func_cpf.isnumeric()) or (len(func_cpf) != 11):
            print('CPF inválido. Tente novamente.')
        else:
            funcionarios.append(func_cpf)  # 3
            break


def insere_rg():
    """
    Função para inserção do RG do funcionario, verificando possíveis erros.
    Verifica se o RG possui alguma letra.
    """
    while True:
        func_rg = input('RG: (Apenas numeros)')
        if not func_rg.isnumeric():
            print('RG nao pode conter letras')
        else:
            funcionarios.append(func_rg)  # 2
            break


def insere_dting():
    """
    Função para inserção da data de ingresso do funcionario, verificando possíveis erros.
    Obtém a idade a partir da subtração do ano atual com o ano de nascimento.
    """
    while True:
        func_dt_ing = input('Data de ingresso: ').split('/' or ' ')
        if not (func_dt_ing[0].isnumeric()) or (func_dt_ing[1].isnumeric()) or (func_dt_ing[2].isnumeric()):
            funcionarios.append(func_dt_ing)
            break
        else:
            print('Data de nascimento inválida. Tente novamente.')
def insere_data():
    """
    Função para inserção da data de nascimento do funcionario, verificando possíveis erros.
    Obtém a idade a partir da subtração do ano atual com o ano de nascimento.
    """
    while True:
        func_dt_nasc = input('Data de nascimento: ').split('/' or ' ')
        if not (func_dt_nasc[0].isnumeric()) or (func_dt_nasc[1].isnumeric()) or (func_dt_nasc[2].isnumeric()):
            func_idade = ano_atual - int(func_dt_nasc[2])
            funcionarios.append(func_idade)  # 4
            break
        else:
            print('Data de nascimento inválida. Tente novamente.')


def insere_cep():
    """
    Função para inserção do CEP do funcionario, verificando possíveis erros.
    Verifica se o RG possui alguma letra.
    """
    while True:
        func_cep = input('Digite o CEP (Apenas numeros): ')
        if not func_cep.isnumeric():
            print('CEP incorreto. Verifique e tente novamente.')
        else:
            func_endereco = pycep_correios.consultar_cep(func_cep)
            funcionarios.append(func_endereco)   # 5
            break
    return func_endereco
def insere_tel():
    """
    Função para inserção dotelefonedo funcionario, verificando possíveis erros.
    Verifica se o telefone possui alguma letra.
    """
    while True:
        func_tel = input('telefone: ')
        if (func_tel.isalpha()) or (not func_tel.isnumeric()):
            print('telefone não pode conter letras, tente novamente.')
        else:
            funcionarios.append(func_tel)  # 1
            break



def cadastro_funcionarios():
    """
    Função para o cadastro do funcionarios, adicionando um código único a cada cliente.
    Utilizando funcoes definidas anteriormente para o cadastramento.
    """
    global func_cdg
    func_cdg += 1
    print(f'Cadastrando usuario {func_cdg}')
    funcionarios.append(func_cdg)  # 0
    insere_nome()  # 1
    insere_cpf()   # 2
    insere_rg()    # 3
    insere_data()  # 4
    insere_cep()   # 5
    insere_dting() #6
    insere_tel()#7
def consulta_funcionarios():
    """
    Função para a consulta do funcionarios a partir do código único.
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
data de ingresso:{funcionarios[5]}
telefone:{funcionarios[6]}
Endereço:""")  # Impressão dos dados do funcionarios consultado
        for key in funcionarios[5]:  # Estrutura deee repeticao para impressao formatada do dicionario ENDEREÇO
            print("{0}\t\t{1}".format(key, funcionarios[5][key]))
    else:
        print('O usuario com este codigo nao consta na base de dados.')
