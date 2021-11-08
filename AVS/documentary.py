from extender import *
from rnd import Random


class Documentary:
    def __init__(self):
        self.name = ""
        self.year = 0
        self.duration = 0

    def read_str_array(self, strArray, i):
        # должно быт как минимум три непрочитанных значения в массиве
        if i >= len(strArray) - 2:
            return 0
        self.name = str(strArray[i])
        self.year = int(strArray[i+1])
        self.duration = int(strArray[i+2])
        i += 3
        return i

    def print(self):
        print("Documentary: name = ", self.name, "year = ", self.year, "duration = ", self.duration,
              "task = ", self.task())

    def write(self, ostream):
        ostream.write("Documentary: name = {}  year = {}  duration = {}, task = {}".
                      format(self.name, self.year, self.duration, self.task()))

    def random_print(self):
        r = Random()
        self.name = r.generate_random_string(10)
        self.year = r.generate_random_int(1900, 2022)
        self.duration = r.generate_random_int(30, 300)
        print("Documentary: name = ", self.name, "year = ", self.year, "duration = ", self.duration,
              "task = ", self.task())

    def random_write(self, ostream):
        ostream.write("Documentary: name = {}  year = {}  duration = {}, task = {}".
                      format(self.name, self.year, self.duration, self.task()))

    def task(self):
        ans = 0.0
        ans = self.year / len(self.name)
        return ans
