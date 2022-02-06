# Diccionario
#
# Un Diccionario es una estructura de datos y un tipo de dato
# en Python con características especiales que nos permite
# almacenar cualquier tipo de valor como enteros, cadenas,
# listas e incluso otras funciones. Estos diccionarios nos
# permiten además identificar cada elemento por una clave (Key).

cart = {
    "name": "book",
    "quantity": 3,
    "price": 12.50
}

person = {
    "nombre": "César",
    "apellido": "Vargas"
}

print(person)
print(type(person))
print(cart)
print(dir(cart))
print(person.keys())
print(person.items())
print(cart.clear())
print(cart)
del person
print(person)


products = [
    {'name': 'book', 'price': 25.12},
    {'name': 'Salsas', 'price': 5},
    {'pan': "cochas"}
]

print(products)
