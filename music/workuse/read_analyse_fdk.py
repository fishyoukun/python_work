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
    data_in = np.fromfile(filename, dtype=datatype)

    data_len_ori = len(data_in)
    data_len = data_len_ori // ChanNum
    print "data_len_ori = ", data_len_ori
    print "data_len = ", data_len
    # initial the data structure channal * data_dot
    data = np.zeros([ChanNum,data_len], float) # initial 2 dimension data array

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
        plt.show()

    # freq_analize
    if freq_analize == True:
        # window = np.hanning(data_len)
        # z = np.fft.fft(data[i][0:data_len] * window)

        # plt.figure()
        # for i in np.arange(ChanNum):
        #     plt.figure()
        #     plt.subplot(ChanNum + 1, 1, i + 1)
            # freq_axe = np.linspace(-0.5, 0.5, data_len) * fs
            # z = np.fft.fft(data[i][0:data_len]) / np.sqrt(data_len)
            # z = np.fft.fftshift(z)
            # plt.plot(freq_axe, (np.abs(z)), color='g')
            # plt.plot(freq_axe, np.abs(z), color='g')
            # plt.plot(freq_axe, window, color='r')
            # plt.yscale('log')
            # plt.grid('true')
            # plt.xlabel('fs')
            # plt.title(comments)
            # plt.show()
        plt.figure()
        window = np.hanning(data_len)
        freq_axe = np.linspace(-0.5, 0.5, data_len) * fs
        z = np.fft.fft(data[0] ) / np.sqrt(data_len)  # first channel
        z = np.fft.fftshift(z)

        plt.plot(freq_axe, 20*np.log(np.abs(z)), color='g')
        # plt.plot(freq_axe, np.abs(z), color='g')

        # plt.yscale('linear')
        plt.grid('true')
        plt.xlabel('fs')
        # plt.title(comments)
        plt.show()

if __name__ == '__main__':
    # configuration
    fs = 48000
    freq_analize = True
    plotflag = False

    AudioFilePath = r'C:\Users\KYou\Documents\FDK_Workspace\.debug\probes\ProbeSession.180921210905'
    AudioFileNameOnly = 'module-COPIER(1) Output-0.pcm'
    # SourceAudioFileNameOnly = r'chirp_48K_20hz_20khz_2CH_40s_-15dB.wav'
    # SinkAudioFileNameOnly = 'dump-output-alsa_output.hw_0_14-ch08-s32-48000Hz-20s.raw'
    SourceChanNum = 8
    # SinkChanNum = 8
    datatype = np.int32
    SourceQ = 31
    # SinkQ = 15

    filename = AudioFilePath + '\\' + AudioFileNameOnly

#source file
DataReadFreqAnalyse(filename,datatype,SourceChanNum,fs,'source',SourceQ)

# DataReadFreqAnalyse(SinkAudioFileNameOnly,datatype,SinkChanNum,fs,'sink',SinkQ)
# plt.show()







