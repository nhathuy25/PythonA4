from enum import Enum, auto
import numpy as np
import main

class Seance:
    def __init__(self, id=0, nom=''):
        self.id=id
        self.nom=nom

    def  __repr__(self):
        return self.nom

class Matiere(Seance):
    def __init__(self, id:int, nom='', hCM=0):
        self.id = id
        self.nom = nom
        self.heureCM = hCM

    def __repr__(self):
        return self.nom

    def stringForCsv(self):
        return self.nom+';'+str(self.heureCM)



class ListeDeMatiere:
    def __init__(self):
        self.listeM=[]

    def readFromCsv(self, filename):
        file = open(filename, 'r')

        line = file.readline()
        lineNumber = 1
        while line != '':
            line = line.strip('"')
            if line!='' and line[0]!='#':
                fields = line.split(';')
                addMatiere = True
                #them dieu kien de add Matiere!

                if addMatiere:
                    self.listeM.append(Matiere(id=int(fields[0]), nom=fields[1], hCM=int(fields[2])))

            line = file.readline()
            lineNumber+=1
        file.close()
        return True

    def __repr__(self):
        s=''
        for mat in self.listeM:
            s+=repr(mat)+'\n'
        return s

jours = ["Lundi", "Mardi", "Mecredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

class Semaine:
    def __init__(self):
        self.numS = []
        for i in range(20): #There are 20 weeks
            seances = []
            for j in range(27): #There are 27 classes in a week
                seances.append(Matiere(99,"",99))
            self.numS.append(seances)


    def __repr__(self):
        return f'Semaine: {str(self.numS)} Date: {self.date}, Seances: {self.list_seance}'
    #    return self.numSemaine + ', ' + str(self.date) +', '+str(self.j)+', '+self.list_seance

col = ListeDeMatiere()
col.readFromCsv('./ListeDeMatiere.csv')

col1= ListeDeMatiere()

