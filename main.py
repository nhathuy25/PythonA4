import tkinter.messagebox
import Classes
from tkinter import *
import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename="cosmo")
# App interface:
root.title("Gestion d'emploi du temps")
root.iconbitmap("./logo.png")
root.geometry('1000x500')

# Copyright label
licenses = tb.Label(text="© Designed by Huy NGUYEN and Khoa VU - 4A INSA CVL 2023",
                    font=('Times new roman', 10, 'italic'))
licenses.grid(row=1)

###     INITIALISATION OF VARIABLES:
# Initialisation of 2D list called sem:
# sem = Classes.Semaine()

# Import list of subjects:
matieres = Classes.ListeDeMatiere()
matieres.readFromCsv("./ListeDeMatiere.csv")
matieres.updateActualList('./ListeSeances.csv')

# Create Tabs:
my_notebook = tb.Notebook(root, bootstyle="primary")
my_notebook.grid(row=2, padx=50, pady=30)

tab1 = tb.Frame(my_notebook)
tab2 = tb.Frame(my_notebook)
tab3 = tb.Frame(my_notebook)

my_notebook.add(tab1, text="Ajouter une séance")
my_notebook.add(tab2, text="Supprimer une séance")
my_notebook.add(tab3, text="Déplacer une séance")


### AJOUTER SEANCES

##Fonctions:

# getIdSeance takes a string which is the name of seance and convert it to index of it in listM
def getIdSeance(nom: str):
    arr = []
    founded = False
    for s in matieres.listeM:
        arr.append(s)
    for temp in arr:
        if nom == str(temp):
            founded = True
            return arr.index(temp)
    if founded == False:
        return 99


# Function printSeances allows us to print out all the existing matiere
def printSeances():
    arr = []
    for s in matieres.listeM:
        arr.append(s)
    for temp in arr:
        print(temp)


# Function checkType: since the input value of type (CM, TD, TP) is originally an integer, we need to convert it to a variable type string
def checkType(id: int):
    if id == 1:
        return 'CM'
    elif id == 2:
        return 'TD'
    else:
        return 'TP'


# Function convertJour allows us to convert string ('Lundi', 'Mardi',..) to an integer variable marked 1,2,3,4,5,6,7
def convertJour(s: str):
    index = Classes.jours.index(s)
    return index + 1


# Function ajouteSeance (IMPORTANT) is served to take all the data from API and stocked into a .csv file the new class information
def ajouteSeance():
    ### Pick up values:
    # Check if any field is missing:
    if combo_seance.get() != '' and r.get() != 0 and seance1.get() != '' and jour1.get() != '':
        id_matiere = getIdSeance(combo_seance.get())  # an integer define id of the seance
        type_seance = checkType(r.get())  # string ('CM', 'TD', 'TP')
        num_seance = int(seance1.get())  # number of the seance in the day
        num_jour = convertJour(jour1.get())  # an integer from 1 to 7 indicate from Monday to Sunday
        num_semaine = int(semaine1.get())  # number of week

    # if one or more fields are missing, send error
    else:
        tk.messagebox.showerror(message="Please fill in all the info!", title="Error")

    # If-else condition to save the class' number
    if (type_seance=='TD' or type_seance=='TP') and id_type.get()!='':
        num_classe = int(id_type.get())  # number of the class: TD (from 1 to 3) or TP (from 1 to 6)
    elif type_seance=='CM':
        num_classe=0    # Need to check again if it causes any error?
    else:
        tk.messagebox.showerror(message=f'Please fill in the {type_seance} class number', title="Error")

    #addSeance = True
    # Create a new class from input data to be verified:
    nouveau_seance = Classes.Seance(id=id_matiere, type=type_seance, numSemaine=num_semaine, numJour=num_jour,
                                    numSeance=num_seance, numClasse=num_classe)
    # - Add new verify condition here
    addSeance = nouveau_seance.verifySeance('./ListeSeances.csv')
    #
    if addSeance:
        # Write the input class to a new file csv called: 'ListeSeances.csv'
        nouveau_seance.writeToCsv('./ListeSeances.csv')
            # Then, update the actual hour of the subject left by referencing the id of the subject:
            # PROBLEM: HAVEN'T REDUCE THE HOURS BASE ON ID OF CLASS TD/TP
        for mat in matieres.listeM:
            # Verify first if there is available class left to add

            if nouveau_seance.id == mat.id:
                if nouveau_seance.type == 'CM' and mat.heureCM > 0:
                    mat.heureCM -= 1
                elif nouveau_seance.type == 'TD' and mat.heureTD > 0:
                    mat.heureTD -= 1
                elif nouveau_seance.type == 'TP' and mat.heureTP > 0:
                    mat.heureTP -= 1
                else:   # If cannot add in a new class since there is no available class left, send error message
                    tk.messagebox.showerror(message=f'There is no class {nouveau_seance.type} of {mat.nom} left!')

        # Test function: to print out the current statistics of the subject
        num = int(nouveau_seance.id)
        label1.config(
            text=f'{nouveau_seance.type} of {matieres.listeM[nouveau_seance.id]} added! Class left: CM[{matieres.listeM[num].heureCM}] TD[{matieres.listeM[num].heureTD}] TP[{matieres.listeM[num].heureTP}]',
            font=('Arial', 13))


# Add seance
label_seance = tb.Label(tab1, text="Selecter la seance:", font=('Arial', 11, 'italic'))
label_seance.grid(row=3, pady=10)

combo_seance = tb.Combobox(tab1, bootstyle='secondary', values=Classes.col.listeM)
combo_seance.grid(row=3, column=1)

# Radio buttons: Choosing class type (CM, TD, TP)
label_radio = tb.Label(tab1, text="Type: ", font=('Arial', 11, 'italic'))
label_radio.grid(row=3, column=4, padx=30)

r = IntVar()  # A continously changing variable keep track the value of the radiobuttons


def Clicked(value):
    # tk.messagebox.showinfo(title="Radiobutton", message=f'{value} clicked')
    pass


tb.Radiobutton(tab1, text="CM  ", bootstyle="secondary", variable=r, value=1, command=lambda: Clicked(r.get())).grid(
    row=3, column=5)
tb.Radiobutton(tab1, text="TD  ", bootstyle="secondary", variable=r, value=2, command=lambda: Clicked(r.get())).grid(
    row=3, column=6)
tb.Radiobutton(tab1, text="TP  ", bootstyle="secondary", variable=r, value=3, command=lambda: Clicked(r.get())).grid(
    row=3, column=7)

# Label and entry of the number week
label_semaine = tb.Label(tab1, text="Saisir la semaine: ", font=('Arial', 11, 'italic'))
label_semaine.grid(row=4, pady=10)

semaine1 = tb.Entry(tab1, bootstyle="secondary")
semaine1.grid(row=4, column=1, ipadx=8.5)

# Label and number of the class base on it's type (TD/TP)
label_idtype = tb.Label(tab1, text="Numéro de TP/TD", font=('Arial', 11, 'italic'))
label_idtype.grid(row=4, column=4)

id_type = tb.Entry(tab1, bootstyle="secondary")
id_type.grid(row=4, column=6)

# Label and entry combobox for choosing the day in the week:
label_jour = tb.Label(tab1, text=" Jour de semaine: ", font=('Arial', 11, 'italic'))
label_jour.grid(row=5)

jour1 = tb.Combobox(tab1, bootstyle='secondary', values=Classes.jours)
jour1.grid(row=5, column=1)

# Label and entry for number of the class (from 1 to 4)
label_numSeance = tb.Label(tab1, text="Numero de la seance: ", font=('Arial', 11, 'italic'))
label_numSeance.grid(row=6, pady=10)

seance1 = tb.Combobox(tab1, bootstyle="secondary", values=[1, 2, 3, 4])
seance1.grid(row=6, column=1)

# Button to submit the form
button1 = tb.Button(tab1, text="Ajouter", bootstyle="primary", command=lambda: ajouteSeance())
button1.grid(row=7, column=3, pady=10)

### Testing
label1 = tb.Label(bootstyle='success')
label1.grid(row=8)

root.mainloop()

print(getIdSeance("MAEL"))
printSeances()
# print(combo_seance)
# sem.numS[1][0] = Classes.Seance(id=1, hCM=2)
