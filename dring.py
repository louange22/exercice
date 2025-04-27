class Drink:
    """Une boisson"""
    def __init__(self,price):
        """initialiser un prix"""
        self.price=price
    def drink(self):
        """boire la boisson"""    
        print(" je ne sais pas ce que c'est mais je dois boire comme ça")
class Coffee(Drink):
    prices = {"simple":1,"serrer":1,"allonge":1.5} 
    
    def __init__(self, type):
        self.type=type
        super().__init__(price=self.prices.get(type,5))
    def drink(self):
        print(f"un bon cafe de{self.type} qui coute {self.price}$ pour me reveiller")
coffe=Coffee("allonge")
boire=coffe.drink()        
                
