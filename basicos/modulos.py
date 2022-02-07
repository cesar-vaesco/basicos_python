# Un módulo es un objeto de Python con atributos con nombres arbitrarios que puede enlazar y
# hacer referencia. Simplemente, un módulo es no es otra cosa sino un archivo con extensión . py.
# Un módulo puede definir funciones, clases y variables, también puede incluir código ejecutablei


from datetime import date, timedelta
from fmath import suma, resta
from colorama import Back,Fore, Style

print(date.today())
print(timedelta(minutes=100))

suma(5, 6)
resta(5, 6)
print(Fore.RED + 'some red text')
print(Back.LIGHTBLUE_EX + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')