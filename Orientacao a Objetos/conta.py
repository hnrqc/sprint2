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

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def set_limite(self, limite):
        self.__limite = limite