class Elf:
    def update(self, gift):
        pass
        
class NotificationPublisher:
    def __init__(self):
        self.subscribers = []

    def register_elf(self, subscriber):
        self.subscribers.append(subscriber)

    def remove_elf(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify_elf(self, gift):
        for subscriber in self.subscribers:
            subscriber.update(gift)
            
class ConcreteSubscriber(Elf):
    def __init__(self, name):
        self.name = name

    def update(self, gift):
        print(f'{self.name} received : {gift}')