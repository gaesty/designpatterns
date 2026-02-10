class FactoryGift:
    # def __init__(self, name):
    #     self.name = name
        
    def create_new_gift(self, name):
        if name == 'electronic':
            return Electronic()
        elif name == 'toy':
            return Toy()
        elif name == 'book':
            return Book()
        else :
            pass
            
class Book:
    def createGift(self):
        return "Création d'un livre "
        
class Toy:
    def createGift(self):
        return "Création d'un jouet "
        
class Electronic:
    def createGift(self):
        return "Création d'une console "
