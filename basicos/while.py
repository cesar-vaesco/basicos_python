
count = 4

while count <= 10:
    print(f"Count: {count}")
    count += 1

contador = 1
while contador <= 4:
    if contador == 1:
        print("\t")
    print(str(contador) + ". Ciclando.... ")
    contador += 1

print("\t")

contador = 0
while contador < 10:
    if contador % 2 == 0:
        contador += 1
        continue
    print(f"Mostrando números impares: {contador}")
    contador += 1
print(KeyboardInterrupt)
print("Mostrando todos los números: %s" % contador)

count = 1
while count < 10:
    if count % 2 == 0:
        break
    print(f"Mostrando el primer número impar: {count}")
    count += 1
