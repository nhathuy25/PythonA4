import Classes
import tkinter as tk
import tkinter.messagebox
import tkinter.scrolledtext


mainWnd = tk.Tk(className= "Gestion d'emploi du temps")

def AfficherSemaine():
    return 1

def AjouterSeance():
    global entreeSeance, entreeNum_Seance, entreeDate, entreeType

    Seance = entreeSeance.get().strip()

    return 1

startX = 25
startY = 50
offsetX1 = 60
offsetX2 = 250
offsetY = 50

frame = tk.Frame(master=mainWnd, width=690, height=400)
frame.pack()

labelSemaine = tk.Label(master= frame, text='Semaine numéro: ' )
labelSemaine.place(x=3*startX, y= startY)

entreeSemaine = tk.Entry(master= frame)
entreeSemaine.place(x=3*startX+2.75*offsetX1, y=startY)

boutonAugmenter = tk.Button(master= frame, text='>>')
boutonAugmenter.place(x=3*startX+5*offsetX1, y=startY)

boutonDiminuer = tk.Button(master= frame, text='<<')
boutonDiminuer.place(x=3*startX+2*offsetX1, y=startY)

boutonAfficher = tk.Button(master= frame, text="Afficher l'emploi du temps", command=AfficherSemaine())
boutonAfficher.place(x=3*startX+6*offsetX1, y=startY)

labelAjouter = tk.Label(master=frame, text="- Ajouter une séance:")
labelAjouter.place(x=startX, y=startY + offsetY)

labelSeance = tk.Label(master=frame, text="Nom de matière:")
labelSeance.place(x=startX+2.3*offsetX1, y=startY + offsetY)

entreeSeance = tk.Entry(master=frame)
entreeSeance.place(x=startX+offsetX1*4, y=startY + offsetY)

labelDate = tk.Label(master=frame, text="Date:")
labelDate.place(x=startX+6.5*offsetX1, y=startY + offsetY)

entreeDate = tk.Entry(master=frame)
entreeDate.place(x=startX+offsetX1*7.5, y=startY + offsetY)

labelNum_Seance = tk.Label(master=frame, text="Numéro de séance:")
labelNum_Seance.place(x=startX+2.1*offsetX1, y=startY + 2*offsetY)
###
entreeNum_Seance = tk.Entry(master=frame)
entreeNum_Seance.place(x=startX+offsetX1*4, y=startY + 2*offsetY)

labelType = tk.Label(master=frame, text="Type:")
labelType.place(x=startX+6.5*offsetX1, y=startY + 2*offsetY)

entreeType = tk.Entry(master=frame)
entreeType.place(x=startX+offsetX1*7.5, y=startY + 2*offsetY)

boutonAjouter = tk.Button(master=frame, text= "X", command= AjouterSeance())
boutonAjouter.place(x=startX +offsetX1*10, y=startY + 1.5*offsetY)

mainWnd.mainloop()