# own modules
# thirdy party modules // modulos de terceros
# python modules // de la propia biblioteca de python.

import datetime # un forma de importar una libreria

from datetime import timedelta # otra manera de importar una libreria
print(timedelta(minutes=70))


print(datetime.date.today())
print(datetime.timedelta(minutes=70))


from datetime import timedelta, date
print(timedelta(minutes=70))
print(date.today())

# importamos un modulo creado
import fmath

fmath.add(1, 2)
fmath.substract(1,2)


from fmath import add, substract

substract(1, 2)
add(1, 2)
