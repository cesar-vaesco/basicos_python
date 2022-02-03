nombre = "César"
print(nombre)
point = (2.0, 3.0)
print( point[0])
print( point[1] + 10 )
#point[ 0 ] = 3.0
#Las tublas son inmutables
print( point[0] )
point_3d = point + (4.0,)
print("Nueva tupla: " )
print( point_3d)
x, y, z = point_3d
print(x)
print(y)
print(z)
print("Mi nombre es : %s %s"% ("César","Vargas"))
print("\n Rango\n")
range(10)
print(list(range(10)))
range(0, 10000)
print(list(range(0, 100)))
range(1,12,2)
print(list(range(1,12,2)))

