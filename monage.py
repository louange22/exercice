class MonAge:
    def __init__(self,anneeEncour,anneeNaissance=200):
        self.anneeEncou=anneeEncour
        self.anneeNaissance=anneeNaissance
    def calcul(self):
        return self.anneeEncou-self.anneeNaissance    
mon_age=MonAge(2025,2004)
print(mon_age.anneeEncou)
print(mon_age.anneeNaissance)
print(mon_age.calcul())      