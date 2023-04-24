

from Laptop import laptopList


class FiltLapt():
    def filter1():
        print (" 1 - Модель\n 2 - ОЗУ\n 3 - Объем ЖД\n 4 - Операционная система\n 5 - Цвет")
        n = int(input('Введите цифру, соответствующую необходимому критерию: '))
        if n == 1:
            sc1 = input("Введите производителя ноутбука: ")
            print(sc1)
            prodClass = [laptop for laptop in laptopList if laptop._product == sc1]
            for laptop in prodClass:
                print(laptop._product+'--'+str(laptop._randomMemory)+'--'+str(laptop._hardDisk)+
                '--'+laptop._operSystem+'--'+laptop._color)


        elif n == 2:
            sc2 = int(input("Введите минимальный объём ОЗУ: "))
            memClass = [laptop for laptop in laptopList if laptop._randomMemory >= sc2]
            for laptop in memClass:
                print(laptop._product+'--'+str(laptop._randomMemory)+'--'+str(laptop._hardDisk)+
                '--'+laptop._operSystem+'--'+laptop._color)


        elif n == 3:
            sc3 = int(input("Введите минимальный объём жёсткого диска: "))
            diskClass = [laptop for laptop in laptopList if laptop._hardDisk >= sc3]
            for laptop in diskClass:
                print(laptop._product+'--'+str(laptop._randomMemory)+'--'+str(laptop._hardDisk)+
                '--'+laptop._operSystem+'--'+laptop._color)

        
        elif n == 4:
            sc4 = str(input("Введите требуемую ос: "))
            systemClass = [laptop for laptop in laptopList if laptop._operSystem == sc4]
            for laptop in systemClass:
                print(laptop._product+'--'+str(laptop._randomMemory)+'--'+str(laptop._hardDisk)+
                '--'+laptop._operSystem+'--'+laptop._color)

        
        elif n == 5:
            sc5 = str(input("Введите цвет: "))
            systemClass = [laptop for laptop in laptopList if laptop._color == sc5]
            for laptop in systemClass:
                print(laptop._product+'--'+str(laptop._randomMemory)+'--'+str(laptop._hardDisk)+
                '--'+laptop._operSystem+'--'+laptop._color)

        else:
            print("Не соответствует необходимому критерию")


