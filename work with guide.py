class Cars:

    def __init__(self, model):
        self.model = model
        self.in_move = False

    def drive(self):
        self.in_move = True

    def stop(self):
        self.in_move = False

    def get_info(self):
        return self.model

class Mercedes(Cars):

    def __init__(self, model, year):
        super().__init__(model=model)
        self.year = year

    def get_info(self):
        return f'Model: {self.model}, year: {self.year}'

class BMW(Cars):

    def __init__(self, model='X3'):
        super().__init__(model=model)

    def lock_car(self):
        self.is_locked = True

    def unlock_car(self):
        self.is_locked = False

if __name__ == '__main__':
    car1 = Cars('Lada Vesta')
    car2 = Mercedes('E240', 2001)
    car3 = BMW()

    cars = [car1, car2, car3]

    for car in cars:
        print(car.model)

    print(car1.get_info())
    print(car2.get_info())
    car3.lock_car()
    print(car3.is_locked)


