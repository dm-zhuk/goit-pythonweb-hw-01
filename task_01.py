#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import Optional
import logging

# створюємо логер, даємо йому ім'я та встановлюємо рівень INFO
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

# Створюємо файловий handler для логера, рівень ERROR:
fh = logging.FileHandler("app.log")
fh.setLevel(logging.ERROR)
fh.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(fh)


class Vehicle(ABC):
    def __init__(self, make: str, model: str):
        self.make: str = make
        self.model: str = model
        self.reg_spec: Optional[RegionalSpec] = None

    @abstractmethod
    def start_engine(self) -> None:
        raise NotImplementedError


class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Мотор заведено")


class RegionalSpec:
    def __init__(self, region: str, speed_unit: str):
        self.region: str = region
        self.speed_unit: str = speed_unit

    def __str__(self) -> str:
        return f"{self.region}, Speed: {self.speed_unit}"


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        raise NotImplementedError

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        raise NotImplementedError


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        car = Car(make, model)
        car.reg_spec = RegionalSpec("US Spec", "mph")
        return car

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        bike = Motorcycle(make, model)
        bike.reg_spec = RegionalSpec("US Spec", "mph")
        return bike


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        car = Car(make, model)
        car.reg_spec = RegionalSpec("EU Spec", "km/h")
        return car

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        bike = Motorcycle(make, model)
        bike.reg_spec = RegionalSpec("EU Spec", "km/h")
        return bike


# Використання
def main():
    # Створення американських автомобілів та мотоциклів
    us_make = USVehicleFactory()
    us_car = us_make.create_car("Toyota", "Corolla")
    us_bike = us_make.create_motorcycle("Harley-Davidson", "Sportster")

    us_car.start_engine()
    logger.info(f"{us_car.make} {us_car.model}: {us_car.reg_spec}")
    us_bike.start_engine()
    logger.info(f"{us_bike.make} {us_bike.model}: {us_bike.reg_spec}")

    # Створення європейських автомобілів та мотоциклів
    eu_make = EUVehicleFactory()
    eu_car = eu_make.create_car("Volkswagen", "Golf")
    eu_bike = eu_make.create_motorcycle("BMW", "R1250GS")

    eu_car.start_engine()
    logger.info(f"{eu_car.make} {eu_car.model}: {eu_car.reg_spec}")
    eu_bike.start_engine()
    logger.info(f"{eu_bike.make} {eu_bike.model}: {eu_bike.reg_spec}")


if __name__ == "__main__":
    main()
