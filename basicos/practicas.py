ages = {'César': 41, 'Eloy':32}
print(ages)
print(ages['César'])
ages['Aurelio'] = 21
print(ages)
ages['Rogelio'] = 55
print(ages)
print("\t Borrando elemento Rogelio del diccionario ")
del ages['Rogelio']
print(ages)
print("\tBorrar todo el diccionario")
del ages
#print(ages)
print("\tNuevo diccionario")
ages1 = {'César': 41, 'Eloy':32}
print(ages1)
print(ages1.get('Eloy'))
print(ages1.keys())
#print(list(ages1.kyes()))
print(ages1.values())
