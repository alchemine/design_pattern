from abc import ABCMeta, abstractmethod


class Trip(metaclass=ABCMeta):
    @abstractmethod
    def setTransport(self):
        pass
    @abstractmethod
    def day1(self):
        pass
    @abstractmethod
    def day2(self):
        pass
    @abstractmethod
    def day3(self):
        pass
    @abstractmethod
    def returnHome(self):
        pass
    def itinerary(self):
        self.setTransport()
        self.day1()
        self.day2()
        self.day3()
        self.returnHome()
class VeniceTrip(Trip):
    def setTransport(self):
        print("Take a boat and find your way in the Grand Canal")
    def day1(self):
        print("V1")
    def day2(self):
        print("V2")
    def day3(self):
        print("V3")
    def returnHome(self):
        print("VrH")
class MaldivesTrip(Trip):
    def setTransport(self):
        print("On foot, on any island, Wow!")
    def day1(self):
        print("M1")
    def day2(self):
        print("M2")
    def day3(self):
        print("M3")
    def returnHome(self):
        print("MrH")


class TravelAgency:
    def arrange_trip(self):
        choice = input("What kind of place you'd like to go historical or to a beach?")
        if choice == 'historical':
            self.trip = VeniceTrip()
            self.trip.itinerary()
        if choice == 'beach':
            self.trip = MaldivesTrip()
            self.trip.itinerary()

TravelAgency().arrange_trip()
