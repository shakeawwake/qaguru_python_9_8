from dataclasses import dataclass
from typing import Dict


@dataclass
class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае

        """
        if self.quantity >= quantity:
            return True
        else:
            raise ValueError

    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """

        try:
            self.check_quantity(quantity)
            return True
        except ValueError:
            return f'Вы можете купить только {self.quantity} ед. продукта'

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    #     # Словарь продуктов и их количество в корзине
    products: Dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    #
    def add_product(self, product: Product, buy_count=1):

        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество2
        """
        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count
        return f"Продукт добавлен в карзину"

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if remove_count is None or remove_count >= self.products[product]:
            del self.products[product]
        else:
            self.products[product] -= remove_count
        return self.products[product]

    def clear(self):
        self.products = {}

    def get_total_price(self, product: Product) -> float:
        for key in self.products:
            return self.products[key] * product.price

    #
    def buy(self, product: Product):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        try:
            for key in self.products:
                product.check_quantity(self.products[key])
                return f'Вы купили {product.name} за {self.get_total_price(product)}'
        except ValueError:
            return (f'Вы можете купить только {product.quantity} ед. продукта')
        self.clear()