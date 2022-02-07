
# Set es una coleccón desordenada la cúal no tiene un indice


colores = {'rojo', 'azul', 'morado'}
print(type(colores))
#Buscar elementos en un Set
print('rojo' in colores)
#Agregar elementos
colores.add('Violeta')
print(colores)
#Remover elementos
colores.remove('Violeta')
print(colores)
#Limpiar un set
colores.clear()
print(colores)
#Eliminar un set
del colores
print(colores)