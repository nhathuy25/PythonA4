from main import *


#getIdSeance takes a string which is the name of seance and convert it to index of it in listM
def getIdSeance(nom:str):
    arr = []
    pass
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

def clearEntry():
    combo_seance.delete(0, 'end')
    r.trace_remove()
    seance1.delete(0, 'end')
    jour1.delete(0, 'end')
    semaine1.delete(0,'end')

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
        num_semaine = int(semaine1.get())                   #number of week
    #if one or more fields are missing, send error
    else:
        tk.messagebox.showerror(message="Please fill in all the info!", title="Error")

    sem.numS[num_semaine][num_seance*num_jour]= Classes.Seance(id=id_matiere, hCM=10)
    label1.config(text=f'{sem.numS[num_semaine][num_seance*num_jour]} ajoute! and nom {combo_seance.get()}')

    #Clear entry after hitting the button
    clearEntry()

