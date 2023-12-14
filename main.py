'''
Description of main.py file:
Contain the window of the application, with User Interface, define the input fields and their associate functions.
The principal function of main.py is to do tasks such as adding, deleting or changing a class. Each task associate with
one function, there are ajouteSeance, supprimeSeance and deplaceSeance.

It exists also other side-functions to help convert the input data to a suitable data type.
'''

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
copyright_label = tb.Label(text="© Designed by Huy NGUYEN and Khoa VU - 4A INSA CVL 2023",
                    font=('Times new roman', 10, 'italic'))
copyright_label.grid(row=1)

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


### FONCTIONS

# getIdSeance takes a string which is the name of the class (seance) and convert it to index of it in listM
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

# Function searchSeance(): find the class base on date and time, return all the class' information
def searchSeance(numSemaine, numJour, numSeance):
    file = open('./listeSeances.csv', 'r')
    line = file.readline()
    lineNumber=1
    while line != '':
        if line !='' and line[0] != '#':
            fields = line.split(';')
            if numSemaine==int(fields[2]) and numJour==int(fields[3]) and numSeance==int(fields[4]):
                return Classes.Seance(id=int(fields[0]), type=fields[1], numSemaine=int(fields[2]), numJour=int(fields[3]), numSeance=int(fields[4]), numClasse=int(fields[5]))
        line = file.readline()
        lineNumber += 1
    file.close()

    # if cannot find the class correspondant, return 0 value
    return 0

# Function ajouteSeance (IMPORTANT) is served to take all the data from API and stocked into a .csv file the new class information
def ajouteSeance():
    ### Pick up values:
    # Check if any input field is missing:
    if combo_seance.get() != '' and r.get() != 0 and seance1.get() != '' and jour1.get() != '':
        id_matiere = getIdSeance(combo_seance.get())  # an integer define id of the seance
        type_seance = checkType(r.get())  # string ('CM', 'TD', 'TP')
        num_seance = int(seance1.get())  # number of the seance in the day
        num_jour = convertJour(jour1.get())  # an integer from 1 to 7 indicate from Monday to Sunday
        num_semaine = int(semaine1.get())  # number of week

    # if one or more than one field is missing, send an error message
    else:
        tk.messagebox.showerror(message="Please fill in all the info!", title="Error")

    # If-else condition to save the class' number
    if (type_seance == 'TD' or type_seance == 'TP') and id_type.get() != '':
        num_classe = int(id_type.get())  # number of the class: TD (from 1 to 3) or TP (from 1 to 6)
    elif type_seance == 'CM':
        num_classe = 0
    else:
        tk.messagebox.showerror(message=f'Please fill in the {type_seance} class number', title="Error")

    # addSeance = True
    # Create a new class from input data to be verified:
    nouveau_seance = Classes.Seance(id=id_matiere, type=type_seance, numSemaine=num_semaine, numJour=num_jour,
                                    numSeance=num_seance, numClasse=num_classe)
    # Verify the condition of nouveau_seance before adding it to the timetable
    addSeance = nouveau_seance.verifySeance()

    if addSeance: # If the conditions are satisfied
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
                else:  # If cannot add in a new class since there is no available class left, send error message
                    tk.messagebox.showerror(message=f'There is no class {nouveau_seance.type} of {mat.nom} left!')

        # Result label: to print out the current statistics of the subject by update the label1
        num = int(nouveau_seance.id)
        label1.config(
            text=f'{nouveau_seance.type} of {matieres.listeM[nouveau_seance.id]} added! Class left: CM[{matieres.listeM[num].heureCM}] TD[{matieres.listeM[num].heureTD}] TP[{matieres.listeM[num].heureTP}]',
            font=('Arial', 13))


def supprimeSeance():
    # Verify that all the input fields are filled
    if semaine2.get() != '' and seance2.get() != '' and jour2.get() != '':
        num_seance = int(seance2.get())  # number of the seance in the day
        num_jour = convertJour(jour2.get())  # an integer from 1 to 7 indicate from Monday to Sunday
        num_semaine = int(semaine2.get())  # number of week
    # if one or more fields are missing, send error
    else:
        tk.messagebox.showerror(message="Please fill in all the info!", title="Error")

    # For the selected class, we only care about the date and number of class of it
    seance_supprime = Classes.Seance(id=99, type='', numSemaine=num_semaine, numJour=num_jour, numSeance=num_seance, numClasse=0)
    # Delete class, assign the seance returned into delSeance to verify
    delSeance = seance_supprime.deleteSeance()

    # If we cannot find the class, the function will return value of 0. Else, it will return a variable type Seance
    if delSeance!=0:
        num = int(seance_supprime.id)
        label1.config(text=f'A class in S{num_semaine}, {jour2.get()}, No class: {num_seance} deleted!', font=('Arial', 13))
        # After remove the class selected, update the current hour left of the subject
        for mat in matieres.listeM:
            if mat.id == int(delSeance[0]):
                if delSeance[1] == 'CM':
                    mat.heureCM += 1
                elif delSeance[1] == 'TD':
                    mat.heureTD += 1
                elif delSeance[1] == 'TP':
                    mat.heureTP += 1

    # If we can't find a class with the date and time inputs, refresh the label1
    else:
        label1.config(text='')

def deplaceSeance():
    # Take the infomations typed in UI
    if semaine3.get() != '' and seance3.get() != '' and jour3.get() != '' and semaine4.get() != '' and seance4.get() != '' and jour4.get() != '':
        # date and time (1)
        num_seance1 = int(seance3.get())  # number of the seance in the day
        num_jour1 = convertJour(jour3.get())  # an integer from 1 to 7 indicate from Monday to Sunday
        num_semaine1 = int(semaine3.get())  # number of week

        # date and time (2)
        num_seance2 = int(seance4.get())  # number of the seance in the day
        num_jour2 = convertJour(jour4.get())  # an integer from 1 to 7 indicate from Monday to Sunday
        num_semaine2 = int(semaine4.get())  # number of week

    # if one or more than one field is missing, send an error message:
    else:
        tk.messagebox.showerror(message="Please fill in all the info!", title="Error")

    # Assign a temporary class (seance) using the date and time (1) of the class to be moved
    seance_temp = searchSeance(num_semaine1, num_jour1, num_seance1)
    # Note: Function searchSeance return a variable type Seance base on date and time. This returned variable is found in
    # in the ListeSeances.csv

    # Create a new class (seance) base on the subject info (taken from seance_temp) and the date and time (2) to replace
    nouv_seance = Classes.Seance(id=seance_temp.id, type=seance_temp.type, numSemaine=num_semaine2, numJour=num_jour2, numSeance=num_seance2, numClasse=seance_temp.numClasse)
    # Then, verify whether the new class satisfy the adding conditions
    addSeance = nouv_seance.verifySeance()

    # If we found the class to be replaced and the destine date and time (2) is available
    if seance_temp != 0 and addSeance:
        label1.config(text="seance found!")
        # 1- Remove the class to be changed
        seance_temp.deleteSeance()
        # 2- Re-increase the number of hour left base on the information of the chosen class (id and type)
        for mat in matieres.listeM:
            if mat.id == int(seance_temp.id):
                if seance_temp.type == 'CM':
                    mat.heureCM += 1
                elif seance_temp.type == 'TD':
                    mat.heureTD += 1
                elif seance_temp.type == 'TP':
                    mat.heureTP += 1

        # Write the class with date and time (2) changed to 'ListeSeances.csv' to update
        nouv_seance.writeToCsv('./ListeSeances.csv')

        # Then, update the actual hour of the subject left by referencing the id of the subject:
        for mat in matieres.listeM:
            # Verify first if there is available class left to add
            if nouv_seance.id == mat.id:
                if nouv_seance.type == 'CM' and mat.heureCM > 0:
                    mat.heureCM -= 1
                elif nouv_seance.type == 'TD' and mat.heureTD > 0:
                    mat.heureTD -= 1
                elif nouv_seance.type == 'TP' and mat.heureTP > 0:
                    mat.heureTP -= 1
                else:  # If cannot add in a new class since there is no available class left, send error message
                    tk.messagebox.showerror(message=f'There is no class {nouv_seance.type} of {mat.nom} left!')

        # Test function: to print out the current statistics of the subject by update the label1
        num = int(nouv_seance.id)
        label1.config(
            text=f'{nouv_seance.type} of {matieres.listeM[nouv_seance.id]} replaced! Class left: CM[{matieres.listeM[num].heureCM}] TD[{matieres.listeM[num].heureTD}] TP[{matieres.listeM[num].heureTP}]',
            font=('Arial', 13))

    # If we cannot found the class to be moved base on date and time (1) input, send a message through label1
    elif seance_temp == 0:
        label1.config(text="Seance not found!")


## USER INTERFACE
# Add seance
label_seance = tb.Label(tab1, text="Selectionner la matière:", font=('Arial', 11, 'italic'))
label_seance.grid(row=3, pady=10)

combo_seance = tb.Combobox(tab1, bootstyle='secondary', values=Classes.col.listeM)
combo_seance.grid(row=3, column=1)

# Radio buttons: Choosing class type (CM, TD, TP)
label_radio = tb.Label(tab1, text="Type: ", font=('Arial', 11, 'italic'))
label_radio.grid(row=3, column=4, padx=30)

r = IntVar()  # A continously changing variable keep track the value of the radiobuttons

tb.Radiobutton(tab1, text="CM  ", bootstyle="secondary", variable=r, value=1).grid(row=3, column=5)
tb.Radiobutton(tab1, text="TD  ", bootstyle="secondary", variable=r, value=2).grid(row=3, column=6)
tb.Radiobutton(tab1, text="TP  ", bootstyle="secondary", variable=r, value=3).grid(row=3, column=7)

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


# SUPRIMMER UNE SEANCE

label_semaine2 = tb.Label(tab2, text="Saisir la semaine: ", font=('Arial', 11, 'italic'))
label_semaine2.grid(row=4, padx=40, pady=10)

semaine2 = tb.Entry(tab2, bootstyle="secondary")
semaine2.grid(row=4, column=1, ipadx=8.5)

label_jour2 = tb.Label(tab2, text=" Jour de semaine: ", font=('Arial', 11, 'italic'))
label_jour2.grid(row=5)

jour2 = tb.Combobox(tab2, bootstyle='secondary', values=Classes.jours)
jour2.grid(row=5, column=1)

label_numSeance2 = tb.Label(tab2, text="Numero de la seance: ", font=('Arial', 11, 'italic'))
label_numSeance2.grid(row=6, pady=10)

seance2 = tb.Combobox(tab2, bootstyle="secondary", values=[1, 2, 3, 4])
seance2.grid(row=6, column=1)

button2 = tb.Button(tab2, text="Supprimer", bootstyle="primary", command=lambda: supprimeSeance())
button2.grid(row=7, column=3, pady=10)


# DEPLACER UNE SEANCE

label_date1 = tb.Label(tab3, text="Info de la séance (1)", font=('Arial', 11, 'italic'))
label_date1.grid(row=1)

label_date2 = tb.Label(tab3, text="Info de la séance (2)", font=('Arial', 11, 'italic'))
label_date2.grid(row=1, column=2)

# Date and time (1)
label_semaine3 = tb.Label(tab3, text="Saisir la semaine: ", font=('Arial', 11, 'italic'))
label_semaine3.grid(row=4, padx=30, pady=10)

semaine3 = tb.Entry(tab3, bootstyle="secondary")
semaine3.grid(row=4, column=1, ipadx=8.5)

label_jour3 = tb.Label(tab3, text=" Jour de semaine: ", font=('Arial', 11, 'italic'))
label_jour3.grid(row=5)

jour3 = tb.Combobox(tab3, bootstyle='secondary', values=Classes.jours)
jour3.grid(row=5, column=1)

label_numSeance3 = tb.Label(tab3, text="Numero de la seance: ", font=('Arial', 11, 'italic'))
label_numSeance3.grid(row=6, pady=10)

seance3 = tb.Combobox(tab3, bootstyle="secondary", values=[1, 2, 3, 4])
seance3.grid(row=6, column=1)

button3 = tb.Button(tab3, text="Déplacer", bootstyle="primary", command=lambda: deplaceSeance())
button3.grid(row=7, column=2, pady=10)

# Date and time (2)
label_semaine4 = tb.Label(tab3, text="Saisir la semaine: ", font=('Arial', 11, 'italic'))
label_semaine4.grid(row=4, column=2, padx=30)

semaine4 = tb.Entry(tab3, bootstyle="secondary")
semaine4.grid(row=4, column=3, ipadx=8.5)

label_jour4 = tb.Label(tab3, text=" Jour de semaine: ", font=('Arial', 11, 'italic'))
label_jour4.grid(row=5, column=2)

jour4 = tb.Combobox(tab3, bootstyle='secondary', values=Classes.jours)
jour4.grid(row=5, column=3)

label_numSeance4 = tb.Label(tab3, text="Numero de la seance: ", font=('Arial', 11, 'italic'))
label_numSeance4.grid(row=6, column=2, pady=10)

seance4 = tb.Combobox(tab3, bootstyle="secondary", values=[1, 2, 3, 4])
seance4.grid(row=6, column=3)


### Testing
label1 = tb.Label(bootstyle='success')
label1.grid(row=8)

root.mainloop()

print(getIdSeance("MAEL"))
printSeances()
# print(combo_seance)
# sem.numS[1][0] = Classes.Seance(id=1, hCM=2)
