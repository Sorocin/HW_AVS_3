from extender import *

class Game:
    def __init__(self):
        self.name = ""
        self.year = 0
        self.producer = ""

    def read_str_array(self, strArray, i):
        # должно быт как минимум три непрочитанных значения в массиве
        if i >= len(strArray) - 2:
            return 0
        self.name = str(strArray[i])
        self.year = int(strArray[i + 1])
        self.producer = str(strArray[i + 2])
        i += 3
        return i

    def print(self):
        print("Game: name = ", self.name, "year = ", self.year, "producer = ", self.producer,
              "task = ", self.task())

    def write(self, ostream):
        ostream.write("Game: name = {}  year = {}  producer = {}, Perimeter = {}".
                      format(self.name, self.year, self.producer, self.task()))

    def random_print(self):
        r = Random()
        self.name = r.generate_random_string(10)
        self.year = r.generate_random_int(1900, 2022)
        self.producer = r.generate_random_string(10)
        print("Documentary: name = ", self.name, "year = ", self.year, "duration = ", self.producer,
              "task = ", self.task())

    def random_write(self, ostream):
        ostream.write("Game: name = {}  year = {}  producer = {}, Perimeter = {}".
                      format(self.name, self.year, self.producer, self.task()))



    def task(self):
        ans = 0.0
        ans = self.year / len(self.name)
        return ans
