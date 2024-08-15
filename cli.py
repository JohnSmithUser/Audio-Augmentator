import argparse
import soundfile as sf
from augmentor import Augmentor

def read_audio(file_path):
    audio, samplerate = sf.read(file_path)
    return audio.T, samplerate  # Транспонировать в (num_channels, num_samples)

def save_audio(file_path, audio, samplerate):
    sf.write(file_path, audio.T, samplerate)  # Транспонировать обратно в (num_samples, num_channels)

def main(input_file, output_file):
    audio, samplerate = read_audio(input_file)
    augmentor = Augmentor()
    augmented_audio = augmentor.augment(audio)
    save_audio(output_file, augmented_audio, samplerate)

if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='Audio Data Augmentation')
    # parser.add_argument('input_file', type=str, help='Path to input audio file')
    # parser.add_argument('output_file', type=str, help='Path to save augmented audio file')
    
    # args = parser.parse_args()
    # main(args.input_file, args.output_file)
    main('silerov4_ru_baya.wav', 'out.wav')