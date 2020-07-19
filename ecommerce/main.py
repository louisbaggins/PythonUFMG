from abc import ABC, ABCMeta, abstractmethod, abstractproperty
from models import Livro, Brinquedo, Eletronico, CestaCompras

def main():
    livro1 = Livro("Senhor dos Aneis", 15.00)
    brinq1 = Brinquedo("Carrinho", 12.99)

    cesta = CestaCompras()
    cesta.adicionar_item(livro1, 3)
    cesta.adicionar_item(brinq1, 4)
 
    cesta.relatorio_final()

if __name__ == '__main__':
    main()