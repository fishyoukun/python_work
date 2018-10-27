from __future__ import division
import numpy as np
from matplotlib import pyplot as plt
from pydub import AudioSegment
import os
from scipy.io import wavfile
# import play2 as pl2
import pyaudio
import wave

def DataReadFreqAnalyse(audiofile,datatype,ChanNum,fs,comments,Q):
    # read file
    file_dir = 'D:\dumpresult\dump'
    # file_nameonly = 'dump-output-alsa_output.hw_0_14-ch08-s32-48000Hz-20s.raw'
    # file_nameonly = 'dump-input-Media-ch02-s32-48000Hz-20s.raw'
    filename = file_dir + '\\' + audiofile
    data_in = np.fromfile(filename, dtype=datatype)

    data_len_ori = len(data_in)
    data_len = data_len_ori // ChanNum
    print "data_len_ori = ", data_len_ori
    print "data_len = ", data_len
    # initial the data structure channal * data_dot
    data = np.zeros([ChanNum,data_len], float)


    for i in np.arange(ChanNum):
        for j in np.arange(data_len):
            data[i][j] = data_in[j * ChanNum + i]/np.power(2,Q)

    if plotflag == True:
        time_axe = np.linspace(0,data_len,data_len)/fs
        plt.figure()
        for i in np.arange(ChanNum):
            # for j in np.arange(data_len):
            plt.subplot(ChanNum+1,1,i+1)
            plt.plot(time_axe, data[i])
            plt.grid('true')
            plt.xlabel('tims /s')
            # plt.title('time domain amp')

    # freq_analize
    if freq_analize == True:
        # window = np.hanning(data_len)
        # z = np.fft.fft(data[i][0:data_len] * window)
        z = np.fft.fft(data[i][0:data_len]) / np.sqrt(data_len)
        z = np.fft.fftshift(z)
        # freq_axe = (np.array(range(0, data_len)) / data_len - 0.5) * fs
        freq_axe = np.linspace(-0.5, 0.5,data_len) * fs
        plt.figure()
        for i in np.arange(ChanNum):
            plt.subplot(ChanNum + 1, 1, i + 1)
            plt.plot(freq_axe, 20*np.log(np.abs(z)), color='g')
            # plt.plot(freq_axe, window, color='r')
            plt.yscale('log')
            plt.grid('true')
            plt.xlabel('fs')
        plt.title(comments)


if __name__ == '__main__':
    # configuration
    fs = 48000
    freq_analize = True
    plotflag = True

    SourceAudioFileNameOnly = 'dump-input-Media-ch02-s32-48000Hz-20s.raw'
    # SourceAudioFileNameOnly = 'chirp_48K_20hz_20khz_2CH_40s_-15dB.wav'
    SinkAudioFileNameOnly = 'dump-output-alsa_output.hw_0_14-ch08-s32-48000Hz-20s.raw'
    SourceChanNum = 2
    SinkChanNum = 8
    datatype = np.int16
    SourceQ = 15
    SinkQ = 15


#source file
DataReadFreqAnalyse(SourceAudioFileNameOnly,datatype,SourceChanNum,fs,'source',SourceQ)

# DataReadFreqAnalyse(SinkAudioFileNameOnly,datatype,SinkChanNum,fs,'sink',SinkQ)
plt.show()







