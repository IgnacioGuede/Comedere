from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from modelo import (
    FuncionalidadRecetas,
    FuncionalidadSemanas,
    FuncionalidadConfiguracion,
)
from pdf import crear
from modelo import Recetas, Configuracion
import tkinter


class VistaApp:
    def ventana_volver(ventana):
        ventana.destroy()
        VistaApp.ventana_principal()

    def ventana_principal():

        #########################################
        # VENTANA PRINCIPAL
        ##########################################
        ventana = Tk()
        ventana.title("Comedere Club")
        ventana.config(width=230, height=220)
        ventana.resizable(width=FALSE, height=FALSE)
        ventana.iconphoto(False, tkinter.PhotoImage(file="trebol.ico"))

        dec1 = Label(ventana, width=60, bg="olive drab2")
        dec1.place(x=0, y=210)

        ### LABELS
        # TITULO
        lbl_titulo = Label(
            ventana,
            text="🍀 Comedere Club",
            width=19,
            font=("Segoe Print", 14),
            bg="olive drab2",
        )
        lbl_titulo.place(x=0, y=10)

        ### BOTONES
        # BOTON PARA VER LAS RECETAS
        btn_recetas = Button(ventana, text="Recetas", bd=5, font=("Gadugi", 14))
        btn_recetas.place(x=67, y=60)
        btn_recetas.config(command=lambda: VistaApp.ventana_recetas(ventana))

        # BOTON PARA VER MENU SEMANAL
        btn_semana = Button(ventana, text="Menu Semanal", bd=5, font=("Gadugi", 12))
        btn_semana.place(x=48, y=120)
        btn_semana.config(command=lambda: VistaApp.ventana_semanas(ventana))

        # BOTON PARA VER MENU SEMANAL
        btn_configuracion = Button(
            ventana, text="Configuración", bd=2, font=("Gadugi", 8)
        )
        btn_configuracion.place(x=7, y=180)
        btn_configuracion.config(
            command=lambda: VistaApp.ventana_configuracion(ventana)
        )

        ventana.mainloop()

        ####################################
        # VENTANA RECETAS
        ####################################

    def ventana_recetas(ventana_prin):

        ventana_prin.destroy()
        ## VENTANA RECETAS
        ventana = Tk()
        ventana.title("Comedere Club")
        ventana.protocol("WM_DELETE_WINDOW", lambda: VistaApp.ventana_volver(ventana))
        ventana.config(width=490, height=400)
        ventana.resizable(width=FALSE, height=FALSE)
        ventana.iconphoto(False, tkinter.PhotoImage(file="trebol.ico"))

        ### LABELS
        # TITULO
        lbl_titulo = Label(
            ventana,
            text="🍀 Comedere Club / Recetas",
            width=33,
            font=("Segoe Print", 18),
            bg="olive drab2",
        )
        lbl_titulo.place(x=0, y=5)

        # TOTAL DE RECETAS AGREGADAS
        lbl_recetas = Label(ventana, font=("Gadugi", 12), bg="olive drab2")
        lbl_recetas.place(x=15, y=369)

        # MOSTRAR TOTAL DE RECETAS AGREGADAS
        def mostrar_total():
            resultado = 0
            for x in Recetas.select():
                resultado = resultado + 1

            lbl_recetas.config(text="Recetas guardadas: " + str(resultado) + " 🍀")
            lbl_recetas.after(800, mostrar_total)

        mostrar_total()

        # FORMATO ULTIMA VEZ
        lbl_formato = Label(ventana, text="dd/mm/aaaa", font=("Gadugi", 8))
        lbl_formato.place(x=400, y=165)

        # LABEL PARA BORRAR
        lbl_borrar = Label(ventana, text="ID de la receta ▲", font=("Gadugi", 8))
        lbl_borrar.place(x=381, y=245)

        ### ENTRYS
        # ENTRY PARA AGREGAR RECETAS
        entry_agregar = Entry(ventana, width=24, bg="snow3")
        entry_agregar.place(x=15, y=105)

        # ENTRY PARA BUSCAR RECETAS
        entry_buscar = Entry(ventana, width=24, bg="snow3")
        entry_buscar.place(x=330, y=105)

        # ENTRY PARA BORRAR
        entry_borrar = Entry(ventana, width=4, bg="snow3")
        entry_borrar.place(x=450, y=223)

        ### BOTONES
        # BOTON PARA AGREGAR RECETAS
        btn_agregar = Button(ventana, text="Agregar recetas", bd=5, font=("Gadugi", 12))
        btn_agregar.place(x=24, y=60)
        btn_agregar.config(
            command=lambda: FuncionalidadRecetas.agregar_receta(
                str.lower(entry_agregar.get()), entry_agregar
            )
        )

        # BOTON PARA BUSCAR RECETAS
        btn_buscar = Button(ventana, text="Buscar...", bd=5, font=("Gadugi", 12))
        btn_buscar.place(x=370, y=60)
        btn_buscar.config(
            command=lambda: FuncionalidadRecetas.buscar_recetas(
                str.lower(entry_buscar.get()),
                recetas.get(),
                ult_vez.get(),
                entry_borrar,
                treeview,
            )
        )

        # BOTON PARA BORRAR RECETAS
        btn_borrar = Button(ventana, text="Borrar", bd=5, font=("Gadugi", 12))
        btn_borrar.place(x=380, y=205)
        btn_borrar.config(
            command=lambda: FuncionalidadRecetas.borrar_receta(
                str.lower(entry_borrar.get()), entry_borrar, treeview
            )
        )

        # BOTON PARA MOSTRAR RECETAS
        btn_mostrar = Button(ventana, text="Mostrar Recetas", bd=5, font=("Gadugi", 10))
        btn_mostrar.place(x=375, y=290)
        btn_mostrar.config(
            command=lambda: FuncionalidadRecetas.mostrar_recetas(treeview)
        )

        # BOTON PARA VOLVER
        btn_volver = Button(ventana, text="Volver", bd=2, font=("Gadugi", 10))
        btn_volver.place(x=440, y=370)
        btn_volver.config(command=lambda: VistaApp.ventana_volver(ventana))

        ### CHECK BOX
        recetas = IntVar()
        check_recetas = Checkbutton(
            ventana,
            variable=recetas,
            onvalue=1,
            offvalue=0,
            text="Receta",
            command=lambda: checks(check_ult_vez, recetas.get()),
        )
        check_recetas.place(x=380, y=125)

        ult_vez = IntVar()
        check_ult_vez = Checkbutton(
            ventana,
            variable=ult_vez,
            onvalue=1,
            offvalue=0,
            text="Ultima vez",
            command=lambda: checks(check_recetas, ult_vez.get()),
        )
        check_ult_vez.place(x=380, y=145)

        def checks(check, var):
            check.config(state=DISABLED)
            if var == 0:
                check.config(state=NORMAL)

        # TREEVIEW PARA VER RECETAS AGREGADAS
        style = ttk.Style(ventana)
        style.theme_use("clam")
        style.configure("Treeview", foreground="white")

        treeview = ttk.Treeview(ventana)
        treeview["columns"] = ("ID", "Receta", "Ultima vez hecha")
        treeview.column("#0", width=0, stretch=NO)
        treeview.column(
            "ID",
            width=40,
            anchor=CENTER,
        )
        treeview.column(
            "Receta",
            width=233,
            anchor=CENTER,
        )
        treeview.column(
            "Ultima vez hecha",
            width=80,
            anchor=CENTER,
        )

        treeview.heading("#0", text="", anchor=CENTER)
        treeview.heading("ID", text="ID", anchor=CENTER)
        treeview.heading("Receta", text="Receta", anchor=CENTER)
        treeview.heading("Ultima vez hecha", text="Ultima vez hecha", anchor=CENTER)

        treeview.place(x=15, y=130)

        ventana.mainloop()

        ##############################################
        # VENTANA SEMANAS
        ##############################################

    def ventana_semanas(ventana_prin):

        ventana_prin.destroy()
        ## VENTANA SEMANAS
        ventana = Tk()
        ventana.title("Comedere Club")
        ventana.protocol("WM_DELETE_WINDOW", lambda: VistaApp.ventana_volver(ventana))
        ventana.config(width=670, height=320)
        ventana.resizable(width=FALSE, height=FALSE)
        ventana.iconphoto(False, tkinter.PhotoImage(file="trebol.ico"))

        ### LABELS
        # TITULO
        lbl_titulo = Label(
            ventana,
            text="🍀 Comedere Club / Semanas",
            width=45,
            font=("Segoe Print", 18),
            bg="olive drab2",
        )
        lbl_titulo.place(x=0, y=5)

        ### ENTRYS
        # ENTRY NOMBRE DEL PDF
        entry_nombre = Entry(ventana, width=21, bg="snow3")
        entry_nombre.place(x=15, y=260)
        entry_nombre.insert(0, "Menu semanal")

        ### BOTONES

        # BOTON PARA VOLVER
        btn_volver = Button(ventana, text="Volver", bd=2, font=("Gadugi", 10))
        btn_volver.place(x=5, y=290)
        btn_volver.config(command=lambda: VistaApp.ventana_volver(ventana))

        # BOTON PARA MODIFICAR SEMANA
        btn_mod_semana = Button(
            ventana,
            text="Modificar la\nsemana marcada",
            bd=4,
            font=("Gadugi", 10),
            padx=7,
        )
        btn_mod_semana.place(x=15, y=140)
        btn_mod_semana.config(
            command=lambda: VistaApp.ventana_mod_semana(
                ventana, pasado.get(), presente.get(), futuro.get(), treeview
            )
        )
        btn_pdf = Button(
            ventana, text="Importar la semana\nactual a PDF", bd=4, font=("Gadugi", 10)
        )
        btn_pdf.place(x=15, y=200)
        btn_pdf.config(command=lambda: crear(str(entry_nombre.get())))

        ### CHECK BOX
        pasado = IntVar()
        check_pasado = Checkbutton(
            ventana, variable=pasado, onvalue=1, offvalue=0, text="Semana pasada"
        )
        check_pasado.config(
            command=lambda: [
                checks_semanas(check_presente, check_futuro, pasado.get()),
                FuncionalidadSemanas.mostrar_semana(
                    pasado.get(), presente.get(), futuro.get(), treeview
                ),
            ]
        )
        check_pasado.place(x=15, y=70)

        presente = IntVar()
        check_presente = Checkbutton(
            ventana, variable=presente, onvalue=1, offvalue=0, text="Semana actual"
        )
        check_presente.config(
            command=lambda: [
                checks_semanas(check_pasado, check_futuro, presente.get()),
                FuncionalidadSemanas.mostrar_semana(
                    pasado.get(), presente.get(), futuro.get(), treeview
                ),
            ]
        )
        check_presente.place(x=15, y=90)

        futuro = IntVar()
        check_futuro = Checkbutton(
            ventana, variable=futuro, onvalue=1, offvalue=0, text="Semana siguiente"
        )
        check_futuro.config(
            command=lambda: [
                checks_semanas(check_pasado, check_presente, futuro.get()),
                FuncionalidadSemanas.mostrar_semana(
                    pasado.get(), presente.get(), futuro.get(), treeview
                ),
            ]
        )
        check_futuro.place(x=15, y=110)

        def checks_semanas(check1, check2, var):
            check1.config(state=DISABLED)
            check2.config(state=DISABLED)
            if var == 0:
                check1.config(state=NORMAL)
                check2.config(state=NORMAL)

        # TREEVIEW PARA VER LAS SEMANAS
        style = ttk.Style(ventana)
        style.theme_use("clam")
        style.configure("Treeview", foreground="white")

        treeview = ttk.Treeview(ventana)
        treeview["columns"] = ("Dia", "Receta", "Que falta")
        treeview.column("#0", width=0, stretch=NO)
        treeview.column(
            "Dia",
            width=80,
            anchor=CENTER,
        )
        treeview.column(
            "Receta",
            width=223,
            anchor=CENTER,
        )
        treeview.column(
            "Que falta",
            width=180,
            anchor=CENTER,
        )

        treeview.heading("#0", text="", anchor=CENTER)
        treeview.heading("Dia", text="Dia", anchor=CENTER)
        treeview.heading("Receta", text="Receta", anchor=CENTER)
        treeview.heading("Que falta", text="Que falta", anchor=CENTER)

        treeview.place(x=170, y=70)

        ventana.mainloop()

        ##############################################
        # VENTANA MODIFICAR SEMANAS
        ##############################################

    def ventana_mod_semana(ventana_prin, pasado, presente, futuro, treeview):

        if pasado == 0 and presente == 0 and futuro == 0:
            messagebox.showinfo(
                message="Ninguna semana seleccionada", title="Comedere Club"
            )
            VistaApp.ventana_semanas(ventana)

        else:
            ventana_prin.withdraw()
            ## VENTANA MODIFICAR SEMANAS
            ventana = Tk()
            ventana.title("Comedere Club")
            ventana.protocol(
                "WM_DELETE_WINDOW",
                lambda: [ventana_prin.deiconify(), ventana.destroy()],
            )
            ventana.config(width=270, height=250)
            ventana.resizable(width=FALSE, height=FALSE)

            texto = ""
            if pasado == 1:
                texto = " Modificando la semana pasada ..."
            elif presente == 1:
                texto = " Modificando la semana actual ..."
            else:
                texto = " Modificando la semana siguiente ..."
            # LABEL PARA SABER QUE SEMANA ESTOY MODIFICANDO
            lbl_modificar = Label(
                ventana,
                text=(texto),
                anchor=W,
                width=43,
                font=("Gadugi", 12),
                bg="olive drab2",
            )
            lbl_modificar.place(x=0, y=10)

            ### LABELS
            # LABEL DIA
            lbl_dia = Label(
                ventana, text="Dia", width=9, font=("Gadugi", 8), bg="olive drab2"
            )
            lbl_dia.place(x=15, y=100)

            # LABEL RECETA
            lbl_receta = Label(
                ventana, text="Receta", width=9, font=("Gadugi", 8), bg="olive drab2"
            )
            lbl_receta.place(x=15, y=150)

            # LABEL DIA
            lbl_falta = Label(
                ventana,
                text="Que falta?",
                width=9,
                font=("Gadugi", 8),
                bg="olive drab2",
            )
            lbl_falta.place(x=15, y=200)

            ### ENTRYS
            # ENTRY DIA
            entry_dia = Entry(ventana, width=17, bg="snow3", state="readonly")
            entry_dia.place(x=35, y=125)

            # ENTRY RECETA
            entry_receta = Entry(ventana, width=20, bg="snow3")
            entry_receta.place(x=15, y=175)

            # ENTRY QUE FALTA
            entry_falta = Entry(ventana, width=20, bg="snow3")
            entry_falta.place(x=15, y=225)

            # BOTON PARA MODIFICAR ALGUNA RECETA
            btn_modificar = Button(ventana, text="Modificar", bd=5, font=("Gadugi", 12))
            btn_modificar.place(x=15, y=45)
            btn_modificar.config(
                command=lambda: FuncionalidadSemanas.modificar_semana(
                    pasado,
                    presente,
                    futuro,
                    entry_dia.get(),
                    str.lower(entry_receta.get()),
                    entry_falta.get(),
                    treeview,
                )
            )

            # ELEGIR RECETA ALEATORIAMENTE
            btn_random = Button(
                ventana, text="Elegir receta\naleatoriamente", bd=5, font=("Gadugi", 9)
            )
            btn_random.place(x=147, y=155)
            btn_random.config(
                command=lambda: FuncionalidadSemanas.receta_aleatoria(entry_receta)
            )

            # BOTON PARA VOLVER
            btn_dia = Button(ventana, text="Volver", bd=2, font=("", 10))
            btn_dia.place(x=220, y=220)
            btn_dia.config(
                command=lambda: [ventana_prin.deiconify(), ventana.destroy()]
            )

            # POPUP PARA AUTOCOMPLETAR EL DIA
            btn_dia = Button(ventana, text="▼", bd=5, font=("", 5))
            btn_dia.place(x=15, y=125)
            btn_dia.config(command=lambda: popup_mostrar())

            # MOSTRAR MENU POPUP
            def popup_mostrar():
                try:
                    popup_dia.tk_popup(x=200, y=300)
                finally:
                    popup_dia.grab_release()

            # OPCIONES DEL MENU POPUP
            popup_dia = Menu(ventana, tearoff=0)
            popup_dia.add_command(
                label="Lunes",
                command=lambda: [
                    normal(entry_dia),
                    borrar_entry(entry_dia),
                    entry_dia.insert(0, "Lunes"),
                    readonly(entry_dia),
                ],
            )
            popup_dia.add_command(
                label="Martes",
                command=lambda: [
                    normal(entry_dia),
                    borrar_entry(entry_dia),
                    entry_dia.insert(0, "Martes"),
                    readonly(entry_dia),
                ],
            )
            popup_dia.add_command(
                label="Miercoles",
                command=lambda: [
                    normal(entry_dia),
                    borrar_entry(entry_dia),
                    entry_dia.insert(0, "Miercoles"),
                    readonly(entry_dia),
                ],
            )
            popup_dia.add_command(
                label="Jueves",
                command=lambda: [
                    normal(entry_dia),
                    borrar_entry(entry_dia),
                    entry_dia.insert(0, "Jueves"),
                    readonly(entry_dia),
                ],
            )
            popup_dia.add_command(
                label="Viernes",
                command=lambda: [
                    normal(entry_dia),
                    borrar_entry(entry_dia),
                    entry_dia.insert(0, "Viernes"),
                    readonly(entry_dia),
                ],
            )

            def borrar_entry(entry):
                entry.delete(0, "end")

            def readonly(entry):
                entry.config(state="readonly")

            def normal(entry):
                entry.config(state="normal")

            ventana.mainloop()

    ##################
    ## VENTANA CONFIGURACION
    ##################

    def ventana_configuracion(ventana_prin):
        ventana_prin.destroy()

        ventana = Tk()
        ventana.title("Comedere Club")
        ventana.protocol("WM_DELETE_WINDOW", lambda: VistaApp.ventana_volver(ventana))
        ventana.config(width=195, height=150)
        ventana.resizable(width=FALSE, height=FALSE)
        ventana.iconphoto(False, tkinter.PhotoImage(file="trebol.ico"))

        lbl_titulo = Label(
            ventana,
            text="🍀 Configuración",
            width=16,
            font=("Segoe Print", 14),
            bg="olive drab2",
        )
        lbl_titulo.place(x=0, y=10)

        guardar_recetas = IntVar()
        check_recetas = Checkbutton(
            ventana,
            variable=guardar_recetas,
            onvalue=1,
            offvalue=0,
            text="Guardar recetas",
        )
        check_recetas.place(x=5, y=60)

        btn_dia = Button(ventana, text="❓", font=("", 8))
        btn_dia.place(x=150, y=60)
        btn_dia.config(
            command=lambda: messagebox.showinfo(
                title="Comedere Club",
                message="Cuando finalice la semana, las recetas que esten en la semana actual sin guardar, se agregaran automaticamente en el listado de recetas",
            )
        )

        btn_guardar = Button(ventana, text="Guardar y salir", font=("", 10))
        btn_guardar.place(x=45, y=120)
        btn_guardar.config(
            command=lambda: [
                FuncionalidadConfiguracion.configuraciones(guardar_recetas.get()),
                VistaApp.ventana_volver(ventana),
            ]
        )

        for x in Configuracion.select():
            if x.configuracion == 1 and x.id == 2:
                check_recetas.select()

        ventana.mainloop()
