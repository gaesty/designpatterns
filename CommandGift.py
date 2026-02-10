# class Command:
#     def execute(self):
#         pass


# class Gift:
#     def toy_gift(self):
#         print("Le cadeau sélectionné est un Jouet")

#     def electronic_gift(self):
#         print("Le cadeau sélectionné est une Console")

#     def book_gift(self):
#         print("Le cadeau sélectionné est un Livre")


# class ToyGiftCommand(Command):
#     def __init__(self, gift):
#         self.gift = gift

#     def execute(self):
#         self.gift.toy_gift()


# class ElectronicGiftCommand(Command):
#     def __init__(self, gift):
#         self.gift = gift

#     def execute(self):
#         self.gift.electronic_gift()


# class BookGiftCommand(Command):
#     def __init__(self, gift):
#         self.gift = gift

#     def execute(self):
#         self.gift.book_gift()


# class GiftSelector:
#     def __init__(self):
#         self.gift = None

#     def set_gift(self, gift):
#         self.gift = gift

#     def select_gift(self):
#         if self.gift:
#             self.gift.execute()

class GiftOrderCommand:
    def __init__(self, facade):
        self.facade = facade
        
    def execute(self, gift_type, strategy):
        self.facade.prepare_and_deliver_gift(gift_type, strategy)