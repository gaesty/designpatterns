from FacadeGift import FacadeGift
from CommandGift import GiftOrderCommand
from StrategyGift import DeliveryContext, DroneStrategyDelivery, ElfStrategyDelivery, SleighStrategyDelivery

santa = FacadeGift()

order = GiftOrderCommand(santa)
delivery = DeliveryContext()

# order.execute(gift_type="toy", strategy=DroneStrategyDelivery())
# order.execute(gift_type="book", strategy=ElfStrategyDelivery())
# order.execute(gift_type="electronic", strategy=SleighStrategyDelivery())

# gift_types = ["toy", "toy", "book", "electronic", "electronic", "electronic"]
# strategies = [
#     DroneStrategyDelivery(), DroneStrategyDelivery(),
#     ElfStrategyDelivery(),
#     SleighStrategyDelivery(), SleighStrategyDelivery(), DroneStrategyDelivery()
# ]

# order.execute(gift_types=gift_types, strategies=strategies, nbElf=3)
# 


gift_types = ["toy", "toy", "book", "electronic", "electronic", "electronic"]
strategies = [
    DroneStrategyDelivery(), DroneStrategyDelivery(),
    ElfStrategyDelivery(),
    SleighStrategyDelivery(), SleighStrategyDelivery(), DroneStrategyDelivery()
]


print("MODE 1 : Distribution round-robin automatique")
order.execute(gift_types=gift_types, strategies=strategies, nbElf=3)

print("MODE 2 : Assignation manuelle (many-to-many)")

santa2 = FacadeGift()
order2 = GiftOrderCommand(santa2)
assignments = {
    0: [0, 1],
    1: [2],
    2: [0, 2],
    3: [1],
    4: [0, 1, 2],
    5: [0],
}

order2.execute(gift_types=gift_types, strategies=strategies, nbElf=3, assignments=assignments)