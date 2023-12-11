from enum import Enum, auto
import numpy as np
import csv

class Matiere:
    def __init__(self, id:int, nom='', heureCM=0, heureTD=0, heureTP=0):
        self.id = id
        self.nom = nom
        self.heureCM = heureCM
        self.heureTD=heureTD
        self.heureTP=heureTP

    def __repr__(self):
        return self.nom

    def stringForCsv(self):
        return self.nom+';'+str(self.heureCM)

class Seance:
    def __init__(self, id:int, type:str, numSemaine:int, numJour:int, numSeance:int, numClasse=0):
        self.id=id
        self.type=type
        self.numSemaine=numSemaine
        self.numJour=numJour
        self.numSeance=numSeance
        self.numClasse=numClasse

    def stringForCsv(self):
        return [self.id, self.type, self.numSemaine, self.numJour, self.numSeance, self.numClasse]

    def writeToCsv(self, filename):
        #Write a new line of class into the file
        with open(filename, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=';')
            csv_writer.writerow(self.stringForCsv())
        # - After that, remove the existing hour of the class base on the type (CM, TD, TP)


    # Function verifySeance: to verify the condition before adding a class to csv, including whether the time table
    # is free or not at the moment; is the new class conflicts the hierarchy of CM > TD > TP?
    # PROBLEM: CAUSING OVERFLOW EACH TIME CONDUCTING VERIFICATION
    def verifySeance(self, fileListeSeance):
        file=open(fileListeSeance, 'r')
        line=file.readline()
        verified=True
        lineNumber=1
        while line!='':
            line.strip('"')
            if line!='' and line[0]!='#':
                fields=line.split(';')
                # 1- Verify if the class is already added:
                if self.id==int(fields[0]) and self.type==fields[1] and self.numSemaine==int(fields[2]) and self.numJour==int(fields[3]) and self.numSeance==int(fields[4]) and self.numClasse==int(fields[5]):
                    verified=False
                # 2- Condition CM>TD>TP
                if self.id==int(fields[0]) and self.type==fields[1] and self.numSemaine==int(fields[2]) and self.numJour==int(fields[3]) and self.numSeance==int(fields[4]):
                    if self.numClasse > int(fields[5]):
                        verified=False
        return verified


    def  __repr__(self):
        return f'ID: {self.id}, hCM: {self.heureCM}'

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
                    self.listeM.append(Matiere(id=int(fields[0]), nom=fields[1], heureCM=int(fields[2]), heureTD=int(fields[3]), heureTP=int(fields[4])))

            line = file.readline()
            lineNumber+=1
        file.close()
        return True

    def updateActualList(self, file_seances):
        file = open(file_seances, 'r')
        line = file.readline()
        lineNumber = 1

        while line != '':
            line = line.strip('"')
            if line != '' and line[0] != '#':
                fields = line.split(';')
                addSeance = True
                # Dieu kien de addseance

                if addSeance:
                    seance = Seance(id=int(fields[0]), type=fields[1], numSemaine=int(fields[2]), numSeance=int(fields[3]), numJour=int(fields[4]))
                    for mat in self.listeM:
                        if seance.id == mat.id:
                            if seance.type == 'CM':
                                mat.heureCM -= 2
                            elif seance.type == 'TD':
                                pass
                            elif seance.type == 'TP':
                                pass

            line = file.readline()
            lineNumber += 1

    def __repr__(self):
        s=''
        for mat in self.listeM:
            s+=repr(mat)+'\n'
        return s


class ListeDeSeance:
    def __init__(self):
        self.listeSeance=[]

    def readFromCsv(self):
        file = open('./ListeSeances.csv', 'r')
        line=file.readline()
        lineNumber=1

        while line!='':
            line=line.strip('"')
            if line!='' and line[0]!='#':
                fields=line.split(';')
                addSeance=True

                if addSeance:
                    self.listeSeance.append(Seance(id=int(fields[0]), type=fields[1], numSemaine=int(fields[2]), numJour=int(fields[3])
                                                   , numSeance=int(fields[4]), numClasse=int(fields[5])))
            line=file.readline()
            lineNumber+=1
        file.close()
        return True


jours = ["Lundi", "Mardi", "Mecredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

class Semaine:
    def __init__(self):
        self.numS = []
        for i in range(20): #There are 20 weeks
            seances = []
            for j in range(27): #There are 27 classes in a week
                seances.append(Seance(99,""))
            self.numS.append(seances)


    def __repr__(self):
        return f'Semaine: {str(self.numS)} Date: {self.date}, Seances: {self.list_seance}'
    #    return self.numSemaine + ', ' + str(self.date) +', '+str(self.j)+', '+self.list_seance

col = ListeDeMatiere()
col.readFromCsv('./ListeDeMatiere.csv')

