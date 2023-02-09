class CarClass:
    def __init__(self, brand, model, year, probeg):
        self.brand = brand
        self.model = model
        self.year = year
        self.probeg = int(probeg)

    def show_car(self):
        print(f"{self.brand}, {self.model}, {self.year} год, {self.probeg} км")


# print(__name__)
