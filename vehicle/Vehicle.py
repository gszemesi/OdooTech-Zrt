from abc import ABCMeta, abstractmethod


class Vehicle(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, type, marka):
        self.__type = type
        self.__marka = marka

    def getType(self):
        return self.__type

    def getMarka(self):
        return self.__marka
