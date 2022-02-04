
# Formas de escribir strings
print("César")
print('César')
print('''César''')
print("""César""")

# Identificar tipos de datos
print(type("César"))
print(type(500))

# Concatenar strings
print("Vero" + " Cortéz")

# Números
print(type(30))
print(30)

# Float
print(type(3.5))
print(3.5)

# Boolean
print(type(True))
print(True)
print(type(False))
print(False)

# Lista de datos
lista = [10, 20, 30, 40, 50, 60]
saludos = ['Hola', 'Adios', 'Bye']
mezcla_datos = [10, "Hola", 50]
print(lista)
print(saludos)
print(mezcla_datos)


# Tupla
mi_tupla = (10, 20, 30, 40, 50, 60)
tupla_vacia = ()
print(type(mi_tupla))
print(mi_tupla)
print(type(tupla_vacia))
print(tupla_vacia)


# Diccionarios clave: valor
mi_diccionario = {"nombredelapersona": "César",
                  "apellido": "vargas", "apodo": "Chicharo", "edad": 41}
print(type(mi_diccionario))
print(mi_diccionario)

# Tipo de dato None
print(type(None))