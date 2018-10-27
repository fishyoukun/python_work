from __future__ import division
import numpy as np
from matplotlib import pyplot as plt
from pydub import AudioSegment
import os
from scipy.io import wavfile
# import play2 as pl2
import pyaudio
import wave

# configuration
fs = 48000
freq_analize = False
need_remove_zero = True
audio_play = False
plotflag = True
CHUNK = 1024

# read file
file_dir = 'C:\Users\KYou\Documents\FDK_Workspace\.debug\probes\ProbeSession.180906165525'
file_nameonly = 'module-COPIER(1) Output-0.pcm'
filename = file_dir + '\\' + file_nameonly
data_in = np.fromfile(filename, dtype=np.int32)

# remove zero
if need_remove_zero == True:
    j = 0
    data = np.zeros(len(data_in), int)
    for i in np.arange(len(data_in)):
        if data_in[i] != 0:
            data[j] = data_in[i]
            j = j + 1
else:
    data = data_in
    i = len(data_in)
    j = i
# repair the j index
j = j - 1
print "file length : ", i
print "file_0_remove length : ", j
wavfile.write('b.wav', fs, data)

if plotflag == True:
    time_axe = np.array(range(0, j)) / fs
    plt.figure()
    plt.subplot(211)
    plt.plot(time_axe, data_in[0:j], 'r')
    plt.grid('true')
    plt.xlabel('tims /s')
    plt.title('time domain amp')

    time_axe = np.array(range(0, j)) / fs
    plt.subplot(212)
    plt.plot(time_axe, data[0:j], color='r')
    plt.grid('true')
    plt.xlabel('tims /s')
    plt.title('time domain amp')
    plt.show()

# freq_analize
if freq_analize == True:
    z = np.fft.fft(data[0:j])
    z = np.fft.fftshift(z)
    freq_axe = np.array(range(0, j)) / j - 0.5
    plt.figure()
    plt.plot(freq_axe, np.abs(z), color='g')
    plt.grid('true')
    plt.xlabel('fs')
    plt.title('freq domain amp')
    plt.show()

if audio_play == True:
    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()
    data_f = np.zeros(j, float)
    data_temp = np.zeros(64, float)
    data_f = np.true_divide(data, pow(2, 31))
    # print len(data_f)
    # open stream (2)
    # stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
    #                 channels=wf.getnchannels(),
    #                 rate=wf.getframerate(),
    #                 output=True)
    stream = p.open(format=4,
                    channels=1,
                    rate=16000,
                    output=True)
    # play stream (3)
    k = 0
    chunk_num = j // 64 + 1
    for k in range(0, chunk_num):
        data_temp = data_f[k * 64:(k + 1) * 64]
        stream.write(data_temp)

    # stop stream (4)
    stream.stop_stream()
    stream.close()

    # close PyAudio (5)
    p.terminate()
