from scipy.signal import fftconvolve
import random
import librosa
import os


class Reverberator:

    def __init__(self, x, fs):
        self.x = x
        self.fs = fs

        irs_dir = "/media/yurii/ToshibaLaptopHDD/datasets/rirs/RIRS_NOISES/rirs_train"
        irs_path = [os.path.join(irs_dir, ir) for ir in os.listdir(irs_dir)]
        target_ir_path = random.choice(irs_path, 1)
        self.ir, _ = librosa.core.load(target_ir_path, sr=self.fs, mono=True)

    def fft_conv(self):
        y = fftconvolve(self.x, self.ir, mode='same')
        return y
