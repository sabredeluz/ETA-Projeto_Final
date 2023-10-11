class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self): #1 - incluir retorno do metodo str, e alteracao do restaurant.name
        """Imprima uma descrição simples da instância do restaurante."""
        return f'''Esse restaturante chama {self.restaurant_name} and serve comida {self.cuisine_type}.
        "Esse restaurante está servindo {self.number_served} consumidores desde que está aberto.'''

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        if not self.open:
            self.open = True       # ao abrir o restaurante,  open deveria ser true
            self.number_served = 0 # ao abrir o restaurante number_served deveria ser 0
            return f"{self.restaurant_name} agora está aberto!"
        else:
            return f"{self.restaurant_name} já está aberto!"

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            self.number_served = 0
            return f"{self.restaurant_name} agora está fechado!"
        else:
            return f"{self.restaurant_name} já está fechado!"

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        if self.open:
            self.number_served = total_customers
        else:
            # para manter o padrao, alterei a string para já esta fechado, igual ao metodo close restaurant
            return f"{self.restaurant_name} já está fechado!"


    def increment_number_served(self, more_customers):  # nao deveria ter um decrement number served?

        """Aumenta número total de clientes atendidos por este restaurante."""
        if self.open:
            # o sistema nao estava incrementando a qtd atual, somente reconfigurando o mesmo.
            # para manter o padrao, alterei a string para já esta fechado, igual ao metodo close restaurant
            self.number_served = self.number_served + more_customers
        else:
            return f"{self.restaurant_name} já está fechado!"
