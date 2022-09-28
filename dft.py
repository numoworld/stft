def dft(data):
    import numpy as np
    # because of the computational-heavy nature of the DFT, 
    # we will only use the first 1024 samples
    data = data[:1024]
    n = len(data)
    i, k = np.meshgrid(np.arange(n), np.arange(n))
    dft_matrix = np.exp(-2j * np.pi * i * k / n)
    return np.dot(dft_matrix, data)
