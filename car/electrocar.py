from car import carclass


class ElectroCar(carclass.CarClass):
    def __init__(self, brand, model, year, probeg):
        super().__init__(brand, model, year, probeg)
        self.battery = 100

    def description_battery(self):
        print(f"Этот автомобиль имеет мощность {self.battery}%")


# print(__name__)
