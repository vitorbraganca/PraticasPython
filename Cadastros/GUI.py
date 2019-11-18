"""
Aparência do programa, interface.
"""

# Menus de opcoes
from Cadastros.cadastro_funcionario import cadastro_funcionario
from Cadastros.cadastro_clientes import cadastro_cliente
from Cadastros.cadastro_produtos import cadastro_produtos
from Cadastros.listar import listar_funcionarios, listar_clientes, listar_produtos
from Cadastros.consultar import consultar_funcionario_cod, consultar_clientes_cod, consultar_produtos_cod

menu_principal = """ 
1- Usuario: Gerente
2- Usuario: Vendedor
3- Encerrar aplicação\n
"""
opcoes_funcionario = """
1- Gestao de clientes
2- Deslogar como funcionario\n
"""
opcoes_gerente = """
1- Gestao de funcionarios
2- Gestao de clientes
3- Gestao de produtos
4- Deslogar como gerente\n
"""
menu_funcionario = """
1 - Cadastrar funcionario
2- Consultar funcionario
3- Listar todos funcionarios
4- Editar dados de funcionarios
5- Sair\n
"""
menu_clientes = """
1 - Cadastrar cliente
2- Consultar cliente
3- Listar todos clientes
4- Editar dados de clientes
5- Sair\n
"""
menu_produtos = """
1 - Cadastrar produtos
2- Consultar produtos
3- Listar todos produtos
4- Editar dados de produtos
5- Sair\n
"""
rodape = """Encerrando aplicaçao... Obrigado por usar!

Desenvolvido por:
- Vítor Eduardo Bragança
- Sighy
- Monvar
- Jonathan Kovansky
- Gabriel Flores 

\n
"""


def gestao_funcionario():
    while True:
        print(menu_funcionario)
        op = int(input('OPCAO: '))
        if op == 1:
            cadastro_funcionario()
        elif op == 2:
            while True:
                consultar_funcionario_cod()
                resp = input(
                    'Deseja consultar novamente? ').upper()  # Deixando em caixa alta para reduzir possibilidades
                if resp.startswith('N'):
                    print('Consulta encerrada ')
                    break
                else:
                    print('Nova consulta... ')
        elif op == 3:
            print('Listando todos os dados cadastrados...')
            listar_funcionarios()
            print('Voltando para o menu...')
        elif op == 4:
            print('Funcionalidade em desenvolvimento...')
            print('Voltando para o menu...')
        elif op == 5:
            print('Saindo...')
            break
        else:
            print('Funcao nao encontrada. Tente novamente.')


def gestao_cliente():
    while True:
        print(menu_clientes)
        op = int(input('OPCAO: '))
        if op == 1:
            cadastro_cliente()
        elif op == 2:
            while True:
                consultar_clientes_cod()
                resp = input(
                    'Deseja consultar novamente? ').upper()  # Deixando em caixa alta para reduzir possibilidades
                if resp.startswith('N'):
                    print('Consulta encerrada ')
                    break
                else:
                    print('Nova consulta... ')
        elif op == 3:
            print('Listando todos os dados cadastrados...')
            listar_clientes()
            print('Voltando para o menu...')
        elif op == 4:
            print('Funcionalidade em desenvolvimento...')
            print('Voltando para o menu...')
        elif op == 5:
            print('Saindo...')
            break
        else:
            print('Funcao nao encontrada. Tente novamente.')


def gestao_produtos():
    while True:
        print(menu_produtos)
        op = int(input('OPCAO: '))
        if op == 1:
            cadastro_produtos()
        elif op == 2:
            while True:
                consultar_produtos_cod()
                resp = input('Deseja consultar novamente? ').upper()
                if resp.startswith('N'):
                    print('Consulta encerrada.')
                    break
                else:
                    print('Nova consulta...')
        elif op == 3:
            print('Listando todos os produtos cadastrados...')
            listar_produtos()
        elif op == 4:
            print('Funcionalidade em desenvolvimento...')
            print('Voltando para o menu...')
        elif op == 5:
            print('Saindo...')
            break
        else:
            print('Funcao nao encontrada. Tente novamente.')
