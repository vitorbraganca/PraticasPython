from Cadastros.cadastro_clientes import *
from Cadastros.cadastro_funcionario import *
from Cadastros.GUI import linha


def listar_clientes():
    for i in clientes:
        print(f'Codigo: {i[0]}')
        print(f'Nome: {i[1]}')
        print(f'CPF: {i[2]}')
        print(f'RG: {i[3]}')
        print(f'Idade: {i[4]}')
        print('Endereço completo: ')
        print(f'Bairro: {i[5]["bairro"]}')
        print(f'CEP: {i[5]["cep"]}')
        print(f'Cidade: {i[5]["cidade"]}')
        print(f'Logradouro: {i[5]["end"]}')
        print(f'UF: {i[5]["uf"]}')
        linha(50)


def listar_funcionarios():
    for i in funcionarios:
        print(f'Codigo: {i[0]}')
        print(f'Nome: {i[1]}')
        print(f'CPF: {i[2]}')
        print('')
        linha(50)

linha(50)
