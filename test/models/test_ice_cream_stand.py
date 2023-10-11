from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    def test_flavors_available(self):
        sabores = ['Chocolate', 'Pistache', 'Flocos', 'Tapioca']
        baccio_de_latte = IceCreamStand('Baccio de latte', 'Italiana', sabores)
        msg_esperada = 'No momento temos os seguintes sabores de sorvete disponíveis:'
        actual_result, actual_msg = baccio_de_latte.flavors_available()
        assert actual_result == sabores
        assert actual_msg == msg_esperada

    def test_flavors_available_empty_list(self):
        sabores = []
        baccio_de_latte = IceCreamStand('Baccio de latte', 'Italiana', sabores)
        msg_esperada = "Estamos sem estoque atualmente!"
        actual_msg = baccio_de_latte.flavors_available()
        assert actual_msg == msg_esperada

    def test_find_flavor(self):
        sabores = ['Chocolate', 'Pistache', 'Flocos', 'Tapioca']
        expected_result = f'Temos no momento {sabores}!'
        baccio_de_latte = IceCreamStand('Baccio de latte', 'Italiana', sabores)
        actual_result = baccio_de_latte.find_flavor('Pistache')
        assert actual_result == expected_result

    def test_find_flavor_not_found(self):
        sabores = ['Chocolate', 'Pistache', 'Flocos', 'Tapioca']
        flavor_not_found = 'Graviola'
        expected_result = f'Não temos {flavor_not_found}, no momento sorvetes disponiveis {sabores}!'
        baccio_de_latte = IceCreamStand('Baccio de latte', 'Italiana', sabores)
        actual_result = baccio_de_latte.find_flavor(flavor_not_found)
        assert actual_result == expected_result

    def test_find_flavor_not_flavor_empty(self):
        sabores = []
        flavor_not_found = 'Graviola'
        expected_result = f'Estamos sem estoque atualmente!'
        baccio_de_latte = IceCreamStand('Baccio de latte', 'Italiana', sabores)
        actual_result = baccio_de_latte.find_flavor(flavor_not_found)
        assert actual_result == expected_result

    def test_add_flavor(self):
        sabores = ['Chocolate', 'Pistache', 'Flocos', 'Tapioca']
        new_flavor = 'Chocolate Belga'
        expected_result = f"{new_flavor} adicionado ao estoque!"
        baccio_de_latte = IceCreamStand('Baccio de latte', 'Italiana', sabores)
        actual_result = baccio_de_latte.add_flavor(new_flavor)
        assert actual_result == expected_result

    def test_add_flavor_in_list(self):
        new_flavor = 'Chocolate Belga'
        sabores = ['Chocolate', 'Pistache', 'Flocos', 'Tapioca']
        baccio_de_latte = IceCreamStand('Baccio de latte', 'Italiana', sabores)
        baccio_de_latte.add_flavor(new_flavor)
        actual_result, msg = baccio_de_latte.flavors_available()
        expected_result = ['Chocolate', 'Pistache', 'Flocos', 'Tapioca', new_flavor]
        assert actual_result == expected_result

    def test_add_flavor_in_empty_list(self):
        new_flavor = 'Chocolate Belga'
        sabores = []
        baccio_de_latte = IceCreamStand('Baccio de latte', 'Italiana', sabores)
        baccio_de_latte.add_flavor(new_flavor)
        actual_result, msg = baccio_de_latte.flavors_available()
        expected_result = [new_flavor]
        assert actual_result == expected_result

    def test_add_flavor_in_twice(self):
        new_flavor = 'Chocolate Belga'
        expected_result = "Sabor já disponivel!"
        sabores = [new_flavor]
        baccio_de_latte = IceCreamStand('Baccio de latte', 'Italiana', sabores)
        actual_result = baccio_de_latte.add_flavor(new_flavor)
        assert actual_result == expected_result
