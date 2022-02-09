class Conta:

    def __init__(self,numero,titular,saldo,limite):
        print("Construindo Objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo é {} do titular {}".format(self.__saldo,self.__titular))

    def deposita(self,valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def transfere(self, valor , destino):
        self.saque(valor)
        destino.deposita(valor)
