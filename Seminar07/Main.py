
#       Необходимо реализовать свой проект на каком-то другом языке программирования   
#  ДЗ семинара 2 ООП-java => python
# • Подумать над структурой класса Ноутбук для магазина техники - выделить поля и методы.
# • Создать множество ноутбуков.
# • Написать метод, который будет запрашивать у пользователя критерий (или критерии) фильтрации и
# выведет ноутбуки, отвечающие фильтру.


from FiltStat import FiltStat
from FiltLapt import FiltLapt

class Main():
        def choice1():
            print (" 1 - Ноутбук\n 2 - Стационарный компьютер")
            z = int(input('Введите цифру, соответствующую необходимому критерию: '))
            if z == 1 or z == 2:
                Main.choice2(z)
            else:
                print("Не соответствует необходимому критерию")

        def choice2(z):
            if z == 1:
                FiltLapt.filter1()
            else:
                FiltStat.filter2()

           
Main.choice1()

    


