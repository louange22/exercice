from abc import ABC
class Shape(ABC):
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,length):
        self.length=length
        
    def area(self):
        return self.length * self.length
    
class Triangle(Shape):
    def __init__(self,base,hauteur):
        self.base=base
        self.hauteur=hauteur
        
    def surface_triange(self):
        return (self.base*self.hauteur)/2
    
triange_surgf=Triangle(5,7)
print(triange_surgf.surface_triange())            
        
square = Square(4)
#square_area=square.area()
#print(square_area)


  