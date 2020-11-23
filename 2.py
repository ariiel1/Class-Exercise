import math
class Circle:
    
    def __init__(self,radius=1.0,color="red"):
        self.__radius = radius
        self.__color = color

    def getRadius(self):
        return self.__radius
    
    def setRadius(self):
        self.__radius = radius

    def getColor(self):
        return self.__color

    def setColor(self):
        self.__color = color

    def toString(self):
        return (f"Radius: {self.__radius}, Color: {self.__color}")

    def getArea(self):
        return (2**self.__radius) * math.pi

class Cylinder(Circle):
    def __init__(self, height=1.0,radius=1.0,color="red"):
        self.__height = height
        super().__init__(radius,color)

    def getHeight(self):
        return self.__height
    
    def setHeight(self):
        self.__height = height

    def toString(self):
        return (f"Height: {self.__height}, Radius: {self.__radius}, Color: {self.__color}")

    def getVolume(self):
        return self.getArea * self.__height