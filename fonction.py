# pour creer une fonction en python on utilise mot cle def
#fonction sans parametre,avec parametre aura en parathese les elements,et fonction qui retourne
# fonction sans parametre

# def afficher_message():
#     print("bonjour lulu")
# afficher_message()

# def affiche_nom_postnom(nom,postnom):
#     print("Nom :",nom)
#     print("postnom",postnom)
    
# affiche_nom_postnom("dupont","lulu")
#exercice pour trouver le maximum dans une liste

# liste=[2,4,5,10]
# maximum=max(liste)
# minimum=min(liste)
# print(maximum)
 #class rectange:
     #longeur = 3
     #largeur = 4
     #quand on cree une classe la premiere letrre doit etre en majuscule et au cas ou il 
    # y'a plusieur mots ecrivez ex:RectangeClasse,chaque debut du mot par lettre majuscule et pas de separation
     
class Rectange:
     def __init__(self,longeur,largeur,couleur="red"):
         self.longeur=longeur
         self.largeur=largeur
         self.couleur=couleur
     def calculer_surface(self):
          return self.longeur*self.largeur
     def additionner(self):
         return self.longeur+self.largeur
     
#le nom de l'estance doite etre different par rapport au nom d'une classe      
rectange=Rectange(5,2,"blue")
# print(rectange.longeur)
# print(rectange.largeur)
# print(rectange.couleur)
print(rectange.calculer_surface())
print(rectange.additionner())
  