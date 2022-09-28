# Fourier Transform

basic Discrete Fourier Transform (DFT), Fast Fourier Transform (FFT) and Short-Time Fourier Transform (STFT) implementations;

use this command line:
<code>python main.py <filename> <algorithm></code>
to graph desired algorithms, for example:

<code>python main.py <filename> stft</code>

for STFT spectrogram on that file.

you can specify some optional parameters:
1. <code>--frame-size N</code> set frame size (which is equal to window size in this case) to N samples 
2. <code>--hop-size N</code> set hop size to N samples ("shift" size to next window measure)
3. <code>--window window_function_name</code> set desired window function (possible window identifiers are at the bottom of this readme)

NOTE: in order for DFT to not flood your memory, it slices signal to only first 1024 samples.

Possible window function identifiers:
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
'kaiser'
