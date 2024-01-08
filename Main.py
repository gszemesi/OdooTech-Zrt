# Szemesi Gábor
# gszemesi@gmail.com

import os
import json

from vehicle import Bike
from vehicle import Car


def readAndCreate(dir_path, vehicles):
    for entry in getFiles(dir_path):
        file = open(entry)
        jsonData = json.load(file)
        print(entry.name + " fájl megnyitása és beolvasása.")

        if jsonData['type'] == "bicikli":
            bike = Bike(jsonData['type'], jsonData['terhelhetoseg'], jsonData['marka'])
            vehicles.append(bike)
            print("Bike objekt létrehozása.")
        elif jsonData['type'] == "auto":
            car = Car(jsonData['type'], jsonData['ajtok_szama'], jsonData['marka'])
            vehicles.append(car)
            print("Car objekt létrehozása.")
        else:
            raise Exception("Error! Not find or exists " + jsonData["type"] + " constructor!")


def listVehicle(vehicles):
    print("\nList vehicles:")
    for vehicle in vehicles:
        if type(vehicle).__name__ == "Bike":
            print("Jármű típusa:", vehicle.getType(), ", terhelhetőség:", vehicle.getTerhelhetoseg(), ", márka:",
                  vehicle.getMarka())
        elif type(vehicle).__name__ == "Car":
            print("Jármű típusa:", vehicle.getType(), ", ajtók száma:", vehicle.getAjtok_szama(), ", márka:",
                  vehicle.getMarka())
        else:
            raise Exception("Error! Unknown vehicle! " + vehicle["type"])


def getFiles(base_dir):
    for entry in os.scandir(base_dir):
        if entry.is_file():
            yield entry
        elif entry.is_dir():
            yield from getFiles(entry.path)


if __name__ == "__main__":
    vehicles = []
    readAndCreate("data", vehicles)
    listVehicle(vehicles)
