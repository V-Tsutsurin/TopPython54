from car import carclass

class ElectroCar(carclass.CarClass):
    def __init__(self, brand, model, year, probeg):
        super().__init__(brand, model, year, probeg)
        self.battery = 100

    def description_battery(self):
        print(f"Батарея автомобиля имеет целостность {self.battery}")



if __name__ == "__main__":
    print("1")
    print("1")
    print("1")
    print("1")
    print("1")
    print("1")
    print("1")
    print("1")
    print("1")
    e_car = ElectroCar("Toyota", "camry", 2022, 15000)
    e_car.show_car()
    e_car.description_battery()