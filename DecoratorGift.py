class GiftDecorator:        
    def __init__(self, gift):
     self.gift = gift
    
     def createGift(self):
         return self.gift.createGift()


class RubanGiftDecorator(GiftDecorator):
    def __init__(self, wrapping):
        self.wrapping = wrapping
    def createGift(self):
        return self.wrapping.createGift() + "Ruban "

class WrappingPaperGiftDecorator(GiftDecorator):
    def __init__(self, wrapping):
        self.wrapping = wrapping
    def createGift(self):
        return self.wrapping.createGift() + "Papier Cadeau " 
        
class BoxGiftDecorator(GiftDecorator):
    def __init__(self, wrapping):
        self.wrapping = wrapping
    def createGift(self):
        return self.wrapping.createGift() + "Boite " 
        
        