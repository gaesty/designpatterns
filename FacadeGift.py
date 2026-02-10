from FactoryGift import FactoryGift
from StrategyGift import DeliveryContext
from ObserverGift import NotificationPublisher, ConcreteSubscriber
from DecoratorGift import WrappingPaperGiftDecorator, RubanGiftDecorator


class FacadeGift:
    def __init__(self):
        self.factory = FactoryGift()
        self.workshop = NotificationPublisher()
        self.workshop.register_elf(ConcreteSubscriber("Buddy"))
        self.workshop.register_elf(ConcreteSubscriber("Jingle"))
        self.context = DeliveryContext()

    def prepare_and_deliver_gift(self, gift_type, delivery_strategy):
        gift = self.factory.create_new_gift(gift_type)
        gift = WrappingPaperGiftDecorator(gift)
        gift = RubanGiftDecorator(gift)
        
        self.context.set_delivery_strategy(delivery_strategy)

        createGift = gift.createGift()

        self.workshop.notify_elf(createGift)

        print(createGift)
        print(self.context.make_delivery())
