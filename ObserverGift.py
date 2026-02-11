class Elf:
    def update(self, gift):
        pass
        
class NotificationPublisher:
    def __init__(self):
        self.subscribers = []
        self.assignments = {}

    def register_elf(self, subscriber):
        self.subscribers.append(subscriber)

    def remove_elf(self, subscriber):
        self.subscribers.remove(subscriber)

    def assign_elf_to_gift(self, elf, gift_index):
        if gift_index not in self.assignments:
            self.assignments[gift_index] = []
        if elf not in self.assignments[gift_index]:
            self.assignments[gift_index].append(elf)

    def get_elfs_for_gift(self, gift_index):
        return self.assignments.get(gift_index, [])

    def notify_elf(self, gift, gift_index=None):
        if gift_index is not None and gift_index in self.assignments:
            for subscriber in self.assignments[gift_index]:
                subscriber.update(gift)
        else:
            for subscriber in self.subscribers:
                subscriber.update(gift)


class ConcreteSubscriber(Elf):
    def __init__(self, name):
        self.name = name
        self.assigned_gifts = []

    def update(self, gift):
        print(f'{self.name} travaille sur : {gift}')

    # def __repr__(self):
    #     return self.name