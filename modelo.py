from tkinter import *
from peewee import *
from tkinter import messagebox
import random
import re

# CREAR UNA BASE DE DATOS SI NO EXISTE
db = SqliteDatabase("Base.db")


class BaseModel(Model):
    class Meta:
        database = db


# TABLA DE RECETAS
class Recetas(BaseModel):
    receta = TextField(unique=True)
    ult_vez = TextField()


# TABLA SEMANA ANTERIOR
class Pasada(BaseModel):
    dia = TextField(unique=True)
    receta = TextField()
    que_falta = TextField()


# TABLA SEMANA ACTUAL
class Actual(BaseModel):
    dia = TextField(unique=True)
    receta = TextField()
    que_falta = TextField()


# TABLA SEMANA SIGUIENTE
class Siguiente(BaseModel):
    dia = TextField(unique=True)
    receta = TextField()
    que_falta = TextField()


class Configuracion(BaseModel):
    configuracion = IntegerField()
    descripcion = TextField(unique=True)


db.connect()
db.create_tables([Recetas, Pasada, Actual, Siguiente, Configuracion])

# GUARDAR 5 REGISTROS PARA CADA TABLA
lista_dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
try:
    for x in lista_dias:
        crear_pasada = Pasada(dia=(x), receta="-", que_falta=("-"))
        crear_pasada.save()

        crear_presente = Actual(dia=(x), receta="-", que_falta=("-"))
        crear_presente.save()

        crear_futuro = Siguiente(dia=(x), receta="-", que_falta=("-"))
        crear_futuro.save()
except:
    pass
try:
    backup_hecho = Configuracion(configuracion=0, descripcion="pasaje de recetas")
    backup_hecho.save()

    crear_configuracion = Configuracion(configuracion=0, descripcion="Guardar recetas")
    crear_configuracion.save()
except:
    pass

# BORRAR EL TREEVIEW
def borrar_treeview(tv):
    registro = tv.get_children()
    for x in registro:
        tv.delete(x)


class FuncionalidadRecetas:

    ### AGREGAR UNA NUEVA RECETA
    def agregar_receta(receta, entry):

        valor = 1

        if len(receta) == 0:
            messagebox.showinfo(message="Campo de recetas vacio", title="Comedere Club")
            valor = 0

        else:
            for x in Recetas.select():
                if re.fullmatch(x.receta, receta):
                    messagebox.showinfo(
                        message="La receta '" + (receta) + "' ya existe",
                        title="Comedere Club",
                    )
                    valor = 0

            if valor == 1:
                guardar = Recetas(receta=(receta), ult_vez="--/--/----")
                guardar.save()

                messagebox.showinfo(
                    message="¡Receta guardada exitosamente!", title="Comedere Club"
                )

        entry.delete(0, "end")

    ### BORRAR RECETAS
    def borrar_receta(borra, entry, treeview):

        borrar_treeview(treeview)

        if len(borra) == 0:
            messagebox.showinfo(message="Campo de borrado vacio", title="Comedere Club")

        else:
            pregunta = messagebox.askquestion(
                title="Comedere Club",
                message="¿Desea borrar la receta ¨" + (borra) + "¨?",
            )

            if pregunta == "yes":

                valor = 0
                total_recetas = 0
                receta_borrada = 0

                for x in Recetas.select():

                    total_recetas = total_recetas + 1

                    if re.fullmatch(str(x.id), borra):

                        receta_borrada = int(x.id)
                        valor = 1
                        borrar = Recetas.get(Recetas.id == borra)
                        borrar.delete_instance()

                if valor == 0:
                    messagebox.showinfo(
                        message="La receta ¨" + borra + "¨ no fue encontrada",
                        title="Comedere Club",
                    )

                elif valor == 1:
                    messagebox.showinfo(
                        message="¡La receta ¨" + borra + "¨ fue borrada exitosamente!",
                        title="Comedere Club",
                    )
                    FuncionalidadRecetas.acomodar_id(total_recetas, receta_borrada)

        FuncionalidadRecetas.mostrar_recetas(treeview)
        entry.delete(0, "end")

    # ACOMODAR ID DE LAS RECETAS
    def acomodar_id(total, borrada):

        actualizar = borrada - 1

        while borrada <= total:
            acomodar = Recetas.update(id=actualizar).where(Recetas.id == borrada)
            acomodar.execute()
            borrada = borrada + 1
            actualizar = actualizar + 1

    ### MOSTRAR TODAS LAS RECETAS
    def mostrar_recetas(tv):

        borrar_treeview(tv)

        valor = 0

        for x in Recetas.select():

            valor = 1
            tv.insert("", END, text=[0], values=(x.id, x.receta, x.ult_vez))

        if valor == 0:
            messagebox.showinfo(
                message="No se encontraron registros de recetas", title="Comedere Club"
            )

    ### BUSCAR RECETAS
    def buscar_recetas(buscar, receta, ult_vez, entry, tv):

        borrar_treeview(tv)

        if len(buscar) == 0:
            messagebox.showinfo(
                message="Campo del buscador vacio", title="Comedere Club"
            )

        elif receta == 0 and ult_vez == 0:
            messagebox.showinfo(
                message="Ninguna opcion seleccionada", title="Comedere Club"
            )

        else:
            tv.insert("", END, text=[0], values=("", "RESULTADOS ▼", (buscar)))
            if receta == 1:

                for x in Recetas.select():
                    if re.search(buscar, x.receta):
                        tv.insert("", END, text=[0], values=("", x.receta, x.ult_vez))

            elif ult_vez == 1:

                for x in Recetas.select():
                    if re.search(buscar, x.ult_vez):
                        tv.insert("", END, text=[0], values=("", x.receta, x.ult_vez))

        entry.delete(0, "end")


#####################################
## FUNCIONALIDAD SEMANAS           ##
#####################################


class FuncionalidadSemanas:
    def mostrar_semana(pasado, presente, futuro, tv):

        borrar_treeview(tv)

        if pasado == 1:
            tv.insert("", END, text=[0], values=("▶ PASADA", "▼", "▼"))
            for x in Pasada.select():
                tv.insert("", END, text=[0], values=(x.dia, x.receta, x.que_falta))

        elif presente == 1:
            tv.insert("", END, text=[0], values=("▶ ACTUAL", "▼", "▼"))
            for x in Actual.select():
                tv.insert("", END, text=[0], values=(x.dia, x.receta, x.que_falta))

        elif futuro == 1:
            tv.insert("", END, text=[0], values=("▶ SIGUIENTE", "▼", "▼"))
            for x in Siguiente.select():
                tv.insert("", END, text=[0], values=(x.dia, x.receta, x.que_falta))

    def modificar_semana(pasado, presente, futuro, dia, receta, que_falta, treeview):

        if len(dia) == 0 or len(receta) == 0:
            messagebox.showinfo(
                message="Debe llenar al menos los primeros 2 campos para modificar",
                title="Comedere Club",
            )

        else:
            semana = Recetas
            if pasado == 1:
                semana = Pasada
            elif presente == 1:
                semana = Actual
            elif futuro == 1:
                semana = Siguiente

            modificar = semana.update(receta=receta, que_falta=que_falta).where(
                semana.dia == dia
            )
            modificar.execute()

            FuncionalidadSemanas.mostrar_semana(pasado, presente, futuro, treeview)
            messagebox.showinfo(message="¡Modificacion exitosa!", title="Comedere Club")

    def receta_aleatoria(entry):
        suma = 0
        for x in Recetas.select():
            suma = suma + 1

        if suma == 0:
            messagebox.showinfo(
                message="No se encontraron recetas guardadas", title="Comedere Club"
            )

        else:
            num_random = random.randint(1, (suma))

            entry.delete(0, "end")

            for x in Recetas.select().where(Recetas.id == num_random):
                entry.insert(0, (x.receta))


class FuncionalidadConfiguracion:
    def configuraciones(recetas):
        if recetas == 1:

            modificar = Configuracion.update(configuracion=1).where(
                Configuracion.id == 2
            )
            modificar.execute()

        else:
            modificar = Configuracion.update(configuracion=0).where(
                Configuracion.id == 2
            )
            modificar.execute()
