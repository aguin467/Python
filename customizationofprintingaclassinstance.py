class Car:
    def _init_(self, make, model, year, miles, price):
        self.make = make
        self.model = model
        self.year = year
        self.miles = miles
        self.price = price

    def _str_(self):
        return('%d %s: \n Milage: %d \n Sticker price: %d') % (self.year, self.make, self.miles, self.price)

cars = []
cars.append(Car('Ford', 'Mustang', 2013, 25000, 37999))
cars.append(Car('Nissan', 'Xterra', 2004, 89500, 7500))
cars.append(Car('Nissan', 'Mazda', 2012, 25000, 15750))

for car in cars:
    print(car)
