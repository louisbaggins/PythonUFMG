from abc import ABC, abstractmethod

class Item(ABC):

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def nome(self):
        return self.__nome

    @property
    def valor(self):
        return self.__valor

    @abstractmethod
    def calculate_discount(self):
        raise NotImplementedError('Method not implemented')
