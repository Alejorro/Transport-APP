#Librerías
from tkinter import*

#Funciones

import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

def dateentry_view(window):
    def print_sel(e):
        print(cal.get_date())
    top = tk.Toplevel(window)

    ttk.Label(top, text='Elige Mes/Día/Año').pack(padx=10, pady=10)
    cal = DateEntry(top, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    cal.pack(padx=10, pady=10)
    cal.bind("<<DateEntrySelected>>", print_sel)

def clickedMessage(window, texto="Clicked"):
    lblClicked = Label(window, text=texto, font=("Arial Bold", 10))
    lblClicked.grid(column=0, row=3)