"""
Código para consulta de funcionarios, clientes e produtos.
"""
from Cadastros.cadastro_funcionario import *
from Cadastros.cadastro_clientes import *


def consultar_funcionario_cod():
    """
    Função para a consulta do funcionario a partir do código único.
    """
    consulta = int(input('Consultar: '))
    for elemento in funcionarios:
        if consulta in elemento:
            print('Usuário está cadastrado. \nExibindo dados...')
            #linha(50)
        else:
            print('Usuario nao encontrado na nossa base de dados.')


def consultar_clientes_cod():
    """
    Função para a consulta do funcionario a partir do código único.
    """
    consulta = int(input('Consultar: '))
    for elemento in clientes:
        if consulta in elemento:
            print('Usuário está cadastrado. \nExibindo dados...')
            #linha(50)
        else:
            print('Usuario nao encontrado na nossa base de dados.')