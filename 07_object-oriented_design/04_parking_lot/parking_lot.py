# Design a parking lot using object-oriented principles.


class Car():
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return str(license_plate)


class Parking_Lot():
    def __init__(self, num_spots):
        self.num_of_spots = num_spots
        self.num_of_free_spots = num_spots

        self.parking_lot = self.initial_parking_spaces(num_spots)



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


    def car_park(self, spot, car):
        # Parking lots are numbered from 1 to num_spots.
        # should probably add something in so people don't park in the same spot.
        self.parking_lot[spot] = car
        self.num_of_free_spots -= 1


    def car_leave(self, spot):
        self.parking_lot[spot] = None
        self.num_of_free_spots += 1


    def __str__(self):
        info = ''

        for spot in range(1, self.num_of_spots+1):
            info += 'Spot {0}: {1}\n'.format(spot, self.parking_lot[spot])

        return info



