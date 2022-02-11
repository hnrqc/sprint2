class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo Objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo é {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar (self, valor_a_sacar):
        valor_disponivel_para_saque = self.__saldo+self.__limite
        return valor_a_sacar <= valor_disponivel_para_saque

    def saque(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Você Não tem saldo disponivel para esta operação, seu saldo atual é R${} e seu limite atual é R${}".format(self.__saldo,self.__limite))


    def transfere(self, valor, destino):
        self.saque(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
