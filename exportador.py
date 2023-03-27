from peewee import *
from datetime import datetime
from modelo import Pasada, Actual, Siguiente, Configuracion, Recetas
import re

dia_hoy = 0
backup = 0
recetas = 0

lista_recetas = []

for x in Configuracion.select().where(Configuracion.id == 2):
    recetas = x.configuracion

dia_hoy = datetime.today().isoweekday()
for x in Configuracion.select().where(Configuracion.id == 1):
    backup = x.configuracion

dia_hoy = 0
backup = 0

if dia_hoy >= 6 and backup == 0:

    for x in Actual.select():

        modificar = Pasada.update(receta=x.receta, que_falta=x.que_falta).where(
            Pasada.dia == x.dia
        )
        modificar.execute()

    for x in Siguiente.select():

        modificar = Actual.update(receta=x.receta, que_falta=x.que_falta).where(
            Actual.dia == x.dia
        )
        modificar.execute()

        modificar = Siguiente.update(receta="-", que_falta="-").where(
            Siguiente.dia == x.dia
        )
        modificar.execute()

    modificar = Configuracion.update(configuracion=1).where(Configuracion.id == 1)
    modificar.execute()

    for x in Pasada.select():
        lista_recetas.append(x.receta)

    contador = 0
    for x in Recetas.select():
        contador = 0
        while contador < 5:

            if re.fullmatch(x.receta, (lista_recetas[contador])):
                modificar = Recetas.update(ult_vez=(datetime.now())).where(
                    Recetas.receta == x.receta
                )
                modificar.execute()

            else:
                try:
                    guardar = Recetas(
                        receta=(lista_recetas[contador]), ult_vez=(datetime.now())
                    )
                    guardar.save()
                except:
                    pass

            contador = contador + 1

elif dia_hoy < 6 and backup == 1:
    modificar = Configuracion.update(configuracion=0).where(Configuracion.id == 1)
    modificar.execute()
