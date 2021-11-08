from extender import *


def read_str_array(container, strArray):
    array_len = len(strArray)
    i = 0   # Индекс, задающий текущую строку в массиве
    figNum = 0
    while i < array_len:
        str = strArray[i]
        key = int(str)   # преобразование в целое
        if key == 1: # признак прямоугольника
            i += 1
            movie = Game()
            i = movie.read_str_array(strArray, i) # чтение прямоугольника с возвратом позиции за ним
        elif key == 2: # признак треугольника
            i += 1
            movie = Cartoon()
            i = movie.read_str_array(strArray, i) # чтение треугольника с возвратом позиции за ним
        elif key == 3:
            i += 1
            movie = Documentary()
            i = movie.read_str_array(strArray, i)  # чтение треугольника с возвратом позиции за ним
        else:
            # что-то пошло не так. Должен быть известный признак
            # Возврат количества прочитанных фигур
            return figNum
        # Количество пробелами фигур увеличивается на 1
        if i == 0:
            return figNum
        figNum += 1
        container.store.append(movie)
    return figNum
