from clases import *

civic = Car('4 cilindros', [
    'conductor delantero', 'pasajero delantero', 'conductor trasero',
    'pasajero trasero'
])

print("Caracteristicas: " + str(civic))
print("Motor: " + str(civic.engine))
print("Llantas: " + str(civic.tires))
print("Llantas: " + str(civic.tires[1]))

civic.licence_plate = 'MAZ8848'

print('Matrícula: ' + str(civic.licence_plate))
print("Caracteristicas: " + str(civic))

civic.description()


#c1 = Car('minicooper','1970','MX1')
#print(c1)