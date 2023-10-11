import pytest
from src.models.restaurant import Restaurant


def test_describe_restaurant():
    rest = Restaurant('outback', 'australiana')
    expected_result = '''Esse restaturante chama Outback and serve comida australiana.
        "Esse restaurante está servindo 0 consumidores desde que está aberto.'''
    actual_result = rest.describe_restaurant()
    assert actual_result == expected_result


def test_open_restaurant():
    rest = Restaurant('outback', 'australiana')
    rest.open_restaurant()
    assert rest.open == True
    assert rest.number_served == 0


def test_open_restaurant_twice():
    rest = Restaurant('outback', 'australiana')
    expected_result = "Outback já está aberto!"
    rest.open_restaurant()
    rest.open_restaurant()
    actual_result = rest.open_restaurant()
    assert actual_result == expected_result


def test_close_restaurant():
    rest = Restaurant('outback', 'australiana')
    rest.open_restaurant()
    rest.close_restaurant()
    assert rest.open == False
    assert rest.number_served == 0


def test_close_restaurant_twice():
    expected_result = "Outback já está fechado!"
    rest = Restaurant('outback', 'australiana')
    rest.open_restaurant()
    rest.close_restaurant()
    actual_result = rest.close_restaurant()
    assert actual_result == expected_result


def test_set_number_served():
    rest = Restaurant('outback', 'australiana')
    rest.open_restaurant()
    rest.set_number_served(10)
    assert rest.open == True
    assert rest.number_served == 10


def test_set_number_served_restaurant_close():
    rest = Restaurant('outback', 'australiana')
    expected_result = "Outback já está fechado!"
    rest.open_restaurant()
    rest.close_restaurant()
    actual_result = rest.set_number_served(10)
    assert actual_result == expected_result


def test_increment_number_served():
    rest = Restaurant('outback', 'australiana')
    rest.open_restaurant()
    rest.set_number_served(10)
    rest.increment_number_served(20)
    assert rest.open == True
    assert rest.number_served == 30


def test_increment_number_servedsss():
    rest = Restaurant('outback', 'australiana')
    expected_result = "Outback já está fechado!"
    rest.open_restaurant()
    rest.close_restaurant()
    actual_result = rest.increment_number_served(20)
    assert actual_result == expected_result
