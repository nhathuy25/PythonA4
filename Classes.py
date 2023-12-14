'''
Description of Classes.py:
The file include all the classes necessary, and its methods to read/write with .csv file
'''

import tkinter as tk
from tkinter import messagebox
import csv
#Pandas library to delete single
import pandas as pd

class Matiere:
    def __init__(self, id:int, nom='', heureCM=0, heureTD=0, heureTP=0):
        self.id = id
        self.nom = nom
        self.heureCM = heureCM
        self.heureTD = heureTD
        self.heureTP = heureTP

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


    # Function verifySeance: to verify the condition before adding a class to csv, including whether the time table
    # is free or not at the moment; is the new class conflicts the hierarchy of CM > TD > TP?
    # PROBLEM: CAUSING OVERFLOW EACH TIME CONDUCTING VERIFICATION
    def verifySeance(self):
        file=open('./ListeSeances.csv', 'r')
        line=file.readline()
        verified=True
        lineNumber=1
        while line!='':
            line.strip('"')
            if line!='' and line[0]!='#':
                fields=line.split(';')
                # 1st condition: Verify if the same class is already added:
                if self.id==int(fields[0]) and self.type==fields[1] and self.numSemaine==int(fields[2]) and self.numJour==int(fields[3]) and self.numSeance==int(fields[4]) and self.numClasse==int(fields[5]):
                    verified=False
                    tk.messagebox.showerror(message=f'There is already a same class of {col.listeM[int(fields[0])]}',
                                            title="Error")
                    return verified

                # 2nd condition: CM>TD>TP
                elif self.numSemaine==int(fields[2]) and self.numJour==int(fields[3]) and self.numSeance==int(fields[4]):
                    if fields[1] == 'CM':
                        verified = False
                        tk.messagebox.showerror(message=f'There is already a CM of {col.listeM[int(fields[0])]}', title="Error")
                        return verified
                    elif fields[1] == 'TD' and ((self.type == 'TD' and self.numClasse == int(fields[5])) or self.type != 'TD'):
                        verified = False
                        tk.messagebox.showerror(message=f'There is already a class {fields[1]} of {col.listeM[int(fields[0])]}', title="Error")
                        return verified
            line=file.readline()
            lineNumber+=1
        file.close()
        return verified

    # Function deleteSeance: to delete a class from inputs of the program
    def deleteSeance(self):
        file = open('./ListeSeances.csv', 'r+')
        line = file.readline()
        deleted = False
        lineNumber = 0
        while line != '':
            line.strip('"')
            if line != '' and line[0] != '#':
                fields = line.split(';')
                if self.numSemaine==int(fields[2]) and self.numJour==int(fields[3]) and self.numSeance==int(fields[4]):
                    # Using library pandas to remove class directly in the csv file without creating a new one
                    # First by read the csv file into pandas DataFrame
                    df = pd.read_csv('./ListeSeances.csv',delimiter="'")
                    #Delete a row base on it's line number
                    df = df.drop(df.index[lineNumber-1])
                    # Reset the index to avoid gaps
                    df = df.reset_index(drop=True)
                    df.to_csv('./ListeSeances.csv', index=False, sep="'")
                    deleted = True
                    tk.messagebox.showinfo(title='Delete a class', message=f'Deleted {col.listeM[int(fields[0])].nom} {fields[1]}!')
                    # Function return fields with all the infomation of the class to update hour in main.py
                    return fields
            line = file.readline()
            lineNumber+=1
        file.close()
        return 0

    # Function moveSeance: to move a class to another date and time
    def moveSeance(self):
        pass

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
        file.close()

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


col = ListeDeMatiere()
col.readFromCsv('./ListeDeMatiere.csv')

