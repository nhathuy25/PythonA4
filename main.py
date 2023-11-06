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
root.geometry('900x500')

#Copyright label
licenses = tb.Label(text="© Designed by Huy NGUYEN and Khoa VU - 4A INSA CVL 2023", font=('Times new roman', 10, 'italic'))
licenses.grid(row = 1)

###     INITIALISATION
#Initialisation of 2D list called sem:
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

#Fonctions:
def getIdSeance(nom:str):
    for s in Classes.col.listeM:
        if nom == s :
            return Classes.col.listeM

def checkType(id:int):
    if id==1:
        return 'CM'
    elif id==2:
        return 'TD'
    else:
        return 'TP'

def jourConverter(s:str):
    index = Classes.jours.index(s)
    return index + 1

def ajouteSeance():
    #global  r, jour1, col, sem
    #Pick up values:
    id_mat = getIdSeance(combo_seance.get())    #mat is a integer define id of the seance
    type = checkType(r.get())                   #type is a string ('CM', 'TD', 'TP')
    num_seance= seance1.get()                   #number of the seance in the day
    jour = jourConverter(jour1.get())           #variable jour is a integer from 1 to 7

    label1.config(text=f'{combo_seance.get()}')
    tk.messagebox.showinfo(message=f"type: {type}, id: {id_mat}, jour: {jour}")
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

#Three radiobutton
tb.Radiobutton(tab1, text="CM  ", bootstyle="secondary", variable=r, value=1, command=lambda: Clicked(r.get())).grid(row=3, column=5)
tb.Radiobutton(tab1, text="TD  ", bootstyle="secondary", variable=r, value=2, command=lambda: Clicked(r.get())).grid(row=3, column=6)
tb.Radiobutton(tab1, text="TP  ", bootstyle="secondary", variable=r, value=3, command=lambda: Clicked(r.get())).grid(row=3, column=7)

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

button1 = tb.Button(tab1, text="Ajouter", bootstyle="primary", command=lambda: ajouteSeance())
button1.grid(row=7, column=3, pady=10)

#### Comment de compare

###
label1 = tb.Label(root, text=f'{combo_seance.get()}')
label1.grid(row=8)

root.mainloop()

print(getIdSeance("Programmation C++"))