import datetime

class ContaBancaria:
    def __init__(self, titular, numero_da_conta, saldo=0):
        self.titular: str = titular
        self.saldo: int = saldo
        # Atributo extra.
        # O numero_da_conta é uma string usada para registra o historico de transferências
        self.numero_conta: str = numero_da_conta
        # Atributo extra.
        # data_de_abertura_da_conta é a data do dia da criação do objeto ContaBancaria específico
        self.data_de_abertura_da_conta = datetime.date.today()
        # Atributo extra.
        # historico_de_transacoes é uma lista contendo todas as transações da conta
        self.historico_de_transacoes = []

    # Deposita um valor na conta
    def depositar(self, valor):
        self.saldo += valor
        self.historico_de_transacoes.append(f"{datetime.datetime.now()} - Depósito de R${valor:.2f}")

    # Saca um valor da conta
    def sacar(self, valor):
        if self.saldo - valor < 0:
            print("Saque Negado! Saldo insuficiente.")
        else:
            self.saldo -= valor
            self.historico_de_transacoes.append(f"{datetime.datetime.now()} - Saque de R${valor:.2f}")

            print(f"Saque de R${valor} efetivado. Saldo atual: R${self.saldo:.2f}")

    # Transfere um valor entre contas
    def transferir(self, valor, conta2):
        if valor <= self.saldo:
            self.saldo -= valor
            conta2.saldo += valor
            self.historico_de_transacoes.append(f"{datetime.datetime.now()} - Transferência de R${valor:.2f} para a conta {conta2.numero_conta}")
            conta2.historico_de_transacoes.append(f"{datetime.datetime.now()} - Recebimento de R${valor:.2f} da conta {self.numero_conta}")
        else:
            print("Saldo insuficiente!")

    # Consulta o saldo atual da conta
    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")
