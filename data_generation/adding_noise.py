import numpy as np
import random
import librosa
import os


class NoiseAdder:

    def __init__(self, x, fs):
        self.x = x
        self.fs = fs

        noises_dir = "/media/yurii/ToshibaLaptopHDD/datasets/qut-noise-timit"
        target_formats = (".wav", ".flac", ".mp3")
        noises_path = []
        for root, dirs, files in os.walk(noises_dir):
            for f in files:
                if any([f.endswith(t_format) for t_format in target_formats]):
                    noises_path.append(os.path.join(root, f))

        self.noise = np.ndarray([0])
        while self.noise.shape[0] < self.x.shape[0]:
            target_ir_path = random.choice(noises_path, 1)
            self.noise, _ = librosa.core.load(target_ir_path, sr=self.fs, mono=True)

    def add_noise(self):
        amp_coef = random.uniform(0.01, 1)
        noise_start = random.randint(0, self.noise.shape[0] - self.x.shape[0] - 1)
        noise = self.noise[noise_start:self.x.shape[0]]
        y = np.add(self.x, noise * amp_coef)
        return y
