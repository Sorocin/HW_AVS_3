from extender import *


def read_str_array(container, strArray):
    array_len = len(strArray)
    i = 0
    figNum = 0
    while i < array_len:
        str = strArray[i]
        key = int(str)
        if key == 1:
            i += 1
            movie = Game()
            i = movie.read_str_array(strArray, i)
        elif key == 2:
            i += 1
            movie = Cartoon()
            i = movie.read_str_array(strArray, i)
        elif key == 3:
            i += 1
            movie = Documentary()
            i = movie.read_str_array(strArray, i)
        else:
            return figNum
        if i == 0:
            return figNum
        figNum += 1
        container.store.append(movie)
    return figNum
