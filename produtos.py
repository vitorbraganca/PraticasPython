produtos = []
produto_cdg = 1  # Padrao codigo de produto, iniciando no 1.


def insere_nome():
    """
    Função para inserção do nome do produto a ser cadastrado, verificando possíveis erros.
    Verifica se o nome possui algum numero.
    """
    while True:
        produto_nome = input('produto: ')
        if (produto_nome.isnumeric()) or (not produto_nome.isalpha()):
            print('o produto não pode conter numeros, tente novamente.')
        else:
            produtos.append(produto_nome)  # 1
            break


def insere_dt_coleta():
    """
    Função para inserção da data de coleta do produto, verificando possíveis erros.
    Verifica se o produto possui letras
    """
    while True:
        produto_dt_coleta= input('data de coleta: (Apenas numeros)')
        if not (produto_dt_coleta.isnumeric()):
            print('data de coleta inválida. Tente novamente.')
        else:
            produtos.append(produto_dt_coleta)  # 3
            break

def insere_data():
    """
    Função para inserção da data de validade do produto, verificando possíveis erros.
    """
    while True:
        produto_dt_val = input('Data de validade: ').split('/' or ' ')
        if not (produto_dt_val[0].isnumeric()) or (produto_dt_val[1].isnumeric()) or (produto_dt_val[2].isnumeric()):
                 # 4
            break
        else:
            print('Data de validade inválida. Tente novamente.')

def insere_peso():
     """
    Função para inserção da peso do produto, verificando possíveis erros.
     """
     while True:
        produto_peso = input('peso do produto: ').split('/' or ' ')
        if not (produto_peso[0].isnumeric()) or (produto_peso[1].isnumeric()) or (
        produto_peso[2].isnumeric()):
             # 5
             break
        else:
            print('peso do produto inválida. Tente novamente.')



def cadastro_produtos():
    """
    Função para o cadastro dos produtos, adicionando um código único a cada produto.
    Utilizando funcçes definidas anteriormente para o cadastramento.
    """
    global produto_cdg
    produto_cdg += 1
    print(f'Cadastrando de produtos {produto_cdg}')
    produtos.append(produto_cdg)  # 0
    insere_nome()  # 1
    insere_dt_coleta() # 2
    insere_data()  # 3
    insere_peso()#5

def consulta_produtos():
    """
    Função para a consulta dos produtos a partir do código único.
    """
    global produto_cdg, produtos
    consulta = int(input('Codigo: '))
    if consulta in produtos:
        print('Cadastrado')
        print(f"""  
Codigo: {produtos[0]}
Nome: {produtos[1]}
data de coleta: {produtos[2]}
data de validade: {produtos[3]} 
peso:{produtos[4]}
""")
