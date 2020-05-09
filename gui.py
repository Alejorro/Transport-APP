#Librerías
from tkinter import *
from tkinter.ttk import *

#Módulos
from Src.guiResources import *

#VentanaPrincipal
window = Tk()
window.geometry('350x200')
window.title("Bienvenid@")

#Barra de menú principal
menuMain = Menu(window)
optionNew = Menu(menuMain)
optionNew.add_command(label='Nuevo')
menuMain.add_cascade(label='Archivos', menu=optionNew)
menuAyuda = Menu(menuMain)
window.config(menu=menuMain)

#Pestaña Principal
lbl = Label(window, text="Introduce la fecha", font=("Arial Bold", 10))
lbl.grid(column=0, row=0)

#Introducción de fecha
botonFecha = Button(window, text='Introducir fecha', command=lambda:dateentry_view(window))
botonFecha.grid(column=1, row=2)

#Botón de aceptar
lbl = Label(window, text="Introduce la fecha", font=("Arial Bold", 10))
lbl.grid(column=0, row=0)

btn = Button(window, text="Aceptar", command=lambda:clickedMessage(window, texto="Fecha introducida"))
btn.grid(column=1, row=4)

#Pestaña Secundaria
lblFecha2 = Label(window, text="La fecha introducida es:", font=("Arial Bold", 10))
lblFecha2.grid(column=0, row=3)

#Estilo de ventanas
estilo = Style(window)
estilo.theme_use('clam')


#Cierre de ventana
window.mainloop()
