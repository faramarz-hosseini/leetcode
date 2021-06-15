class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.slots = [big, medium, small]

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        carType = carType - 1
        if self.slots[carType] - 1 >= 0:
            self.slots[carType] = self.slots[carType] - 1
            return True
        else:
            return False