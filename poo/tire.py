import math


class Tire:
    """ 
    Esta clase representa las caracterisitcas de la llanta 
    que usa un automovil
    """

    def __init__(self,
                 tipo_neumatico,
                 ancho,
                 relacion,
                 diametro,
                 marca='',
                 construccion='R'):
        self.tipo_neumatico = tipo_neumatico
        self.ancho = ancho
        self.relacion = relacion
        self.diametro = diametro
        self.marca = marca
        self.construccion = construccion

    def circuferencia(self):
        """ la circuferencia de la llanta en pulgadas
            >>> tire = Tire('P', 205, 65, 15)
            >>> tire.circuferencia()
        """
        side_wall_inches = (self.ancho * (self.relacion / 100)) / 25.4
        total_diametro = side_wall_inches * 2 + self.diametro
        return round(total_diametro * math.pi, 1)

    def description_tire(self):
        print(
            f'Tire({self.tipo_neumatico}, {self.ancho}. {self.relacion},{self.diametro},{self.marca}, {self.construccion})'
        )

    def __repr__(self):
        """ 
        Información general de llanta
        """
        return (f"{self.tipo_neumatico}{self.ancho}/{self.relacion} " +
                f"{self.construccion}/{self.diametro}")

    def _side_wall_inches(self):
        return (self.ancho * (self.relacion / 100)) / 25.4


### Nueva clase
class SnowTire(Tire):

    def __init__(self,
                 tipo_neumatico,
                 ancho,
                 relacion,
                 diametro,
                 espesor_cadena,
                 marca='',
                 construccion='R'):
        super().__init__(tipo_neumatico, ancho, relacion, diametro, marca, construccion)
        self.espesor_cadena = espesor_cadena

    def circuferencia(self):
        """
            The circumference of a tire w/ show chains in inches.
            >>> tire = SnowTire('P', 205, 65, 15, 2)
            >>> tire.circumference()
            92.7
        """
        side_wall_inches = self._side_wall_inches()
        total_diameter = (side_wall_inches +
                          self.espesor_cadena) * 2 + self.diametro
        return round(total_diameter * math.pi, 1)

    def __repr__(self):
        return super().__repr__() + " (Snow)"