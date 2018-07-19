# Design a parking lot using object-oriented principles.


class Parking_Lot():
    def __init__(self, num_spots):
        self.num_spots = num_spots
        self.spots = self.initial_parking_spaces(num_spots)


    def initial_parking_spaces(self, num_spots):
        parking_spots = {}

        for i in range(1, num_spots + 1):
            parking_spots[i] = None

        return parking_spots


    def available_spots(self):
        return None


    def car_park(self, car):
        return None


    def car_leave(self, car):
        return None




