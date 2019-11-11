"""
Código principal do programa
"""
# Importar todos os outros programas a partir do programa GUI
from Cadastro.GUI import *
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
                print('Funcionalidade em desenvolvimento...')
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
                print('Funcionalidade em desenvolvimento')
            elif op == 3:
                print('Funcionalidade em desenvolvimento')
            elif op == 4:
                print('Deslogando como funcionario...')
                break
    elif user == 3:
        print(rodape)
        break
input('Digite algo para sair...')
