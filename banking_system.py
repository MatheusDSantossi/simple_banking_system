# from datetime import datetime

# Goals 3 operations deposito, saque e extrato

""" 
permitir realizar apenas 3 saques
diários com o limite máximo de 500
por saque. Caso não tenha saldo na
será exibindo a mensagem explicando
armazenar todos os saques e depositos
para mostrar no extrato depois

Já no extrato deve der exibido
todos os depósitos e saques na conta
e depois ser exibido o saldo atual da
mesma

Os valores dever ser exibidos 
utilizando o formato R$ xxx.xx 
"""
saldo = 0
daily_limit = 500
extrato = ""
numero_saques = 0
saques = []
depositos = []
LIMITE_SAQUES = 3

menu = """
-----------------------------ATM--------------------------
1- Saque
2- Deposito
3- Extrato

4- Sair
"""

def saque(value):
    # now = datetime.now()
    global saldo
    global numero_saques
    global LIMITE_SAQUES

    if (value > 0 and numero_saques < LIMITE_SAQUES and value <= saldo):
        saldo -= value
        saque_str = f"Saque - R$ {value:.2f}"
        saques.append(saque_str)
        numero_saques += 1
        print(f"Saque de R$ {value:.2f} realizado com sucesso.")

    elif (value == 0):
        print("Por favor insira um valor maior do que 0")

    elif (numero_saques > LIMITE_SAQUES):
        print("Você atingiu o limite máximo de saques diários.")

    elif (saldo < value):
        print("Saldo insuficiente.")

    else:
        print("Valor incorreto, tente novamente.")

def depositar(value):
    global saldo

    if (value > 0):
        
        saldo += value
        deposito_str = f"Deposito - R$ {value:.2f}"
        depositos.append(deposito_str)
        print(f"Deposito no valor de R$ {value:.2f} realizado com sucesso.")

    elif (value == 0):
        print("Por favor insira um valor maior do que 0")
    
    else:
        print("Valor incorreto, tente novamente.")


while(True):

    print(menu)

    option = str(input("Digite a opção desejada: "))

    if option.lower() == "1":
        
        value = float(input("Digite o valor do saque: "))

        saque(value)
        
    elif option.lower() == "2":
        value = float(input("Digite o valor a ser depositado: "))

        depositar(value)
    elif option.lower() == "3":

        print("\n=================== EXTRATO =================")

        if (saldo == 0 and len(saques) == 0 and len(depositos) == 0):
            print("Não foram feitas movimentações")
            print(f"\nSaldo - R$ {saldo:.2f} \n")
        else:
            for i in depositos:
                extrato += f"{i} \n"

            for j in saques:
                extrato += f"{j} \n"
            
            saldo_msg = f"\nSaldo - R$ {saldo:.2f} \n" 
        
            extrato += saldo_msg

            print(extrato)
        
        print("\n ===========================================")    
        


    elif option.lower() == "4":
        print("Operação finalizada. Volte sempre!")
        break
    else:
        print("Opção inválida tente novamente")


     
# conta = {'Saldo': 0, 'Saque': [], 'Deposito': []}
