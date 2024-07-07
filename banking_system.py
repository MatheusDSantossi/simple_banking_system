# from datetime import datetime
from banking_class import Client, BankingAccount, ContaCorrente, History, Transaction, Deposit, Saque

# Goals 3 operations deposito, saque e extrato

""" 
v2
Criar duas novas funções: cadastrar usuário (cliente do banco) 
e criar conta corrente (vincular com usuário)
usuario (em uma lista) composto por nome, data de nascimento
cpf e endereço (uma string com o formato: logradouro, n°
bairro, cidade/sigla e estado) deve ser armazenado somente
os números do CPF (não podendo ter 2 usuário com o
mesmo cpf)

conta corrente (em uma lista) composto por agência
numero da conta e usuario. O numero da conta é sequencial, 
iniciando em 1. O numero da agencia é fixo, um usuario
pode ter mais de uma conta, porém, uma conta pertence
somente a um usuário (1->n)
"""

from typing import Any


clients = []

nome = ""
data_nascimento = ""
cpf = ""
endereco = ""

agencia = 0
numero_conta = 1

saldo = 0
daily_limit = 500
extrato = ""
numero_saques = 0
saques = []
depositos = []


def cadastrar_cliente():
    print("-------------Faça seu cadastro")

    nome = str(input("Digite seu nome: "))
    cpf = str(input("Digite seu cpf: "))
    data_nascimento = str(input("Digite sua data de nascimento (dd/mm/yyyy): "))
    endereco = str(input("Digite seu endereço: "))

    if (len(clients) > 0):
        for i in clients:
            if (cpf == i.cpf):
                print("CPF já cadastrado!")
                return
            else:

                client = Client(nome, data_nascimento, cpf, endereco)
                clients.append(client)
                return
    elif (len(clients) == 0):
        client = Client(nome, data_nascimento, cpf, endereco)
        clients.append(client)
        print("Cliente cadastrado com sucesso!")
        return
    
    else:
        print("Opção inválida!")

def cadastrar_account():
    global numero_conta
    print("-------------> Faça o cadastro da sua conta")

    cpf = str(input("Digite seu cpf: "))

    client = next((client for client in clients if client.cpf == cpf), None)

    # if (len(clients) > 0):
        # for i in clients:
            # if (cpf == i.cpf):
    if client:
        # account = BankingAccount("0001", numero_conta)
        account = ContaCorrente("0001", numero_conta, client)
        numero_conta += 1
        client.add_account(account)
                
    else:
        print("CPF incorreto")

    # elif (len(clients) == 0):
    #     print("Nenhum cliente cadastrado")
    #     return
    
    # else:
    #     print("Opção inválida!")


def listar_client(cpf):
    # if (len(clients) == 0):
    #     print("Nenhum cliente cadastrado!")
    #     return
    # elif (len(clients) > 0):
    #      for i in clients:
    #          if (i.cpf == cpf):
    #             print(i)
    # else:
    #     print("Opção inválida!")
    client = next((client for client in clients if client.cpf == cpf), None)
    if client:
        print(client)
    else:
        print("CPF incorreto")

def listar_accounts(cpf):
    # if (len(clients) == 0):
    #     print("Nenhuma conta cadastrada!")
    #     return
    # elif (len(clients) > 0):
    #     for i in clients:
    #         if (i.cpf == cpf):
    #              for j in i.accounts:
    #                 print(j)
    #                 return
             
    #     print("Nenhuma conta cadastrada nesse CPF")
    #     return
    client = next((client for client in clients if client.cpf == cpf), None)

    if client:
        for account in client.accounts:
            print(account)
    else:
        print("Cliente não encontrado")

def client_menu(client):
    menu_client = """
    -----------------------------ATM--------------------------
    1- Saque
    2- Deposito
    3- Extrato

    4- Sair
    """

    while(True):

        print(menu_client)

        option = str(input("Digite a opção desejada: "))

        if option.lower() == "1":
            
            agency_number = int(input("Digite o número da agência: "))

            for account in client.accounts:
                if account.agencia == agency_number:
                    value = float(input("Digite o valor do saque: "))

                    client.make_transaction(account, Saque(value))
                    
                
                else:
                    print("Conta não encontrada")

            
        elif option.lower() == "2":

            agency_number = int(input("Digite o número da agência: "))

            for account in client.accounts:
                if account.agencia == agency_number:
                    value = float(input("Digite o valor do deposito: "))

                    client.make_transaction(account, Deposit(value))

                else:
                    print("Conta não encontrada")
                

            # client.make_transaction(client.accounts[0], Deposit(value))
        elif option.lower() == "3":
            agency_number = int(input("Digite o número da agência: "))

            for account in client.accounts:
                print(account.agencia)
                if account.agencia == agency_number:

                    # exibir_extrato(client, client.accounts[0].saldo)
                    exibir_extrato(client, account.saldo)
                    
                else:
                    print("Conta não encontrada")
            # print("\n=================== EXTRATO =================")

            # if (saldo == 0 and len(saques) == 0 and len(depositos) == 0):
            #     print("Não foram feitas movimentações")
            #     print(f"\nSaldo - R$ {saldo:.2f} \n")
            # else:
            #     for i in depositos:
            #         extrato += f"{i} \n"

            #     for j in saques:
            #         extrato += f"{j} \n"
                
            #     saldo_msg = f"\nSaldo - R$ {saldo:.2f} \n" 
            
            #     extrato += saldo_msg

            #     print(extrato)
            
            # print("\n ===========================================")    
            


        elif option.lower() == "4":
            print("Operação finalizada. Volte sempre!")
            break
        else:
            print("Opção inválida tente novamente")

# def exibir_extrato(saldo, /, *, extrato):
def exibir_extrato(client, saldo):

    print("\n================ EXTRATO ================")
    if len(client.accounts) == 0:
        print("Não foram realizadas movimentações." if not extrato else extrato)
    else:
        for account in client.accounts:
            print(account.historico.transactions)

    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def acessar_conta(cpf):
    client = next((client for client in clients if client.cpf == cpf), None)

    # if (len(clients) == 0):
    #     print("Nenhum cliente ou conta cadastrada!")
    #     return
    # elif (len(clients) > 0): 
    #     for i in clients:
    #         if i.cpf == cpf:
    if client:
        client_menu(client)
    else:
        print("Cliente não encontrado.")

while True:

    menu_everyone = """
    ----------------------------- Banco Santos --------------------------
    1- Cadastrar Cliente
    2- Criar Conta Corrente
    3- Listar Clientes
    4- Listar Contas
    5- Acessar Conta

    6- Sair

    """
    print(menu_everyone)
    
    option_initial_menu = str(input("Digite a opção desejada: "))

    if option_initial_menu == "1":
        cadastrar_cliente()
    elif option_initial_menu == "2":
        cadastrar_account()
    elif option_initial_menu == "3":
        listar_client(input("Digite seu CPF: "))
    elif option_initial_menu == "4":
        listar_accounts(input("Digite seu CPF: "))
    elif option_initial_menu == "5":
        cpf_to_access = input("Digite seu CPF: ")
        acessar_conta(cpf_to_access)
    elif option_initial_menu == "6":
        print("Obrigado por confiar no nosso banco!")
        break
    else:
        print("Opção inválida!")
