x = int(input("Ingresa número a comparar: "))

print(x < 30)

if x > 30:
    print(f"{x} es mayor que 30")
elif x < 30:
    print(f"{x} es menor que 30")
else:
    print(f"{x} es 30")


color = input("Ingresa un color: ")
color.lower()

if color == 'rojo' or color == 'amarillo' or color == 'azul':
    print(f'Ingreso {color} el cual es un color primario')
else:
    print(f'{color} no es un color primario o no esta claro el dato ingresado')

nombre = input("Ingresa nombre: ")
apellido = input("Ingresa apellido: ")

if nombre == 'César':
    if apellido == 'Vargas':
        print(f'Tu eres {nombre} {apellido}')
    else:
        print('Tu no eres César Vargas')
else:
    print('Tu no eres César')