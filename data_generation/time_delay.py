import numpy as np
import random


class Delay:

    def __init__(self, x, fs):
        self.x = x
        self.fs = fs

        self.shift = random.randint(0, int(self.fs * 0.08))

    def delay(self):
        y = np.roll(self.x, self.shift)
        y[0:self.shift] = np.zeros((self.shift, 1))
        return y
