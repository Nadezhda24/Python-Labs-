import math

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def isint(value):
    try:
        return int(value) == float(value)
    except ValueError:
        return False


while True:
    try:
        k = int(input("==========================\n"
                      "1. Вычисление математического выражения.\n"
                      "2. Работа со списком элементов разных типов.\n"
                      "3. Вычисление площади фигур.\n"
                      "Для выхода введите 0.\n"
                      "Введите номер задания: "))
    except:
        print("Ошибка, введен не верный номер задания. Попробуйте снова.")
        continue
    break

while k != 0:
    if k == 1:
        while True:
            try:
                x, n =map(int, input("--------------------------\n"
                                     "Задание №1.\nВведите x и n: ").split())
            except:
                print("Ошибка, введено не целое число. Попробуйте снова.")
                continue
            break
        print("Ответ: ", (math.sqrt(abs(math.cos(x))**n + (math.exp(n ** 3))/(math.log(x)) + abs(math.sin(x)) ** (1/n))))
    elif k == 2:
        while True:
            try:
                k2 = int(input("--------------------------\n"
                               "Задание №2.\n"
                               "1. Показать значения списка на экране.\n"
                               "2. Добавить новый элемент в конец списка.\n"
                               "3. Удалить указанный элемент.\n"
                               "4. Сформировать кортеж, состоящий из вещественных положительных элементов списка.\n Вывести содержимое кортежа на экран.\n"
                               "5. Найти произведение всех целочисленных элементов списка.\n"
                               "6. Сформировать  строку  из  значений  элементов  списка.\n  Посчитать  сколько  раз встречается в строке указанное пользователем слово.\n"
                               "7. Задать с клавиатуры множество M1, сформировать множество M2 из списка.\n Вывести на экран симметричную разницумножеств M1 и M2.\n"
                               "8. Получить  из  списка  словарь,  ключом  каждого  элемента  сделать  позицию  элемента  в словаре.\n  Построчно  отобразить  на  экране  элементы  словаря  с  нечетными  значениями ключа.\n"                             
                               "Для выхода введите 0.\n"
                               "Введите номер подзадания:"))
            except:
                print("Ошибка, введен не верный номер задания. Попробуйте снова.")
                continue
            break
        a = [1,-2.78,3, "dscdc", 5, 3.5, 5.0, 1, "dscdc"]
        while k2 != 0:
            if k2 == 1:
                print(a)
            elif k2 == 2:
                t = (input("Введите тип: "))
                if (t == "str"):
                    while True:
                        try:
                            x = (input("Ввведите значение: "))
                        except:
                            print("Ошибка. Попробуйте снова.")
                            continue
                        break
                    a.append(x)
                elif (t == "int"):
                    while True:
                        try:
                            x = int(input("Ввведите значение: "))
                        except:
                            print("Ошибка, введено не целое число. Попробуйте снова.")
                            continue
                        break
                    a.append(x)
                elif (t == "float"):
                    while True:
                        try:
                            x = float(input("Ввведите значение: "))
                        except:
                            print("Ошибка, введено значение не типа float. Попробуйте снова.")
                            continue
                        break
                    a.append(x)
            elif k2 == 3:
                print("1. Удалить по номеру в списке.\n"
                      "2. Удалить по значению.")
                while True:
                    try:
                        k4 = int(input("Выберете способ удаления: "))
                    except:
                        print("Ошибка, введен не верный способ удаления. Попробуйте снова.")
                        continue
                    break
                if k4 == 1:
                    while True:
                        try:
                            x = int(input("Ввведите номер: "))
                        except:
                            print("Ошибка, введено не целое число. Попробуйте снова.")
                            continue
                        break
                    try:
                        a.pop(x)
                    except:
                        print("Ошибка, элемента с данным номером не существует.")
                elif k4 == 2:
                    while True:

                        try:
                            x = int(input("Ввведите значение: "))
                        except:
                            print("Ошибка, введено не целое число. Попробуйте снова.")
                            continue
                        break
                    try:
                        a.remove(x)
                    except:
                        print("Ошибка, элемента с данным значением не существует.")
                else: print("Ошибка, введен не верный способ удаления. Попробуйте снова.")
            elif k2 == 4:
                b = []
                for i in a:
                   if isinstance(i,float):
                       if float(i) > 0:
                             b.append(float(i))
                print("Кортеж: ")
                print(tuple(b))
            elif k2 == 5:
                p = int(1)
                for i in a:
                    if isinstance(i,int):
                       p = int(p) * i
                print("Произведение: " + str(p))
            elif k2 == 6:
                s = str("")
                for i in range(len(a)):
                    s = str(s) + " " + str(a[i])
                s2 = str(input("Введите строку для поиска: "))
                print("Введенное слово встретилось: " +str(s.count(s2)))
            elif k2 == 7:
                b = {i for i in range(10)}
                print(set(a))
                print(b)
                # множество, состоящее только из уникальных элементов исходных множеств
                print("Симметричная разница: ")
                print(set(a)^b)
            elif k2 == 8:
                d = { }
                for i in range(len(a)):
                    d[i] = a[i]
                print("Словарь: ")
                print(d)
                for i in range(len(a)):
                   if i%2 != 0:
                       print("Элемент " + str(i) + ": " +str(d[i]))
            else:
                print("Ошибка, введен не верный номер задания. Попробуйте снова.")
            while True:
                try:
                    k2 = int(input("--------------------------\n"
                               "Задание №2.\n"
                               "1. Показать значения списка на экране.\n"
                               "2. Добавить новый элемент в конец списка.\n"
                               "3. Удалить указанный элемент.\n"
                               "4. Сформировать кортеж, состоящий из вещественных положительных элементов списка.\n Вывести содержимое кортежа на экран.\n"
                               "5. Найти произведение всех целочисленных элементов списка.\n"
                               "6. Сформировать  строку  из  значений  элементов  списка.\n  Посчитать  сколько  раз встречается в строке указанное пользователем слово.\n"
                               "7. Задать с клавиатуры множество M1, сформировать множество M2 из списка.\n Вывести на экран симметричную разницумножеств M1 и M2.\n"
                               "8. Получить  из  списка  словарь,  ключом  каждого  элемента  сделать  позицию  элемента  в словаре.\n  Построчно  отобразить  на  экране  элементы  словаря  с  нечетными  значениями ключа.\n"                             
                               "Для выхода введите 0.\n"
                               "Введите номер подзадания: "))
                except:
                    print("Ошибка, введен не верный номер задания. Попробуйте снова.")
                    continue
                break
    elif k == 3:
        while True:
            try:
                k3 = str(input("--------------------------\n"
                                   "Задание №3.\n"
                                   "S. Площадь квадрата.\n"
                                   "T. Площадь трапеции.\n"
                                   "P. Площадь параллелограмма.\n"
                                   "Для выхода введите E.\nВведите номер подзадания: "))
            except:
                print("Ошибка, введен не верный номер задания. Попробуйте снова.")
                continue
            break
        while (k3 != "E"):
            if k3 == "S":
                while True:
                    try:
                        x = int(input("Ввведите значение стороны квадрата: "))
                    except:
                        print("Ошибка, введен не верный способ удаления. Попробуйте снова.")
                        continue
                    break
                print("Площадь квадрата: " + str(x*x))
            elif k3 == "T":
                while True:
                    try:
                        x = int(input("Ввведите значение верхнего основания трапеции: "))
                    except:
                        print("Ошибка, введен не верный способ удаления. Попробуйте снова.")
                        continue
                    break
                while True:
                    try:
                        y = int(input("Ввведите значение нижнего основания трапеции: "))
                    except:
                        print("Ошибка, введен не верный способ удаления. Попробуйте снова.")
                        continue
                    break
                while True:
                    try:
                        h = int(input("Ввведите значение высоты трапеции: "))
                    except:
                        print("Ошибка, введен не верный способ удаления. Попробуйте снова.")
                        continue
                    break
                print("Площадь трапеции: " + str(0.5 * h * (x+y)))
            elif k3 == "P":
                while True:
                    try:
                        y = int(input("Ввведите значение основания параллелограмма: "))
                    except:
                        print("Ошибка, введен не верный способ удаления. Попробуйте снова.")
                        continue
                    break
                while True:
                    try:
                        h = int(input("Ввведите значение высоты параллелограмма: "))
                    except:
                        print("Ошибка, введен не верный способ удаления. Попробуйте снова.")
                        continue
                    break
                print("Площадь параллелограмма: " + str(h * y))
            else:
                print("Ошибка, введен не верный номер задания. Попробуйте снова.")
            while True:
                try:
                    k3 = str(input("--------------------------\n"
                                   "Задание №3.\n"
                                   "S. Площадь квадрата.\n"
                                   "T. Площадь трапеции.\n"
                                   "P. Площадь параллелограмма.\n"
                                   "Для выхода введите E.\nВведите номер подзадания: "))
                except:
                    print("Ошибка, введен не верный номер задания. Попробуйте снова.")
                    continue
                break
    else: print("Ошибка, введен не верный номер задания. Попробуйте снова.")

    while True:
        try:
            k = int(input("==========================\n"
                          "1. Вычисление математического выражения.\n"
                          "2. Работа со списком элементов разных типов.\n"
                          "3. Вычисление площади фигур.\n"
                          "Для выхода введите 0.\n"
                          "Введите номер задания: "))
        except:
            print("Ошибка, введен не верный номер задания. Попробуйте снова.")
            continue
        break