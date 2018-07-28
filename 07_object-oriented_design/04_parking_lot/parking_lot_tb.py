from parking_lot import *


parking_lot_1 = Parking_Lot(20)

car1 = Car('TEST-123')
car2 = Car('ABC-4568')
car3 = Car('756')

parking_lot_1.car_park(5, car1)
parking_lot_1.car_park(8, car2)

# trying to park in an occupied spot
parking_lot_1.car_park(5, car3)

# car3 finds another spot
parking_lot_1.car_park(2, car3)

# car1 leaves the lot
parking_lot_1.car_leave(5)
print(parking_lot_1)

