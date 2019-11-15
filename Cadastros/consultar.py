"""
Código para consulta de funcionarios, clientes e produtos.
"""
from Cadastros.cadastro_funcionario import *
from Cadastros.cadastro_clientes import *
from Cadastros.cadastro_produtos import produtos


def consultar_funcionario_cod():
    """
    Função para a consulta do funcionario a partir do código único.
    """
    consulta = int(input('Consultar: '))
    for elemento in funcionarios:
        if consulta in elemento:
            print('Funcionario está cadastrado. \nExibindo dados...')
            index = funcionarios.index(elemento)
            for i in funcionarios[index]:
                if i == 0: print(f'Codigo: {i}')
                else: print(i)

            #linha(50)
        else:
            print('Funcionario nao encontrado na nossa base de dados.Verifique as informacoes.')


def consultar_clientes_cod():
    """
    Função para a consulta do funcionario a partir do código único.
    """
    consulta = int(input('Consultar: '))
    for elemento in clientes:
        if consulta in elemento:
            print('Usuário está cadastrado. \nExibindo dados...')
            index = clientes.index(elemento)
            for i in clientes[index]:
                print(i)
            #linha(50)
        else:
            print('Usuario nao encontrado na nossa base de dados. Verifique as informacoes.')


def consultar_produtos_cod():
    """
    Função para a consulta do funcionario a partir do código único.
    """
    consulta = int(input('Consultar: '))
    for elemento in produtos:
        if consulta in elemento:
            print('Produto está cadastrado. \nExibindo dados...')
            index = produtos.index(elemento)
            for i in produtos[index]:
                print(i)
            #linha(50)
        else:
            print('Produto nao encontrado na nossa base de dados. Verifique as informacoes.')