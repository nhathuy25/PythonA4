import tkinter.messagebox
import Classes
from tkinter import *
import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename= "cosmo")
#App interface:
root.title("Gestion d'emploi du temps")
root.iconbitmap("./logo.png")
root.geometry('800x500')

#Copyright label
licenses = tb.Label(text="Designed by Huy NGUYEN and Khoa VU - INSA CVL 2023", font=('Arial', 7, 'italic'))
licenses.grid(row = 1)

#Create Tabs:
my_notebook=tb.Notebook(root, bootstyle="primary")
my_notebook.grid(row=2, padx=50, pady=30)

tab1=tb.Frame(my_notebook)
tab2=tb.Frame(my_notebook)

my_notebook.add(tab1, text="Ajouter une séance")
my_notebook.add(tab2, text="Supprimer une séance")

### AJOUTER SEANCES

#Fonctions:
def AjouteSeance():
    global col, combo_seance, r, date1, jour1

    pass

#Add seance
lable_seance=tb.Label(tab1, text="Selecter la seance:", font=('Arial', 11, 'italic'))
lable_seance.grid(row=3, pady=10)

combo_seance= tb.Combobox(tab1, bootstyle='secondary', values=Classes.col.listeM)
combo_seance.grid(row=3,column=1)

#Radio buttons
lable_radio=tb.Label(tab1, text="Type: ", font=('Arial',11, 'italic'))
lable_radio.grid(row=3,column=4, padx=30)

r = IntVar() #A continously changing variable keep track the value of the radiobuttons

def Clicked(value):
    tk.messagebox.showinfo(title="Radiobutton", message=f'{value} clicked')

tb.Radiobutton(tab1, text="CM  ", bootstyle="secondary", variable=r, value=1, command=lambda: Clicked(r.get())).grid(row=3, column=5)
tb.Radiobutton(tab1, text="TD  ", bootstyle="secondary", variable=r, value=2, command=lambda: Clicked(r.get())).grid(row=3, column=6)
tb.Radiobutton(tab1, text="TP  ", bootstyle="secondary", variable=r, value=3, command=lambda: Clicked(r.get())).grid(row=3, column=7)

lable_semaine=tb.Label(tab1, text="Saisir la semaine: ", font=('Arial', 11, 'italic'))
lable_semaine.grid(row=4, pady=10)

semaine1 = tb.Entry(tab1, bootstyle="secondary")
semaine1.grid(row=4, column=1)

lable_jour=tb.Label(tab1, text=" et le jour: ", font=('Arial', 11, 'italic'))
lable_jour.grid(row=4, column=4)

jour1=tb.Combobox(tab1, bootstyle='secondary', values=Classes.jour)
jour1.grid(row=4, column=6)

button1 = tb.Button(tab1, text="Ajouter", bootstyle="primary")
button1.grid(row=5, column=3, pady=10)

###



root.mainloop()