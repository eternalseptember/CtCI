from parking_lot import *


parking_lot_1 = Parking_Lot(20)

car1 = Car('TEST-123')
car2 = Car('ABC-4568')

parking_lot_1.car_park(5, car1)
parking_lot_1.car_park(8, car2)

print(parking_lot_1)



