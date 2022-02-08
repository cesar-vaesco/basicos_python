from clases import *
from tire import *

tire = Tire('P', 205, 55, 15, 'Toyo', 'R')
#toyo.description_tire()
tires = [tire, tire, tire, tire]

civic = Car(engine='4-cilindros', tires=tires)

print(civic.description())
print(civic.wheel_circuferencia())
#
#print("Caracteristicas: " + str(civic))
#print("Motor: " + str(civic.engine))
#print("Llantas: " + str(civic.tires))
#print("Llantas: " + str(civic.tires[1]))
#
#civic.licence_plate = 'MAZ8848'
#
#print('Matrícula: ' + str(civic.licence_plate))
#print("Caracteristicas: " + str(civic))
#
#civic.description()

#c1 = Car('minicooper','1970','MX1')
#print(c1)