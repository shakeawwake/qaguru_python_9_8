"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from tests.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(quantity=100) is True

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(quantity=10) is True

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        assert 'Вы можете купить только' in product.buy(quantity=1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, cart, product):
        print(product)
        test = cart.add_product(product, buy_count=20)
        assert 'Продукт добавлен в карзину' in test

    def test_remove_product(self, cart, product):
        cart.add_product(product, buy_count=20)
        remove = cart.remove_product(product, 2)
        assert remove == 18

    def test_get_total_price(self, cart, product):
        cart.add_product(product, buy_count=20)
        price = cart.get_total_price(product)
        assert price == 2000

    def test_buy(self, cart, product):
        cart.add_product(product, buy_count=20)
        buy = cart.buy(product)
        assert f'Вы купили {product.name} за {cart.get_total_price(product)}' in buy

    def test_buy_failed(self, cart, product):
        cart.add_product(product, buy_count=20000)
        buy = cart.buy(product)
        assert f'Вы можете купить только {product.quantity} ед. продукта' in buy

    def test_clear(self, cart, product):
        cart.add_product(product, 20)
        cart.clear()