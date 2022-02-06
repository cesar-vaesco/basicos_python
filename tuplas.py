
#
#
#print(type(mi_tupla))
#print(mi_tupla)
#
#segunda_tupla = tuple((1, 2 , 3))
#print(segunda_tupla)
from cmath import pi

## Las tuplas no sopoertan las reaccinaciones

mi_tupla = (1, 2, 3, 4)
print('\tMétodos de una tupla')
print(dir(mi_tupla))
print('\t Inicializar una tupla de un sólo elemento')
x = (1,2,3,4,5)
print(x)
print('\t Acceder elementos a la tupla')
print(x[1])


localizaciones = {
    (32.156, 39.000): "Tokio",
    (22.156, 37.900): "Nueva York"
}

print(type(localizaciones))

print(localizaciones.get(32.156, 39.000))
print(localizaciones.keys())

print('\t Eliminar  la tupla')
del(x)
print(x)