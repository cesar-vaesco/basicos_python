# declaración de funciones
def saludo():
    print("saludo")


def hola_mundo():
    print("Hola mundo")


def saludo_con_nombre(nombre):
    print(f"saludos {nombre}")


def sumar(num1 = 0, num2= 0):
    return num1 + num2


def parametro_por_defecto(saludo="baboso"):
    print("Saludos " + saludo)

# Instanciación de funciones


# saludo()
# hola_mundo()
#
#nombre = input("Ingresa tu nombre: ")
# saludo_con_nombre(nombre)
num1 = int(input(print('Ingresa un número: ')))
num2 = int(input(print('Ingresa segundo número: ')))

print("Resultado: " + str(sumar(num1, num2)))

parametro_por_defecto()

#
# Función con argumentos
#
#
# def mostrar_nombre(nombre):
#    print(f"Mi nombre es {nombre}")
#
#
# mostrar_nombre("César")
#
#
# def sumar_dos(num):
#    return num + 2
#
#
#numero = 5
#print(f"El resultado de sumar {numero} + 2 es:  {sumar_dos(numero)}")
#
#
# def suma(num1, num2):
#    return num1 + num2
#
#
#print(suma(5.9, 6))
#
#
# def tarjeta_contacto(nombre, edad, modelo_coche):
#    return f"Mi nombre es {nombre}, tengo {edad} años, y conduzco un automovil marca '{modelo_coche}'"
#
#
#print(tarjeta_contacto("Cesar", 41, "Ford Fiesta"))
#
#
# def puedo_manejar(edad, edad_conduciendo=16):
#    return edad >= edad_conduciendo
#
#
# print(puedo_manejar(41))
#
