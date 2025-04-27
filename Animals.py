class Animal:
    def crier(self):
        print("Un cri d'animal")
        
class Chien(Animal):
    def crier(self):
        print("waou! waou!")
        
class Chat(Animal):
    def crier(self):
        print("milou")
             
class Inconnu(Animal):
    def crier(self):
        return super().crier() 
animal=Animal()
crie_animal=animal.crier()

chien = Chien()
crie_chien=chien.crier

chat=Chat()
cri_chat=chat.crier()

inconnu=Inconnu()
crie_animal=inconnu.crier()
print()               