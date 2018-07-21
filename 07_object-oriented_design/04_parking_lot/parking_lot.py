# Design a parking lot using object-oriented principles.


class Car():
    def __init__(self, owner):
        self.owner = owner



class Parking_Lot():
    def __init__(self, num_spots):
        self.num_spots = num_spots
        self.num_of_free_spots = num_spots

        self.spots = self.initial_parking_spaces(num_spots)



    def initial_parking_spaces(self, num_spots):
        parking_spots = {}

        for i in range(1, num_spots + 1):
            parking_spots[i] = None

        return parking_spots


    def num_of_free_spots(self):
        return self.num_of_free_spots


    def available_spots(self):
        # print a list of free spots?
        return None


    def car_park(self, car):
        self.num_of_free_spots -= 1


    def car_leave(self, car):
        self.num_of_free_spots += 1




