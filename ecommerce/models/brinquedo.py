from .item import Item
from .constants import Constants


class Brinquedo(Item):
    def __init__(self, name, value):
        super().__init__(name, value)
        self._discount_fee = Constants.TOY_DISCOUNT_FEE

    def calculate_discount(self):
        value_with_discount = self.valor * (Constants.TOTAL_VALUE_PCT - self._discount_fee)
        return value_with_discount