from utils import preprocess
import numpy as np

def fft(data):
    # Add zero padding to the data
    data = preprocess(data)

    def _fft(data):
        n = len(data)
        if n <= 1:
            return data
        even = _fft(data[0::2])
        odd = _fft(data[1::2])

        temp = np.zeros(n).astype(np.complex64)
        for k in range(n//2):
            temp[k] = even[k] + np.exp(-2j * np.pi * k / n) * odd[k]
            temp[k + n//2] = even[k] - np.exp(-2j * np.pi * k / n) * odd[k]

        return temp

    return _fft(data)