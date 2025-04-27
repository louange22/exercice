class Film:
     def __init__(self,name):
         self.name=name
     def watch(self):
         print("je vais etre importante dans le mondeprofessionnel")
        
class FilmCassette(Film):
    pass
film = Film("2004: l'odysse de l'espace")
film_Cassette = FilmCassette("blader runner")
    
print(film.name)
film.watch()
print(film_Cassette.name)
print(film_Cassette.watch())

             
   