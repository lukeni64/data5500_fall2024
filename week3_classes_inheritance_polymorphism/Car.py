# Car Class Example
class Car:
    def __init__(self, make, model, year, mileage, original_price):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.original_price = original_price

    def calc_value(self, current_year):
        return self.original_price * (.90 **(current_year - self.year))


andys_car = Car("Toyota", "Sequoia", 2014, 130000, 70000)
print(andys_car.calc_value(2024))

parkers_car = Car("Mazda", "3", 2014, 170000, 25000)
print(parkers_car.calc_value(2024))

katies_car = Car("Subaru", "Crosstrek", 2023, 16000, 25000)
print(katies_car.calc_value(2024))
        
corvette_car = Car("Chevrolet", "Corvette", 1967, 1000, 12000)
print(corvette_car.calc_value(2024))

class AntiqueCar(Car):
    def calc_value(self, current_year):
        return self.original_price * (1.10 **(current_year - self.year))

gregs_car = AntiqueCar("Cadillac", "Coupe De Ville", 1978, 50000, 10000)
print(gregs_car.calc_value(2024))


car_lot = [andys_car, parkers_car, katies_car, gregs_car]
total_car_lot_value = 0

for car in car_lot:
    total_car_lot_value += car.calc_value(2024)
    
print("total value:", total_car_lot_value )
#     def current_value(self, current_year):
#         return self.original_price * (.90 ** (current_year - self.year))
        
        
# andys_car = Car("Toyota", "Sequoia", 2001, 275000, 45000)

# print("andys_car value:", andys_car.current_value(2023))

# # AntiqueCar Class Example
# class AntiqueCar(Car):
#     def current_value(self, current_year):
#         return self.original_price * (1.03 ** (current_year - self.year))
        
        
# gregs_car = AntiqueCar("Cadillac", "DeVille", 1976, 100000, 18000)

# print("gregs_car value: ", gregs_car.current_value(2023))

# #Polymorphism

# johnnys_car = Car("Ford", "F150", 2015, 55000, 45000)
# jennys_car = Car("Toyota", "Rav1", 2006, 125000, 20000)

# car_lot = [andys_car, johnnys_car, jennys_car, gregs_car]

# total_value = 0.0

# for car in car_lot:
#     total_value += car.current_value(2023)
#     print(type(car))
    
# print("all cars value: ", total_value)

