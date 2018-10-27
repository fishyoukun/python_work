from __future__ import division
import numpy as np
from matplotlib import pyplot as plt
import os
import time

def DataRead_to_FloatChannel(filename, datatype, ChanNum, fs, comments, Q):
    # read file
    data_in = np.fromfile(filename, dtype=datatype)
    data_len_ori = len(data_in)
    data_len = data_len_ori // ChanNum
    print comments + " total len = ", data_len_ori
    print comments + " data_len = ", data_len

    # initial the data structure channal * data_dot
    data = np.zeros([ChanNum, data_len], float)

    for i in np.arange(ChanNum):
        for j in np.arange(data_len):
            data[i][j] = data_in[j * ChanNum + i] / np.power(2, Q)
    return data, data_len

    # remove leading zero and tail-zero


def data_remove_ltzero(data, len):
    leadingzeroflag = 0
    leadingzeronum = 0
    tailingzeroflag = 0
    tailingzeronum = 0
    halflen = len // 2
    dataout = np.zeros(len, float)
    for i in range(halflen):
        if (data[i] != 0.0):
            leadingzeroflag = 1
            leadingzeronum = i
            break
    dataout[0:halflen - i] = data[i:halflen]
    for j in range(halflen):
        if (data[-j] != 0.0):
            tailingzeroflag = 1
            tailingzeronum = len - j + 1
            break
    dataout[halflen - i:len - i - j + 1] = data[halflen:len - j + 1]
    dataoutlen = len - i - j + 1
    return dataout[0:dataoutlen], dataoutlen


# only analyse channel 0
def Data_fft(data, len, window):
    lenout = (len + 1) // 2
    if (window == True):
        window = np.hanning(len)
        window_data = data * window
        z = np.fft.fft(window_data) / np.sqrt(len)
    else:
        z = np.fft.fft(data) / np.sqrt(len)
    zout = z[0:lenout]
    return zout, lenout

def get_intensity_of_freq(ffted_abs_data,fs,freq):
    data_len = len(ffted_abs_data)
    data_inex = int(data_len * freq / (0.5 * fs))
    data = ffted_abs_data[data_inex]
    return data



def data_normlize(data):
    max = np.max(data)
    dataout = data[0:len(data)] / max
    return dataout


if __name__ == '__main__':
    time_pre = time.time()
    # configuration
    fs = 48000
    freq_analize = True
    plotflag = False
    windowflag = False
    harmonic_order = 6
    base_wave = 1000.0
    freq_array = [0.0] * harmonic_order
    for i in range(harmonic_order):
        freq_array[i] = base_wave * (i+1)
    # freq_array = [1000.0,2000.0, 3000.0, 4000.0, 5000.0, 6000.0]
    abs_array = [0]*len(freq_array)


    file_dir = 'D:\dumpresult\dump1k'
    SourceAudioFileNameOnly = 'dump-input-Media-ch02-s32-48000Hz-40s.raw'
    SinkAudioFileNameOnly = 'dump-output-alsa_output.hw_0_14-ch08-s32-48000Hz-40s.raw'
    SourceChanNum = 2
    SinkChanNum = 8
    datatype = np.int16
    SourceQ = 15
    SinkQ = 15

    # generate config
    sinkfilename = file_dir + '\\' + SinkAudioFileNameOnly

    # sink
    (sinkdata, sinklen) = DataRead_to_FloatChannel(sinkfilename, datatype, SinkChanNum, fs, 'sink', SinkQ)
    (sink_remove, sink_num) = data_remove_ltzero(sinkdata[0], sinklen)

    (sink_fft_result, sink_fft_len) = Data_fft(sink_remove, sink_num,windowflag)
    sink_fft_abs = np.abs(sink_fft_result)
    sink_fft_abs_normal = data_normlize(sink_fft_abs)
    print "sink_num = " + str(sink_num)
    # sink_fft_abs_normal = data_normlize(sink_fft_abs)
    harmonic_intensive = 0.0
    for i in range(len(freq_array)):
        abs_array[i] = get_intensity_of_freq(sink_fft_abs,fs,freq_array[i])
    base_intensive = abs_array[0]
    for i in abs_array[1::]:
        harmonic_intensive = i*i + harmonic_intensive
    harmonic_intensive = np.sqrt(harmonic_intensive)

    result = harmonic_intensive / base_intensive
    print "thd result = "+ str(result)
    # print abs_array

    # plot
    freq_axe = np.linspace(0, 0.5, sink_fft_len) * fs
    plt.figure()
    plt.title("sink spectrum")
    plt.plot(freq_axe, sink_fft_abs_normal)
    plt.yscale('log')
    plt.xlabel('Hz')
    plt.ylabel('log')

    plt.figure()
    plt.title("harmonic intense")
    plt.stem(freq_array, abs_array)
    plt.yscale('log')
    plt.xlabel('Hz')
    plt.text(4000.0, 10.0, 'THD = '+str(result))

    # calculate time_duration
    time_after = time.time()
    time_duration = time_after - time_pre
    print "time_duration = " + str(time_duration) + " seconds"
    print "over"

    plt.show()