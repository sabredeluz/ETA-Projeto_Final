from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        if self.flavors:
            msg = "No momento temos os seguintes sabores de sorvete disponíveis:"
            return self.flavors, msg
        else:
            return "Estamos sem estoque atualmente!"

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        if self.flavors:
            if flavor in self.flavors:
                return f"Temos no momento {self.flavors}!"
            else:
                return f"Não temos {flavor}, no momento sorvetes disponiveis {self.flavors}!"
        else:
            return "Estamos sem estoque atualmente!"

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""
        # if self.flavors: # bug caso a sorveteria fique sem nenhum sorvete, o sistema nao permite incluir um novo.
        if flavor in self.flavors:
            return "Sabor já disponivel!"
        else:
            self.flavors.append(flavor)
            return f"{flavor} adicionado ao estoque!"
        #else:
        #    print("Estamos sem estoque atualmente!")

