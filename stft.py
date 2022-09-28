def stft(data, fs, frame_size=2048, hop_size=512, window='hamming'):
    import numpy as np
    import scipy.fft as sfft
    from scipy.signal import get_window
    
    frame_size = 2048
    hop_size = 1024
    window = get_window(window, frame_size)

    output = np.array([sfft.rfft(window*data[i:i+frame_size]) 
                     for i in range(0, len(data)-frame_size, hop_size)])

    t = np.arange(0, (len(data) - frame_size)/fs, hop_size/fs)
    f = np.arange(0, (fs/2 + 1), fs/frame_size)
    
    return f, t, output.T