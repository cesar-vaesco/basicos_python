


def inspect(func):

    def funcion_envuelve(*args, **kwargs):
        # print ('folder {0} already exists'.format(file_name))
        print("corriendo {0}".format(func.__name__))
        val = func(*args, **kwargs)
        print(val)

    return funcion_envuelve


@inspect
def combine(a, b):
    return a + b


class User:
    base_url = 'http://example.com/api'

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    @classmethod
    def query(cls, query_string):
        return cls.base_url + '?' + query_string

    @staticmethod
    def name():
        return 'Cesar Vargas'

    @property
    def full_name(self):
        return f"{self.nombre} {self.apellido}"


inspect(combine(1, b=2))  # salida -> corriendo combine 3

