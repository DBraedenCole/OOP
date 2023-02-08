import random 

class Insect:

    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.flight = None

    def flight_time(self):
        self.flight = random.randint(1,10)

    def get_flight_time(self):
        return self.flight