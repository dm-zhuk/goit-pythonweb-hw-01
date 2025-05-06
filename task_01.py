"""
Наступним кроком потрібно створювати транспортні засоби з урахуванням специфікацій різних регіонів наприклад, для США US Spec та ЄС EU Spec.
Ваше завдання — реалізувати патерн фабрика, який дозволить створювати транспортні засоби з різними регіональними специфікаціями, не змінюючи основні класи транспортних засобів.
Ход виконання завдання 1:
Створити абстрактний базовий клас Vehicle з методом start_engine().
Змінити класи Car та Motorcycle, щоб вони успадковувались від Vehicle.
Створити абстрактний клас VehicleFactory з методами create_car() та create_motorcycle().
Реалізувати два класи фабрики: USVehicleFactory та EUVehicleFactory. Ці фабрики повинні створювати автомобілі та мотоцикли з позначкою регіону наприклад, Ford Mustang (US Spec) відповідно для США.
Змініть початковий код так, щоб він використовував фабрики для створення транспортних засобів.
Очікуваний результат: Код, що дозволяє легко створювати транспортні засоби для різних регіонів, використовуючи відповідні фабрики.
"""


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Мотор заведено")


# Використання
vehicle1 = Car("Toyota", "Corolla")
vehicle1.start_engine()

vehicle2 = Motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()
