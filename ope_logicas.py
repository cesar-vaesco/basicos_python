from unicodedata import numeric


print(bool(""))
print(not "")
print(not 1 > 2)
if 1 < 2:
    print("No es mayor")
print('' or 'César')
print('' and 'César')
print('Vero' and 'César')
print('Vero' and '')

nombre = ""
apellido = "Vargas"
if nombre or apellido:
    print("El usuario solo tienen una parte de su nombre")

primer_nombre = nombre or "César"
print(primer_nombre)

if primer_nombre and apellido:
    print("Nombre: " + primer_nombre + "\nApellido: " + apellido)
