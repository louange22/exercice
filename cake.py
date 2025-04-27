class Cake:
    def __init__(self,flavor):
        self.flavor=flavor
    def __cut__put(self):
        print("le gateau est coupe en quatre")
        cake=Cake("chocolate")
        print(cake.flavor)
        cake.__cut__put()
          
        