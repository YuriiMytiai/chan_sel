from scipy.signal import butter, lfilter
import random


class Filter:

    def __init__(self, x, fs):
        self.x = x
        self.fs = fs
        self.nyq = 0.5 * self.fs

        self.filter_types = ("LP", "HP", "BP", "BS")
        self.filter_orders = (3, 4, 5, 6)

        self.f_type = random.choice(self.filter_types, 1)
        self.f_order = random.choice(self.filter_orders, 1)

    def butter_lowpass(self):
        normal_cutoff = random.uniform(0.3, 0.99)
        b, a = butter(self.f_order, normal_cutoff, btype='lowpass', analog=False, output='ba')
        return b, a

    def butter_highpass(self):
        normal_cutoff = random.uniform(0, 0.7)
        b, a = butter(self.f_order, normal_cutoff, btype='highpass', analog=False, output='ba')
        return b, a

    def butter_bandstop(self):
        r1 = random.uniform(0, 0.8)
        r2 = random.uniform(0.1, 0.9)
        low = min(r1, r2)
        high = max(r1, r2)
        b, a = butter(self.f_order, [low, high], btype='bandstop', output='ba')
        return b, a

    def butter_bandpass(self):
        r1 = random.uniform(0, 0.8)
        r2 = random.uniform(0.1, 0.99)
        low = min(r1, r2)
        high = max(r1, r2)
        b, a = butter(self.f_order, [low, high], btype='bandpass', output='ba')
        return b, a

    def butter_filter(self):
        if self.f_type == "LP":
            b, a = self.butter_lowpass()
        elif self.f_type == "HP":
            b, a = self.butter_highpass()
        elif self.f_type == "BP":
            b, a = self.butter_bandpass()
        elif self.f_type == "BS":
            b, a = self.butter_bandstop()

        y = lfilter(b, a, self.x)
        return y
