"""
Código principal do programa
"""

# Importar todos os outros programas a partir do programa GUI

try:
    from Cadastros.GUI import *
except ImportError:
    from Cadastros.GUI import menu_principal, gestao_cliente, opcoes_funcionario, opcoes_gerente, gestao_funcionario, rodape


while True:
    print(menu_principal)
    user = int(input('Opcao de usuario: '))
    if user == 1:   # Gerente
        print('Logando como gerente.')
        while True:
            print(opcoes_gerente)
            op = int(input('OPCAO: '))
            if op == 1:
                gestao_funcionario()
            elif op == 2:
                gestao_cliente()
            elif op == 3:
                gestao_produtos()
            elif op == 4:
                print('Deslogando...')
                break

    elif user == 2:  # Funcionario
        print('Logando como funcionario.')
        while True:
            print(opcoes_funcionario)
            op = int(input('OPCAO: '))
            if op == 1:
                gestao_cliente()
            elif op == 2:
                print('Deslogando como funcionario...')
                break
            else: 
                print('Funcao não encontrada.')
    elif user == 3:
        print(rodape)
        break
input('Digite algo para sair...')
