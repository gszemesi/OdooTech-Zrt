from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, type,ajtok_szama, marka):
        super(Car, self).__init__(type, marka)
        self.__ajtok_szama = ajtok_szama

    def getAjtok_szama(self):
        return self.__ajtok_szama