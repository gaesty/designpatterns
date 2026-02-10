from FacadeGift import FacadeGift
from CommandGift import GiftOrderCommand
from StrategyGift import DeliveryContext, DroneStrategyDelivery, ElfStrategyDelivery, SleighStrategyDelivery

santa = FacadeGift()

order = GiftOrderCommand(santa)
delivery = DeliveryContext()

order.execute(gift_type="toy", strategy=DroneStrategyDelivery())
order.execute(gift_type="book", strategy=ElfStrategyDelivery())
order.execute(gift_type="electronic", strategy=SleighStrategyDelivery())
