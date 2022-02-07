colores = ['azul', 'verde', 'rojo', 'morado']
count = 1
for color in colores:
    print(str(count) + ". " + color)
    count += 1

for color in colores:
    if color == 'azul':
        print("Si hay color azul se continua con el recorrido del bucle")
        continue
    elif color == 'rojo':
        print("Sí hay rojo se detienen el recorrido del bucle")
        break
    print(color)

punto = (2.1, 3.0, 7)
for valuar in punto:
    print(valuar)

print("\nRecorrido de Diccionario")
edades = {'kevin': 59, 'bob': 40, 'kayla': 21}

for keys in edades:
    print(f"{keys} tiene {edades[keys]} años")

for letras in "mis_carecteres":
    print(letras)

print("\nRecorrido de Tuplas")
lista_de_puntos = [{1, 2}, {2, 3}, {3, 4}]
for x, y in lista_de_puntos:
    print(f"x: {x}, y: {y}")

for nombre, edad in edades.items():
    print(f"Nombre de la persona: {nombre}")
    print(f"\t\tEdad:  {edad}")

print(edades.items())


comidas = ['pan', 'tortillas', 'queso']

for comida in comidas:
    print(comida)

for comida in comidas:
    if comida == 'pan':
        print('Hay pan')
        break
for comida in comidas:
    if comida == 'pan':
        print('Tambien hay tortillas y queso')
        continue

for number in range(0, 10):
    print(number)

for letra in "César":
    print("\t"+letra)
