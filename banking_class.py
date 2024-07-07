from abc import ABC, abstractmethod
from datetime import datetime

class Transaction(ABC):
    @property
    @abstractmethod
    def value(self):
        pass

    def register(self, account):
        account.register(self)

class Deposit(Transaction):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def register(self, account):
        transaction_success = account.depositar(self._value)
        if transaction_success:
            account.historico.add_transaction(self)

class Saque(Transaction):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def register(self, account):
        transaction_success = account.sacar(self._value)
        if transaction_success:
            account.historico.add_transaction(self)

class History:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(
            {
                "tipo": transaction.__class__.__name__,
                "value": transaction.value,
                "date": datetime.now().strftime("%Y-%m-%d"),
            }
        )

class Client:
    def __init__(self, nome, data_nascimento, cpf, endereco, account=None):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.accounts = []

    def make_transaction(self, account, transaction):
        transaction.register(account)

    def add_account(self, account):
        self.accounts.append(account)

    def __str__(self):
        accounts_str = "\n".join(str(account) for account in self.accounts)
        return (f"""Nome: {self.nome} \nData: {self.data_nascimento} \nCPF: {self.cpf} \nEndereco: {self.endereco} 
                \nContas: \n{accounts_str} \n""")

class BankingAccount:
    def __init__(self, agencia, numero, cliente):
        self._saldo = 0
        self._agencia = agencia
        self._numero = numero
        self._cliente = cliente
        self._historico = History()

    @classmethod
    def new_account(cls, cliente, numero):
        return cls(cliente, numero)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, value) -> bool:
        if value > 0 and value <= self._saldo:
            self._saldo -= value
            print(f"Saque de R$ {value:.2f} realizado com sucesso.")
            return True
        elif value == 0:
            print("Por favor insira um valor maior do que 0")
        elif self._saldo < value:
            print("Saldo insuficiente.")
        else:
            print("Valor incorreto, tente novamente.")
        return False

    def depositar(self, value) -> bool:
        if value > 0:
            self._saldo += value
            print(f"Deposito no valor de R$ {value:.2f} realizado com sucesso.")
            return True
        elif value == 0:
            print("Por favor insira um valor maior do que 0")
        else:
            print("Valor incorreto, tente novamente.")
        return False

    def __str__(self):
        return (f"(Agência: {self.agencia} \nNúmero: {self.numero} \nSaldo: R$ {self.saldo:.2f})")

class ContaCorrente(BankingAccount):
    def __init__(self, numero, agencia, cliente, limite=500, limite_saques=3):
        super().__init__(agencia, numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, value) -> bool:
        numero_saques = len([transacao for transacao in self.historico.transactions if transacao["tipo"] == "Saque"])

        excedeu_limite = value > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if value > 0 and not excedeu_limite and not excedeu_saques:
            return super().sacar(value)
        elif excedeu_limite:
            print("Você atingiu o limite máximo de saques diários.")
        elif excedeu_saques:
            print("Você atingiu o limite máximo de saques.")
        else:
            print("Valor incorreto, tente novamente.")
        return False

    def __str__(self):
        return super().__str__()
    