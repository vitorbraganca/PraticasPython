from Cadastros.cadastro_produtos import prod_cdg
from Cadastros.cadastro_produtos import produtos

#Inserir codigo do produto
#Puxar valores da unidade
#Inserir quantidade do produto
#Somar e imprimir valor

venda = []


def Venda_a():
    while True:
        print("""1 - Inserir produto; 
2 - Valor da conta: 
3 - Fechar""")
        op = int(input('OPÇÂO: '))
        if op == 1:
            while True: #Entrar em loop para não haver repetição de interface
                inserirP = int(input('Digite o codigo do produto: '))
                for elemento in produtos:
                    if inserirP in elemento:
                        indexx = len(produtos)
                        #tem que puxar tudo do produto
                        qntd_p = int(input('Digite a quantidade deste produto:'))
                        preco = qntd_p * #buscar quantidade do produto cadastrado
                        print(preco) #Apenas para ver resultado

                        #Busca em produtos peso, nome, qntd
                        #diminuir qntd, mutiplicar pra ter valor e imprimir com nome
                        #Nome        (15X1.16) xxxx
                        return inserirP
                        print(qntd_p)
            
        
                    else:
                        print('Deu merda.')
        elif op == 2:
            #Printa formatado a nota da conta
        elif op == 3:
            #Fechar compra
        else:
            print('Ocorreu um erro! Tente novamente.')
