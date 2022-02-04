
from traceback import print_last


def hola_mundo():
    print("Hola mundo")


hola_mundo()

# Función con argumentos


def mostrar_nombre(nombre):
    print(f"Mi nombre es {nombre}")


mostrar_nombre("César")


def sumar_dos(num):
    return num + 2


numero = 5
print(f"El resultado de sumar {numero} + 2 es:  {sumar_dos(numero)}")


def suma(num1, num2):
    return num1 + num2


print(suma(5.9, 6))


def tarjeta_contacto(nombre, edad, modelo_coche):
    return f"Mi nombre es {nombre}, tengo {edad} años, y conduzco un automovil marca '{modelo_coche}'"


print(tarjeta_contacto("Cesar", 41, "Ford Fiesta"))


def puedo_manejar(edad, edad_conduciendo=16):
    return edad >= edad_conduciendo


print(puedo_manejar(41))
