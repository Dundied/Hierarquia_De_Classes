class Conta:

    def __init__(self, nome='', codigo=0, saldo=0.0):
        self.nome = nome
        self.codigo = codigo
        self.saldo = saldo

    def consultar_saldo(self):
        print(f"Saldo em conta: {self.saldo}")

    def deposito(self, valor):
        if valor > 0.0:
            self.saldo += valor
            print('Depósito concluído com sucesso')
        else:
            print('Valor inválido')

    def saque(self, valor):
        if valor > 0.0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f'Saque realizado no valor de {valor}')
            else:
                print('Saldo insuficiente')
        else:
            print('Valor inválido')

    def transferencia(self, valor, outra_conta):
        if valor > 0.0:
            if self.saldo >= valor:
                self.saldo -= valor
                outra_conta.deposito(valor)
                print(f'Transferência de {valor} realizada com sucesso para a conta de {outra_conta.nome}')
            else:
                print('Saldo insuficiente')
        else:
            print('Valor inválido')


class ContaCorrente(Conta):
    def __init__(self, nome='', codigo=0, saldo=0.0, limite=0.0):
        super().__init__(nome, codigo, saldo)
        self.limite = limite

    def saque(self, valor):
        if valor > 0.0:
            if self.saldo + self.limite >= valor:
                self.saldo -= valor
                print(f'Saque realizado no valor de {valor}')
            else:
                print('Limite de saldo + limite de crédito ultrapassado')
        else:
            print('Valor inválido')


class ContaEspecial(Conta):
    def __init__(self, nome='', codigo=0, saldo=0.0, bonus=0.0):
        super().__init__(nome, codigo, saldo)
        self.bonus = bonus

    def deposito(self, valor):
        if valor > 0.0:
            self.saldo += valor
            self.bonus += valor * 0.01
            print('Depósito e cálculo de bônus concluídos com sucesso')
        else:
            print('Valor inválido')


class ContaPoupanca(Conta):
    def __init__(self, nome='', codigo=0, saldo=0.0, juros=0.0):
        super().__init__(nome, codigo, saldo)
        self.juros = juros

    def aplicar_juros(self):
        self.saldo += self.saldo * (self.juros / 100)
        print('Juros aplicados com sucesso')

#main
    # Criando algumas contas de exemplo
    conta_corrente = ContaCorrente(nome="Fulano", codigo=1, saldo=1000.0, limite=500.0)
    conta_especial = ContaEspecial(nome="Ciclano", codigo=2, saldo=2000.0, bonus=20.0)
    conta_poupanca = ContaPoupanca(nome="Beltrano", codigo=3, saldo=5000.0, juros=1.5)

    # Exemplo de operações com as contas
    print("Saldo inicial das contas:")
    conta_corrente.consultar_saldo()
    conta_especial.consultar_saldo()
    conta_poupanca.consultar_saldo()

    conta_corrente.deposito(500)
    conta_especial.deposito(1000)
    conta_poupanca.deposito(2000)

    conta_corrente.saque(700)
    conta_especial.saque(1500)
    conta_poupanca.saque(3000)

    conta_corrente.consultar_saldo()
    conta_especial.consultar_saldo()
    conta_poupanca.consultar_saldo()

    # Transferência de uma conta para outra
    print("\nTransferência entre contas:")
    conta_corrente.transferencia(300, conta_especial)
    conta_especial.consultar_saldo()

    # Aplicação de juros na conta poupança
    print("\nAplicando juros na conta poupança:")
    conta_poupanca.aplicar_juros()
    conta_poupanca.consultar_saldo()