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

Some examples:

**DFT**: <br>
<code>python main.py sound.wav dft</code><br> <br>
output:<br>
![image](https://user-images.githubusercontent.com/32400447/192854514-eb664db9-2c77-45f8-838f-ed6bb8e7bc23.png) <br><br>



**FFT**:<br>
<code>python main.py sound.wav fft</code><br><br>
output:<br>
![image](https://user-images.githubusercontent.com/32400447/192854692-6dd31e00-135b-4e19-9999-f8c91ffa4717.png) <br><br>


**STFT**:<br>
<code>python main.py sound.wav stft</code><br><br>
output:<br>
![image](https://user-images.githubusercontent.com/32400447/192854890-b3f1a819-0136-4236-a15e-6e87ad16eaf9.png) <br>

<br><br>
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

