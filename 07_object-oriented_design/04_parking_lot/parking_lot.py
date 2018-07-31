# Design a parking lot using object-oriented principles.


class Car():
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return str(self.license_plate)


class Parking_Lot():
    def __init__(self, num_spots):
        self.num_of_spots = num_spots
        self.num_of_free_spots = num_spots
        self.parking_lot = self.initial_parking_spaces(num_spots)
        self.free_spaces = self.initial_free_space_list(num_spots)


    def initial_parking_spaces(self, num_spots):
        parking_spots = {}

        for i in range(1, num_spots + 1):
            parking_spots[i] = None

        return parking_spots


    def initial_free_space_list(self, num_spots):
        init_list = []

        for i in range(1, num_spots + 1):
            init_list.append(i)

        return init_list


    def how_many_free_spots(self):
        return self.num_of_free_spots


    def which_spots_are_available(self):
        self.free_spaces.sort()
        return self.free_spaces


    def car_enters(self, spot, car):
        # Parking lots are numbered from 1 to num_spots.
        # Check to see if the spot is free.
        if self.parking_lot[spot] is not None:
            return None

        self.parking_lot[spot] = car
        self.num_of_free_spots -= 1
        self.free_spaces.remove(spot)


    def car_leaves(self, spot):
        self.parking_lot[spot] = None
        self.num_of_free_spots += 1
        self.free_spaces.append(spot)


    def __str__(self):
        info = ''

        for spot in range(1, self.num_of_spots+1):
            info += 'Spot {0}: {1}\n'.format(spot, self.parking_lot[spot])

        return info



