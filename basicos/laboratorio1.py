# La función print_todo necesita imprimir una cadena que use el nombre y los valores del cuerpo de un diccionario.
# Para hacer esto, podemos utilizar la función de impresión y una cadena f (usando Python 3.6 y superior).
# Aquí hay una forma en que podríamos implementar esta función:
todo1 = {'nombre': 'César', 'edad': 41, 'hijos': 3}


def print_todo(todo):
   # print(print_todo(todo))
    print(
        f"{todo1['nombre']}: {todo1['edad']} \ncantidad de hijos: {todo1['hijos']}")


print_todo(todo1)


