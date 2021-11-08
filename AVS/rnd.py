import random
import string


class Random:

    def generate_random_int(self, minim, maxim):
        return random.randint(minim, maxim)

    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(length))
        return rand_string
