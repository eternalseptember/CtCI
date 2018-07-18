# Design a parking lot using object-oriented principles.


class Parking_Lot():
    def __init__(self, num_spots):
        self.num_spots = num_spots


    def initial_parking_spaces(self, num_spots):
        parking_spots = {}

        for i in range(1, num_spots + 1):
            parking_spots[i] = None

        return parking_spots


    # list of available spots
    # car park on a spot
    # car leaves


