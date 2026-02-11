from DecoratorGift import RubanGiftDecorator, WrappingPaperGiftDecorator
from FactoryGift import FactoryGift
from ObserverGift import ConcreteSubscriber, NotificationPublisher
from StrategyGift import DeliveryContext


class FacadeGift:
    def __init__(self):
        self.factory = FactoryGift()
        self.workshop = NotificationPublisher()
        self.context = DeliveryContext()
        self.elfs = []

    def preparator(self, nbElf):
        
        elf_names = ["Aelar","Aerith","Althaea","Amroth","Anarion","Arannis","Arwen","Belanor","Caelynn",
            "Celeborn","Ciryandil","Daeron","Elandril","Elaria","Elrond","Faelar","Felarion","Galadriel",
            "Galanodel","Haldir","Ithilwen","Luthien","Maeglin","Naerwen","Nimrodel","Oropher","Quarion",
            "Rhiannon","Silvyr","Talanor","Thranduil","Tiriel","Valandil","Yavanna","Zantheril",
        ]
        
        i = 0
        while i < nbElf and i < len(elf_names):
            elf = ConcreteSubscriber(elf_names[i])
            self.workshop.register_elf(elf)
            self.elfs.append(elf)
            i += 1

    def assign_elfs_to_gifts(self, gift_types, assignments=None):
           
            if assignments is not None:
                for gift_index, elf_indices in assignments.items():
                    for elf_idx in elf_indices:
                        if elf_idx < len(self.elfs):
                            self.workshop.assign_elf_to_gift(self.elfs[elf_idx], gift_index)
            else:
                for gift_index in range(len(gift_types)):
                    elf = self.elfs[gift_index % len(self.elfs)]
                    self.workshop.assign_elf_to_gift(elf, gift_index)

    def prepare_and_deliver_gift(self, gift_type, delivery_strategy, gift_index):

        gift = self.factory.create_new_gift(gift_type)
        gift = WrappingPaperGiftDecorator(gift)
        gift = RubanGiftDecorator(gift)

        self.context.set_delivery_strategy(delivery_strategy)

        createGift = gift.createGift()
        
        assigned_elves = self.workshop.get_elfs_for_gift(gift_index)
        print(f"Jouet #{gift_index} ({gift_type}) — Elf(es) assigné(s) : {assigned_elves}")
        
        # self.workshop.notify_elf(createGift, gift_index)

        self.workshop.notify_elf(createGift)

        print(createGift)
        print(self.context.make_delivery())
