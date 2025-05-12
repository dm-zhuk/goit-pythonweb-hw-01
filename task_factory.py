#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from logger import apply_logging

logger = apply_logging("Factory")


class Vehicle(ABC):
    """Abstract base class for all vehicles"""

    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self) -> None:
        """Abstract method to start any engine"""
        pass


class Car(Vehicle):
    def __init__(self, make: str, model: str, spec: str = ""):
        super().__init__(make, model)
        self.spec = spec

    def start_engine(self) -> None:
        log_message = f"{self.make} {self.model}"
        if self.spec:
            log_message += f" ({self.spec})"
        log_message += ": Двигун запущено"
        logger.info(log_message)


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, spec: str = ""):
        super().__init__(make, model)
        self.spec = spec

    def start_engine(self) -> None:
        log_message = f"{self.make} {self.model}"
        if self.spec:
            log_message += f" ({self.spec})"
        log_message += ": Мотор заведено"
        logger.info(log_message)


class VehicleFactory(ABC):
    """Abstract base class for all factories"""

    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    """US-spec vehicles factory"""

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    """EU-spec vehicles factory"""

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU Spec")


us_make = USVehicleFactory()
eu_make = EUVehicleFactory()

vehicle1 = eu_make.create_car("Toyota", "Corolla")
vehicle2 = us_make.create_car("Ford", "Mustang")
vehicle3 = eu_make.create_motorcycle("BMW", "R1250GS")
vehicle4 = us_make.create_motorcycle("Harley-Davidson", "Sportster")

vehicle1.start_engine()
vehicle2.start_engine()
vehicle3.start_engine()
vehicle4.start_engine()
