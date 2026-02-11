class StrategyDelivery():
    def deliver(self):
        pass
        
class DroneStrategyDelivery(StrategyDelivery):
    def deliver(self):
         print("Livraison par un Drone")
        
class ElfStrategyDelivery(StrategyDelivery):
    def deliver(self):
         print("Livraison par un Elf")

class SleighStrategyDelivery(StrategyDelivery):
    def deliver(self):
         print("Livraison par Traineau")
        
class DeliveryContext():
    def __init__(self):
        self.delivery_strategy = None

    def set_delivery_strategy(self, delivery_strategy):
        self.delivery_strategy = delivery_strategy
     
    def make_delivery(self):
        if self.delivery_strategy is not None:
            self.delivery_strategy.deliver()
           