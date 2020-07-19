# Nesse exercício você deve criar uma classe Conta para representar uma conta bancária. 
# Essa classe deve receber em seu método inicializador um único parâmetro numero (referente ao número da conta). 
# Durante a instanciação, um atributo saldo deve ser inicializado com valor 0.0. Esses dois parâmetros devem ser privados. 
# Além disso a classe Conta deve possuir dois métodos para a manipulação do saldo: depositar(valor) e sacar(valor).
# O saldo deve ser modificado exclusivamente por esses métodos, que são responsáveis por incrementar e decrementar o saldo atual, respectivamente.

# A classe Conta deve ser especializada em duas outras classes: ContaCorrente e ContaPoupanca.

# A classe ContaCorrente também em seu inicializador o parâmetro taxa (por exemplo, R$ 1,50). Esse atributo é utilizado em seu método específico cobrar_taxa(), que retira o valor da taxa do saldo atual.

# A classe ContaPoupanca também em seu inicializador o parâmetro juros (por exemplo, 0.05). Esse atributo é utilizado em seu método específico aplicar_juros(), que incrementa do saldo de acordo com o percentual.

# A seguir um exemplo de chamada:

# conta_corrente = ContaCorrente(1, 1.50)
# conta_corrente.depositar(10)
# conta_corrente.cobrar_taxa()

class Conta:
    def __init__(self, account_number):
        self.__account_number = account_number
        self.__saldo = 0.0

    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def saldo(self):
        return self.__saldo
    
    def depositar(self, value):
        self.__saldo += value
    
    def sacar(self, value):
        self.__saldo -= value
    

class ContaCorrente(Conta):
    def __init__(self, account_number, fee):
        super().__init__(account_number)
        self.__fee = fee
    
    def cobrar_taxa(self):
        self.sacar(self.__fee)


class ContaPoupanca(Conta):
    def __init__(self, account_number, interest):
        super().__init__(account_number)
        self.__interest = interest

    def aplicar_juros(self):
        interest_value = self.saldo * self.__interest
        self.depositar(interest_value)


def main():
    conta_corrente = ContaCorrente(1, 1.50)
    conta_poupança = ContaPoupanca(2, 0.10)
    print(conta_corrente.saldo)
    print(conta_poupança.saldo)
    conta_corrente.depositar(10)
    conta_poupança.depositar(10)
    print(conta_corrente.saldo)
    print(conta_poupança.saldo)
    conta_corrente.cobrar_taxa()
    conta_poupança.aplicar_juros()
    print(conta_poupança.saldo)
    print(conta_corrente.saldo)


if __name__ == '__main__':
    main()