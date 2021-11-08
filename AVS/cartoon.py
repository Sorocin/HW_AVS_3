from enum import Enum
from extender import *
from rnd import Random


class Cartoon:
    def __init__(self):
        self.name = ""
        self.year = 0
        self.type = Enum("type", "Draw Puppet Plasticine", start=1)

    def read_str_array(self, strArray, i):
        # должно быт как минимум три непрочитанных значения в массиве
        if i >= len(strArray) - 2:
            return 0
        self.name = str(strArray[i])
        self.year = int(strArray[i+1])
        self.type = (strArray[i+2])
        i += 3
        return i

    def print(self):
        if self.type == 1 or self.type == "Draw":
            self.type = "Draw"
        elif self.type == 2 or self.type == "Puppet":
            self.type = "Puppet"
        else:
            self.type = "Plasticine"
        print("Cartoon: name = ", self.name, "year = ", self.year, "type = ", self.type,
              "task = ", self.task())

    def write(self, ostream):
        ostream.write("Cartoon: name = {}  year = {}  type = {}, task = {}".
                      format(self.name, self.year, self.type, self.task()))

    def random_print(self, digit):
        r = Random()
        if digit == 1:
            self.type = "Draw"
        elif digit == 2:
            self.type = "Puppet"
        else:
            self.type = "Plasticine"
        self.name = r.generate_random_string(10)
        self.year = r.generate_random_int(1900, 2022)
        print("Cartoon: name = ", self.name, "year = ", self.year, "type = ", self.type,
              "task = ", self.task())

    def random_write(self, ostream):
        ostream.write("Cartoon: name = {}  year = {}  type = {}, task = {}".
                      format(self.name, self.year, self.type, self.task()))

    def task(self):
        ans = 0.0
        ans = self.year / len(self.name)
        return ans
