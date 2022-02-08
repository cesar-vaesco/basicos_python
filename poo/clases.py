class Car:
    """
    Modelo de carros que cuenta con tipo de llantas y motor
    """

    def __init__(self, engine, tires):
        """ Método constructor"""
        self.engine = engine
        self.tires = tires

    def __repr__(self):
        """Método que imprime los datos del objeto """
        return f'Car({self.engine},{self.tires})'

    def description(self):
        print(f'Este auto es un {self.engine} y cuenta con las siguientes llantas: {self.tires}')

    def wheel_circuferencia(self):
        if len(self.tires) > 0:
            return self.tires[0].circuferencia()
        else:
            return 0





# def __init__(self, name, year, model):
#     self.name = name
#     self.year_built = year
#     self.model = model

#
# def __repr__(self):
#     return f'Car({self.name},{self.year_built},{self.model})'
