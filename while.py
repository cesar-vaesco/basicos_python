contador = 1
while contador <= 4:
    print(str(contador) + ". Ciclando.... ")
    contador += 1

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
