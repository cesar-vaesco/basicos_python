
with open ('xmen.txt', 'w+') as mi_archivo:
    mi_archivo.write('Beast\n')
    mi_archivo.write('Phoenix\n')
    mi_archivo.writelines(['Cyclops\n', 'Bishop\n', 'Nightcrawler\n'])



mi_archivo = open('xmen.txt', 'r')

with mi_archivo:
    print(mi_archivo.read())
    print("Estoy leyendo de nuevo")
    print(mi_archivo.read())
