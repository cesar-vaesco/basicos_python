print(1 < 2)    # true
print(1 > 2)    #False
print(1 <= 2)   #True
print(1 >= 2)   #False
print(1 == 2)   #False
print(1 == 1)   #True
print(1 == 1.0) #True
print('a' == 'a') #True
print('a' == 'A') #False
print(3.1 == 'A') #False
#print(3.1 >= 'this') #No son tipos de datos compatibles
print('a' > 'b') #False
print('a' != 'b') #True
print(2 in [1,2,3]) # 2 esta en 
print(4 in [1,2,3]) # 4 esta en
print(2 not in [1,2,3]) # 2 no esta en 
print(4 not in [1,2,3]) # 4 no esta en 
if True:
    print("Es Verdadero")
if 1 > 2:
    print("Uno es mayor que 2")
else:
    print("Uno es menor que 2")
    print("Siguiente línea...")
    
nombre = 'Nicanor'
if len(nombre) >= 6:
    print(nombre + ", tu nombre cuenta con más de 5 letras ")
elif len(nombre) == 5:
    print(nombre + ", tu nombre cuenta con 5 letras")
else:
    print(nombre+ ", tu nombre consta de menos de 5 letras")

