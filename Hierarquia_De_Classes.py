class Conta:

    def __init__(self, nome='', codigo=0, valor=0.0):
        self.nome   = nome
        self.codigo = codigo
        self.valor = valor

    def saldo(self, saldo):
        self.saldo = 0.0

    def deposito(self, valor):
        if self.valor > 0.0: 
            self.saldo += self.valor
            print('deposito concluido com sucesso')
        else
            print('valor invalido')          

    def saque(self, valor):


    def transferencia(self, valor):


class ContaCorrente(Conta)
    
class ContaEspecial(Conta)
    
class ContaPoupanca(Conta)
    
