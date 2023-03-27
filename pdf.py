from tkinter import messagebox
from modelo import Actual
from fpdf import *
import os
import re


class Pdf(FPDF):
    def crear_txt():

        with open("conversor.txt", "a") as archivo:

            archivo.write("\t\t\t\t\t\t\t\tComedere club ")
            archivo.write("\nMenu semanal")

            for x in Actual.select():
                archivo.write(
                    "\n\n"
                    + x.dia
                    + ":\n\tReceta: "
                    + x.receta
                    + "\n\tQue Falta?: "
                    + x.que_falta
                )

    def logo(self, name, x, y, w, h):
        self.image(name, x, y, w, h)

    def texts(self, name):
        with open(name, "rb") as xy:
            txt = xy.read().decode("latin-1")
        self.set_font("arial", "", 12)
        self.set_xy(
            10,
            0,
        )
        self.multi_cell(0, 10, txt)

    def titles(self, title):
        self.set_xy(0.0, 0.0)
        self.set_text_color(220, 50, 50)


def crear(nombre):

    patron = "[^a-zA-Z0-9\ ]"
    if re.search(patron, nombre):
        messagebox.showinfo(
            message="El nombre solo puede contener letras, numeros o espacios",
            title="Comedere Club",
        )

    else:
        pregunta = messagebox.askquestion(
            title="Comedere Club",
            message="¿Desea crear el PDF '" + (nombre) + "' de la semana actual?",
        )

        if pregunta == "yes":
            Pdf.crear_txt()
            pdf = Pdf()
            pdf.add_page()
            pdf.texts("conversor.txt")
            pdf.titles("hola")
            pdf.set_author("mi pdf")
            pdf.output((nombre) + ".pdf", "f")
            os.remove("conversor.txt")
            messagebox.showinfo(
                message="¡PDF guardado exitosamente!", title="Comedere Club"
            )
