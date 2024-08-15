import numpy as np

class Augmentor:
    def __init__(self, noise_level=0.01, speed_change_range=(0.7, 1.3), volume_change_range=(0.5, 1.5)):
        self.noise_level = noise_level
        self.speed_change_range = speed_change_range
        self.volume_change_range = volume_change_range

    def add_noise(self, audio):
        noise = np.random.normal(0, self.noise_level, audio.shape)
        return audio + noise

    def change_speed(self, audio):
        speed_factor = np.random.uniform(*self.speed_change_range)
        if len(audio.shape) == 1: # mono
            new_length = int(audio.shape[0] / speed_factor)
            return np.interp(np.linspace(0, audio.shape[0], new_length), np.arange(audio.shape[0]), audio)
        else: # stereo
            new_length = int(audio.shape[1] / speed_factor)
            return np.interp(np.linspace(0, audio.shape[1], new_length), np.arange(audio.shape[1]), audio)

    def change_volume(self, audio):
        volume_factor = np.random.uniform(*self.volume_change_range)
        return audio * volume_factor

    def augment(self, audio):
        audio = self.add_noise(audio)
        audio = self.change_speed(audio)
        audio = self.change_volume(audio)
        return audio