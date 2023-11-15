import tkinter.messagebox
from tkinter import *
import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import Utilities

root = tb.Window(themename= "cosmo")
#App interface:
root.title("Gestion d'emploi du temps")
root.iconbitmap("./logo.png")
root.geometry('900x500')

#Copyright label
licenses = tb.Label(text="© Designed by Huy NGUYEN and Khoa VU - 4A INSA CVL 2023", font=('Times new roman', 10, 'italic'))
licenses.grid(row = 1)

###     INITIALISATION OF VARIABLES:
#Initialisation of 2D list called sem:
import Classes
sem = Classes.Semaine()

#Import list of subjects:
matieres = Classes.ListeDeMatiere()
matieres.readFromCsv("./ListeDeMatiere.csv")


#Create Tabs:
my_notebook=tb.Notebook(root, bootstyle="primary")
my_notebook.grid(row=2, padx=50, pady=30)

tab1=tb.Frame(my_notebook)
tab2=tb.Frame(my_notebook)
tab3=tb.Frame(my_notebook)

my_notebook.add(tab1, text="Ajouter une séance")
my_notebook.add(tab2, text="Supprimer une séance")
my_notebook.add(tab3, text="Déplacer une séance")

### AJOUTER SEANCES

import Utilities

##Fonctions:
Utilities.ajouteSeance()

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
    #tk.messagebox.showinfo(title="Radiobutton", message=f'{value} clicked')
    pass

radio_button1=tb.Radiobutton(tab1, text="CM  ", bootstyle="secondary", variable=r, value=1, command=lambda: Clicked(r.get()))
radio_button2=tb.Radiobutton(tab1, text="TD  ", bootstyle="secondary", variable=r, value=2, command=lambda: Clicked(r.get()))
radio_button3=tb.Radiobutton(tab1, text="TP  ", bootstyle="secondary", variable=r, value=3, command=lambda: Clicked(r.get()))

radio_button1.grid(row=3, column=5)
radio_button2.grid(row=3, column=6)
radio_button3.grid(row=3, column=7)

lable_semaine=tb.Label(tab1, text="Saisir la semaine: ", font=('Arial', 11, 'italic'))
lable_semaine.grid(row=4, pady=10)

semaine1 = tb.Entry(tab1, bootstyle="secondary")
semaine1.grid(row=4, column=1)

lable_jour=tb.Label(tab1, text=" le jour: ", font=('Arial', 11, 'italic'))
lable_jour.grid(row=5)

jour1=tb.Combobox(tab1, bootstyle='secondary', values=Classes.jours)
jour1.grid(row=5, column=1)

lable_numSeance=tb.Label(tab1, text="et le numero de la seance: ", font=('Arial', 11, 'italic'))
lable_numSeance.grid(row=6, pady=10)

seance1=tb.Combobox(tab1, bootstyle="secondary", values=[1,2,3,4])
seance1.grid(row=6, column=1)

button1 = tb.Button(tab1, text="Ajouter", bootstyle="primary", command=lambda: Utilities.ajouteSeance())
button1.grid(row=7, column=3, pady=10)

### Testing
label1=tb.Label(bootstyle='secondary')
label1.grid(row=8)

root.mainloop()

print(Utilities.getIdSeance("MAEL"))
Utilities.printSeances()
#print(combo_seance)
#sem.numS[1][0] = Classes.Seance(id=1, hCM=2)
print(sem.numS[1][0])