from vehicle import Vehicle


class Bike(Vehicle):
    def __init__(self, type, terhelhetoseg, marka):
        super(Bike, self).__init__(type,marka)
        self.__terhelhetoseg = terhelhetoseg

    def getTerhelhetoseg(self):
        return self.__terhelhetoseg
