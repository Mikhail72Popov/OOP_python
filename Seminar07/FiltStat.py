

from Statcomp import statcompList


class FiltStat():
    def filter2():
        print (" 1 - Модель\n 2 - ОЗУ\n 3 - Объем ЖД\n 4 - Операционная система\n 5 - Размер")
        n = int(input('Введите цифру, соответствующую необходимому критерию: '))
        if n == 1:
            sc1 = input("Введите производителя ноутбука: ")
            print(sc1)
            prodClass = [statcomp for statcomp in statcompList if statcomp._product == sc1]
            for statcomp in prodClass:
                print(statcomp._product+'--'+str(statcomp._randomMemory)+'--'+str(statcomp._hardDisk)+
                '--'+statcomp._operSystem+'--'+str(statcomp._size))


        elif n == 2:
            sc2 = int(input("Введите минимальный объём ОЗУ: "))
            memClass = [statcomp for statcomp in statcompList if statcomp._randomMemory >= sc2]
            for statcomp in memClass:
                print(statcomp._product+'--'+str(statcomp._randomMemory)+'--'+str(statcomp._hardDisk)+
                '--'+statcomp._operSystem+'--'+str(statcomp._size))


        elif n == 3:
            sc3 = int(input("Введите минимальный объём жёсткого диска: "))
            diskClass = [statcomp for statcomp in statcompList if statcomp._hardDisk >= sc3]
            for statcomp in diskClass:
                print(statcomp._product+'--'+str(statcomp._randomMemory)+'--'+str(statcomp._hardDisk)+
                '--'+statcomp._operSystem+'--'+str(statcomp._size))

        elif n == 4:
            sc4 = str(input("Введите требуемую ос: "))
            systemClass = [statcomp for statcomp in statcompList if statcomp._operSystem == sc4]
            for statcomp in systemClass:
                print(statcomp._product+'--'+str(statcomp._randomMemory)+'--'+str(statcomp._hardDisk)+
                '--'+statcomp._operSystem+'--'+str(statcomp._size))

        elif n == 5:
            sc5 = int(input("Введите размер: "))
            sizeClass = [statcomp for statcomp in statcompList if statcomp._size == sc5]
            for statcomp in sizeClass:
                print(statcomp._product+'--'+str(statcomp._randomMemory)+'--'+str(statcomp._hardDisk)+
                '--'+statcomp._operSystem+'--'+str(statcomp._size))

        else:
            print("Не соответствует необходимому критерию")

