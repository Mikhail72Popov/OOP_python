
from Warehouse import Warehouse

class Statcomp(Warehouse):
    def __init__(self, product, randomMemory, hardDisk, operSystem, size):
        super(). __init__(product, randomMemory, hardDisk, operSystem)
        self._size = size

statcompList = [Statcomp("Lenovo", 8, 650, "Windows", 25),
                Statcomp("HP", 16, 550, "Windows", 30),
                Statcomp("Asus", 8, 450, "Linux", 12),
                Statcomp("Apple", 16, 750, "MAC", 10),
                Statcomp("HP", 8, 650, "Windows", 26),
                Statcomp("Lenovo", 8, 650, "Windows", 31)]

