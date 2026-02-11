class GiftOrderCommand:
    def __init__(self, facade):
        self.facade = facade
        
    # def execute(self, gift_type, strategy):
    #     self.facade.prepare_and_deliver_gift(gift_type, strategy)
    
    def execute(self, gift_types, strategies, nbElf, assignments=None):
        
        self.facade.preparator(nbElf)
        self.facade.assign_elfs_to_gifts(gift_types, assignments)
        
        for i, (gift_type, strategy) in enumerate(zip(gift_types, strategies)):
            self.facade.prepare_and_deliver_gift(gift_type, strategy, gift_index=i)