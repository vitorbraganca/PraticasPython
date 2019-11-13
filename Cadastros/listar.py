from Cadastros.cadastro_clientes import clientes
from Cadastros.cadastro_funcionario import funcionarios

def linha(multi):
    print('-='*multi)


def listar_clientes():
    for i in clientes:
        linha(25)
        print(f'Codigo: {i[0]}')
        print(f'Nome: {i[1]}')
        print(f'CPF: {i[2]}')
        print(f'RG: {i[3]}')
        print(f'Idade: {i[4]}')
        print(f'Telefone: {i[6]}')
        print(f'E-mail: {i[7]}')
        print('Endereço completo: ')
        print(f'Bairro: {i[5]["bairro"]}')
        print(f'CEP: {i[5]["cep"]}')
        print(f'Cidade: {i[5]["cidade"]}')
        print(f'Logradouro: {i[5]["end"]}')
        print(f'UF: {i[5]["uf"]}')
        linha(25)


def listar_funcionarios():
    for i in funcionarios:
        linha(25)
        print(f'Codigo: {i[0]}')
        print(f'Nome: {i[1]}')
        print(f'CPF: {i[2]}')
        print(f'RG: {i[3]}')
        print(f'Idade: {i[4]}')
        print(f'Telefone: {i[6]}')
        print(f'Cargo: {i[7]}')
        print(f'Funcao: {i[8]}')
        print(f'Salario:{i[9]}')
        print(f'Data de ingresso: {i[10]}')
        print('Endereço completo: ')
        print(f'Bairro: {i[5]["bairro"]}')
        print(f'CEP: {i[5]["cep"]}')
        print(f'Cidade: {i[5]["cidade"]}')
        print(f'Logradouro: {i[5]["end"]}')
        print(f'UF: {i[5]["uf"]}')
        linha(25)
    print('Lista finalizada.')
