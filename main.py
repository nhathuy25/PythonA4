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

###     INITIALISATION OF VARIABLES:
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

##Fonctions:

#getIdSeance takes a string which is the name of seance and convert it to index of it in listM
def getIdSeance(nom:str):
    arr = []
    for s in matieres.listeM:
        arr.append(s)
    for temp in arr:
        if nom==str(temp):
            return arr.index(temp)
        else:
            return 99

def printSeances():
    arr=[]
    for s in matieres.listeM:
        arr.append(s)
    for temp in arr:
        print(temp)

def checkType(id:int):
    if id==1:
        return 'CM'
    elif id==2:
        return 'TD'
    else:
        return 'TP'

def convertJour(s:str):
    index = Classes.jours.index(s)
    return index + 1

def ajouteSeance():
###Pick up values:
    #Check if any field is missing:
    if combo_seance.get() != '' and r.get() != 0 and seance1.get() != 0 and jour1.get() != '':
        id_matiere = getIdSeance(combo_seance.get())        #an integer define id of the seance
        type_seance = checkType(r.get())                    #string ('CM', 'TD', 'TP')
        num_seance= int(seance1.get())-1                    #number of the seance in the day
        num_jour = convertJour(jour1.get())                 #an integer from 1 to 7 indicate from Monday to Sunday
        num_semaine = int(semaine1.get())                              #number of week
    #if one or more fields are missing, send error
    else:
        tk.messagebox.showerror(message="Please fill in all the info!", title="Error")

    sem.numS[num_semaine][num_seance*num_jour]= Classes.Seance(id=id_matiere, hCM=10)
    label1.config(text=f'{sem.numS[num_semaine][num_seance*num_jour]} ajoute! and nom {combo_seance.get()}')

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

### Testing
label1=tb.Label(bootstyle='secondary')
label1.grid(row=8)

root.mainloop()

print(getIdSeance("MAEL"))
printSeances()
#print(combo_seance)
#sem.numS[1][0] = Classes.Seance(id=1, hCM=2)
print(sem.numS[1][0])