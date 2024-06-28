class Client:
    def __init__(self, nome, data_nascimento, cpf, endereco, account=None):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.accounts = [account] if account else []

    def __str__(self):
        return (f"Nome: {self.nome} \nData: {self.data_nascimento} \nCPF: {self.cpf} \nEndereco: {self.endereco} \n Conta: {self.accounts} \n")

class BankingAccount:
    def __init__(self, agencia, numero):
        self.agencia = agencia
        self.numero = numero

    def __str__(self):
        return (f"Agência: {self.agencia} \nNúmero: {self.numero}")