class boite_outil:
    def __init__(self,idboite,marque,date_fabricat,prix=20):
        self.idboite=idboite
        self.marque=marque
        self.date_fabriquant=date_fabricat
        self.prise=prix
    def ajouter(self):
        print("ajouter l'outil ")
    def diminuer(self):
        print("diminuer l'outil")        

class marteaux:
    def __init__(self,num_marteau,couleur_marteaux):
        self.n_mateau=num_marteau
        self.couleur_marteau=couleur_marteaux
    def planter(self):
        print("planter les clou")
    def retirer(self):
        print("retirer le clous")
    def changer_couleur(self):
        print("modifier la couleur du martau")        
        
        
class tournevis:
    def __init__(self,taille,marque):
        self.taille=taille
        self.marq=marque
    def serrer(self):
        print("serrer le vis")
    def desserer(self):
        print("desserer le vis")       
    
              
    