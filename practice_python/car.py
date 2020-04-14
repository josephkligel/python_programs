class Car:
    amount_of_cars = 0

    def __init__(self, manufacturer, model , hp):
        self.__hidden = 'Hello, I am a talking car. Shhh, keep it a secret. ;)'
        print(self.__hidden)
        self.manufacturer = manufacturer
        self.model = model
        self.hp = hp
        Car.amount_of_cars += 1

    def print_info(self):
        print(f'Manufacturer: {self.manufacturer}, Model: {self.model}, HP: {self.hp}')

    def print_car_amount(self):
        print(f'Amount: {Car.amount_of_cars}')

    def __del__(self):
        print('Object is deleted!')
        Car.amount_of_cars -= 1

my_car = Car('Tesla', 'Model X', 525)
my_car2 = Car('Ford', 'Mustang', 400)
my_car.print_info()
del my_car2
my_car.print_car_amount()
