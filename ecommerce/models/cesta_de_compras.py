from .constants import Constants

class CestaCompras:

    def __init__(self):
        self.itens = dict()

    def adicionar_item(self, item, value):
        if item in self.itens:
            self.itens[item] += value
        else:
            self.itens[item] = value 

    def relatorio_final(self):
        report_info = [
            f'{type(key).__name__}, {key.nome}, {self.itens[key]}, ' + format(key.valor, Constants.FLOAT_QTTY_FORMATTER)
            + ', ' + format(key.valor * self.itens[key], Constants.FLOAT_QTTY_FORMATTER) + ', ' + format(key.calculate_discount() * self.itens[key], Constants.FLOAT_QTTY_FORMATTER)
            for key in self.itens
        ]

        values_with_discount_list = [
            key.calculate_discount() * self.itens[key]
            for key in self.itens
        ]
        total_value_with_discount = sum(values_with_discount_list)
        print(format(total_value_with_discount, Constants.FLOAT_QTTY_FORMATTER))
        for report in report_info:
            print(report)
