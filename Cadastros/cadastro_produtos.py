produtos = []
prod_cdg = 2000  # Padrao codigo de produto iniciando em 2000.


def prod_insere_nome():
    """
    Função para inserção do nome do produto.
    """
    while True:
        prod_nome = input('Nome: ')
        return prod_nome


def prod_insere_valor():
    """"
    Função para inserção do valor do produto
    """
    while True:
        prod_valor = float(input('Valor unitario do produto (R$/Un): '))
        if prod_valor <  0:
            print('Valor invalido. Tente novamente.')
        else:
            return prod_valor


def prod_insere_qntd():
    """
    Função para inserção da quantidade de entrada no estoque.
    Verificando possiveis erros.
    """
    while True:
        prod_qntd = int(input('Quantidade de entrada: '))
        if prod_qntd < 0:
            print('Valor invalido. Tente novamente.')
        else:
            return prod_qntd

def cadastro_produtos():
    """
    Função para o cadastro do produto, adicionando um código único a cada produto.
    Utilizando funcoes definidas anteriormente para o cadastramento.
    """
    global prod_cdg
    prod_cdg += 1  # 0
    print(f'Cadastrando produto {prod_cdg}')
    prod_nome = prod_insere_nome()  # 1
    prod_valor = prod_insere_valor()  # 2
    prod_qntd = prod_insere_qntd()  # 3
    produtos.append([prod_cdg, prod_nome, prod_valor, prod_qntd])
