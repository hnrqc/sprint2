class Conta:

    def __init__(self,numero,titular,saldo,limite):
        print("Construindo Objeto...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Saldo é {} do titular {}".format(self.saldo,self.titular))

    def deposita(self,valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

