
from Warehouse import Warehouse

class Laptop(Warehouse):
    def __init__(self, product, randomMemory, hardDisk, operSystem, color):
        super().__init__(product, randomMemory, hardDisk, operSystem)
        self._color = color

laptopList = [Laptop("Lenovo", 8, 650, "Windows", "red"),
              Laptop("HP", 16, 550, "Windows", "black"),
              Laptop("Asus", 8, 450, "Linux","silver"),
              Laptop("Apple", 16, 750, "MAC", "purple"),
              Laptop("HP", 8, 650, "Windows", "white"),
              Laptop("Lenovo", 8, 650, "Windows", "brown")]
