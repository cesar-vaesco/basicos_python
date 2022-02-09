import sys

file_name = 'recipes.txt'

try:
    mi_archivo = open('recipes.txt', 'x')
    mi_archivo.write('Meatballs\n')
    mi_archivo.close()
except FileExistsError as err:
    print ('folder {0} already exists'.format(file_name))
    print(err)
    sys.exit(1)
except:
    print('no se puede escribir en el archivo {0}'.format(file_name))
    sys.exit(1)
else:
    print("Escribir en {0}".format(file_name))
finally:
    print("Ejecucion completa")
