
import re


demo_list = [1, 'hola', 135, '23', True, [1, 2, 3]]
colores = ['rojo', 'azul', 'morado']
print(demo_list)
print(demo_list[1])
print(colores)
print(colores[2])

print('Hacer una tupla en una lista')
lista_tupla = (1, 2, 3)
print(type(lista_tupla))
print(lista_tupla)
lista = lista_tupla
print(type(lista))
lista_numeros = list((1, 2, 3))
print(type(lista_numeros))
print(lista_numeros)

print('Crear una lista usando un rango')
r = list(range(1, 11))
print(r)

print(dir(colores))
print(len(colores))
print(len(demo_list))
print(demo_list[-1])

print('Existe rojo en la lista colores?')
print('rojo' in colores)
print('azulito' in colores)

print(colores)

colores[0] = 'amarillo'
colores.insert(3, 'rosa')
print(colores)
colores.append('violeta')
print(colores)
colores.reverse()
print(colores)
print("Agregar elementos de una lista a una lista ")
colores.extend(['lila', 'naranja'])
print(colores)
colores.extend(['negro', 'blanco'])
print(colores)
print(len(colores))
colores.insert(5, 'caqui')
print(colores)
colores.insert(-1, 'melon')
print(colores)
colores.remove('rosa')
print(colores)
colores.pop(-1)
print(colores)
print('Remover todos los elementos de la lista')
colores.clear()
print(colores)
print('Ordenar todos los elementos de la lista')
colores = ['rojo', 'azul', 'morado', 'rojo']
colores.sort()
print(colores)
colores.sort(reverse=True)
print(colores)

print(colores.index('rojo'))
print(colores.count('rojo'))