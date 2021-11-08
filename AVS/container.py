import documentary
import game
from extender import *


class Container:
    __length = 0

    def __init__(self):
        self.store = []

    def print(self):
        print("Container is store", len(self.store), "movies:")
        for movie in self.store:
            movie.print()
            self.__length = self.__length + 1
        print("Shell Sorting  = ", )

    def write(self, ostream):
        ostream.write("Container is store {} movies:\n".format(len(self.store)))
        for movie in self.store:
            movie.write(ostream)
            ostream.write("\n")
        self.shell()

    def shell_print(self):
        for movie in self.store:
            movie.print()

    def shell_write(self, ostream):
        ostream.write("Sorted {} movies:\n".format(len(self.store)))
        for movie in self.store:
            movie.write(ostream)
            ostream.write("\n")

    def random_print(self, count):
        for i in range(int(count)):
            digit = random.randint(1, 3)
            typeof = random.randint(1, 3)
            if digit == 1:
                game = Game()
                game.random_print()
                self.store.append(game)
            elif digit == 2:
                cartoon = Cartoon()
                cartoon.random_print(typeof)
                self.store.append(cartoon)
            elif digit == 3:
                documentary = Documentary()
                documentary.random_print()
                self.store.append(documentary)
            self.__length = self.__length + 1

    def random_write(self, ostream):
        ostream.write("Container is store {} movies:\n".format(len(self.store)))
        for movie in self.store:
            movie.random_write(ostream)
            ostream.write("\n")
        self.shell()

    def shell_random_print(self):
        print("\n")
        print("\n")
        for movie in self.store:
            movie.random_print()

    def shell_random_write(self, ostream):
        ostream.write("Sorted {} movies:\n".format(len(self.store)))
        for movie in self.store:
            movie.write(ostream)
            ostream.write("\n")

    def shell(self):
        for s in range(self.__length // 2, 0, -1):
            for i in range(0, self.__length):
                for j in range(i + s, self.__length):
                    first = self.store[i].year / len(self.store[i].name)
                    second = self.store[j].year / len(self.store[j].name)
                    if first > second:
                        temp = self.store[j]
                        self.store[j] = self.store[i]
                        self.store[i] = temp
                    j += s - 1
            s //= 2 + 1