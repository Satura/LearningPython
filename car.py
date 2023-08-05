class Car:
#  Класс описывающий автомобиль

    def __init__(self, model, year, volume, mileage):
        # Инициализация авто
        self.model = model
        self.year = year
        self.volume = volume
        self.mileage = mileage
        self.wheel_count = 4

    def description(self):
        # Вывод описания авто 
        print(f'Это чудо отчественного автопрома зовут {self.model}, год выпуска {self.year}, '
              f'объём двигателя {self.volume}, успела наездить {self.mileage} км.')


first_car = Car('Lada 2109', 1988, 1.3, 150000)
first_car.description()


class Truck(Car):

    def __init__(self, model, year, volume, mileage):
        super().__init__(model, year, volume, mileage)
        self.wheel_count = 8

    def description(self):
        print(f'Это представитель рода грузовиков. Его зовут {self.model}, год выпуска {self.year}, '
              f'объём двигателя {self.volume}, проклесил  {self.mileage} км. \n'
              f'Колес у него кстати {self.wheel_count} шт.')


first_truck = Truck('КамАЗ-6560', 2022, 11.8, 78000)
first_truck.description()
