class CarRecord:
	def _init_(self):
		self.year_made = 0
		self.car_vin = ' '

	def _str_(self):
		return ('Year: %s, VIN: %s' % (self.year_made, self.car_vin))


my_car = CarRecord()
my_car.year_made = 2009
my_car.car_vin = 'ABC321'

print(my_car)


class Toy:
    def __init__(self, name, price, min_age):
        self.name = name
        self.price = price
        self.min_age = min_age

    def __str__(self):
        return ('%s costs only $%.2f. Not for children under %d!' %
                (self.name, self.price, self.min_age))


truck = Toy('Monster Truck XX', 14.99, 5)
print(truck)
