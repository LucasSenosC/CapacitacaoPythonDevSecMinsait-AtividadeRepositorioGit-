from contabancaria import ContaBancaria

conta1 = ContaBancaria(titular="Lucas Senos", numero_da_conta="12345-6")
conta1.depositar(100.0)
conta1.consultar_saldo()

conta1.sacar(50.0)
conta1.consultar_saldo()

conta2 = ContaBancaria(titular="Daniella Lopes", numero_da_conta="65432-1")
conta1.transferir(25.0, conta2)
conta1.consultar_saldo()
conta2.consultar_saldo()

conta1.transferir(100.0, conta2)

conta1.depositar(75.0)
print(conta1.historico_de_transacoes)

conta1.sacar(100.0)