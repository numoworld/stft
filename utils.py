def _next_power_of_two(x):
    return 1 if x == 0 else 2**(x - 1).bit_length()

def preprocess(data):
    import numpy as np
    # Pad with zeros to the next power of two
    padded = np.zeros(_next_power_of_two(len(data)), dtype=np.complex64)
    padded[:len(data)] = data
    return padded

def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='WAV file to process')
    parser.add_argument('algo', type=str, help='Algorithm to use: dft, fft, stft')
    parser.add_argument('--frame_size', type=int, default=2048, help='Frame size')
    parser.add_argument('--hop_size', type=int, default=512, help='Hop size')
    parser.add_argument('--window', type=str, default='hamming', help='Window function')
    return parser.parse_args()