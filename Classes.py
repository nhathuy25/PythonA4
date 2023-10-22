from enum import Enum
    
class Seance:
    def __init__(self, id=0, nom=''):
        self.id=id
        self.nom=nom

    def  __repr__(self):
        return self.nom

class Matiere(Seance):
    def __init__(self, id=0, nom='',hCM=0):
        self.id = id
        self.nom = nom
        self.heureCM = hCM

    def __repr__(self):
        return self.nom

    def stringForCsv(self):
        #return self.nom+';'+str(self.heureTD)+';'+self(str.heureTP)
        pass

class ListeDeMatiere:
    def __init__(self):
        self.listeM=[]

    def readFromCsv(self, filename):
        file = open(filename, 'r')

        line = file.readline()
        lineNumber = 1
        while line != '':
            line = line.strip()
            if line!='' and line[0]!='#':
                fields = line.split(';')

                addMatiere = True
                #them dieu kien de add Matiere!

                if addMatiere:
                    self.listeM.append(Matiere(id=fields[0], nom=fields[1], hCM=fields[2]))

            line = file.readline()
            lineNumber+=1
        file.close()
        return True

    def __repr__(self):
        s=''
        for mat in self.listeM:
            s+=repr(mat)+'\n'
        return s

class jour(Enum):
    LUNDI = 1
    MARDI = 2
    MERCREDI = 3
    JEUDI = 4
    VENDREDI = 5
    SAMEDI = 6 
    DIMANCHE = 7

class Date:
    def __init__(self, numS:int, date:str, liste:[3]):
        self.numS = numS
        self.date=date
        self.list_seance=liste

    def __repr__(self):
        return f'Semaine: {str(self.numS)} Date: {self.date}, Seances: {self.list_seance}'
    #    return self.numSemaine + ', ' + str(self.date) +', '+str(self.j)+', '+self.list_seance

col = ListeDeMatiere()
col.readFromCsv('./ListeDeMatiere.csv')

print(col)
