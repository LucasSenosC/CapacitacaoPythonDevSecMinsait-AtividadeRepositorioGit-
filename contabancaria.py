import datetime

class ContaBancaria:
    def __init__(self, titular, numero_da_conta, saldo=0, data_de_abertura_da_conta=None):
        self.titular = titular
        self.saldo = saldo
        self.numero_conta = numero_da_conta
        self.data_abertura = data_de_abertura_da_conta or datetime.date.today()
        self.historico_de_transacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.historico_de_transacoes.append(f"{datetime.datetime.now()} - Depósito de R${valor:.2f}")

    def sacar(self, valor):
        if self.saldo - valor < 0:
            print("Saque Negado! Saldo insuficiente.")
        else:
            self.saldo -= valor
            self.historico_de_transacoes.append(f"{datetime.datetime.now()} - Saque de R${valor:.2f}")

            print(f"Saque de R${valor} efetivado. Saldo atual: R${self.saldo:.2f}")
    
    def transferir(self, valor, conta2):
        if valor <= self.saldo:
            self.saldo -= valor
            conta2.saldo += valor
            self.historico_de_transacoes.append(f"{datetime.datetime.now()} - Transferência de R${valor:.2f} para a conta {conta2.numero_conta}")
            conta2.historico_de_transacoes.append(f"{datetime.datetime.now()} - Recebimento de R${valor:.2f} da conta {self.numero_conta}")
        else:
            print("Saldo insuficiente!")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")
