from abc import ABC, abstractmethod


# Observer Interface
class ISubscriber(ABC):

    @abstractmethod
    def update(self):
        pass


# Observable Interface
class IChannel(ABC):

    @abstractmethod
    def subscribe(self, subscriber):
        pass

    @abstractmethod
    def unsubscribe(self, subscriber):
        pass

    @abstractmethod
    def notify_subscribers(self):
        pass


# Concrete Subject
class Channel(IChannel):

    def __init__(self, name):
        self.name = name
        self.subscribers = []
        self.latest_video = None

    def subscribe(self, subscriber):
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)

    def notify_subscribers(self):
        for subscriber in self.subscribers:
            subscriber.update()

    def upload_video(self, title):
        self.latest_video = title

        print(f"\n[{self.name} uploaded '{title}']")

        self.notify_subscribers()

    def get_video_data(self):
        return f"\nCheckout our new video: {self.latest_video}\n"


# Concrete Observer
class Subscriber(ISubscriber):

    def __init__(self, name, channel):
        self.name = name
        self.channel = channel

    def update(self):
        print(f"Hey {self.name}, {self.channel.get_video_data()}")


# Main
if __name__ == "__main__":

    channel = Channel("CoderArmy")

    subs1 = Subscriber("Varun", channel)
    subs2 = Subscriber("Tarun", channel)

    channel.subscribe(subs1)
    channel.subscribe(subs2)

    channel.upload_video("Observer Pattern Tutorial")

    channel.unsubscribe(subs1)

    channel.upload_video("Decorator Pattern Tutorial")