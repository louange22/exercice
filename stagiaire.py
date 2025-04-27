class Stagiaire:
#constructeur
   def __init__(self,num1=None,age=None,nom=None,prenom=None,note1=None,note2=None):
#rendre tous les attributs prives      
       self.__numeinscription=num1
       self.__age=age
       self.__nom=nom
       self.__prenom=prenom
       self.__note1=note1
       self.__note2=note2
   def calculMoy(self):
       moy=(self.__note1*self.__note2)/2
       print("la moyenne",moy)
       
       #get and set
   def getnumei(self):
       return self.__num1
   def setnum1(self,num1):
       self.__num1=num1
   def getage(self):
       return self.__age
   def setage(self,age):
       self.__age = age
   def getnom(self):
       return self.__nom
   def setnom(self,nom):
       self.__nom = nom
   def getprenom(self):
       return self.__prenom
   def setprenom(self,prenom):
       self.__prenom = prenom
   def getnote1(self):
       return self.__note1
   def setnote1(self,note1):
       self.__note1 = note1
   def getnote2(self):
       return self.__note2
   def setnote2(self,note2):
       self.__note2 = note2
#creation des  objets
s1=Stagiaire(1122,21,"elgarrai","zineb",12,2,18)
#creer s2
s2=Stagiaire()
s2.setnum1(2211)
s2.setage(15)
s2.setnom("aloui")
s2.setprenom("aya")
s2.setnote1(15.2)
s2.setnote2(28)        
          
             
           
        

    