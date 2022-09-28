from dft import dft
from fft import fft
from stft import stft
from utils import parse_args


import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read as read_wav


algos = {
    'dft': dft,
    'fft': fft,
    'stft': stft,
}

windows = {
    'boxcar',
    'triang',
    'blackman',
    'hamming',
    'hann',
    'bartlett',
    'flattop',
    'parzen',
    'bohman',
    'blackmanharris',
    'nuttall',
    'barthann',
    'kaiser',
}

def main():
    args = parse_args()
    if args.algo not in algos:
        raise ValueError('Invalid algorithm')
    if args.window not in windows:
        raise ValueError('Invalid window function')

    fs, data = read_wav(args.filename)
    if len(data.shape) > 1:
        data = data[:, 0]  # Only use the first channel
    if args.algo == 'stft':
        f, t, output = algos[args.algo](data, fs, args.frame_size, args.hop_size, args.window)

        plt.pcolormesh(t, f, np.abs(output))
    else:
        output = algos[args.algo](data)
        plt.plot(np.abs(output))

    plt.show()


if __name__ == '__main__':
    main()