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


def data_normlize(data):
    max = np.max(data)
    dataout = data[0:len(data)] / max
    return dataout


if __name__ == '__main__':

    time_pre = time.time()
    # configuration
    fs = 48000
    freq_start = 20
    freq_stop = 20000

    freq_analize = True
    plotflag = False
    windowflag = False

    file_dir = 'D:\dumpresult\dump_sweep'
    SourceAudioFileNameOnly = 'dump-input-Media-ch02-s32-48000Hz-60s.raw'
    SinkAudioFileNameOnly = 'dump-output-alsa_output.hw_0_14-ch08-s32-48000Hz-60s.raw'
    SourceChanNum = 2
    SinkChanNum = 8
    datatype = np.int16
    SourceQ = 15
    SinkQ = 15

    # generate config
    sourcefilename = file_dir + '\\' + SourceAudioFileNameOnly
    sinkfilename = file_dir + '\\' + SinkAudioFileNameOnly

    # source
    (sourcedata, sourcelen) = DataRead_to_FloatChannel(sourcefilename, datatype, SourceChanNum, fs, 'source', SourceQ)
    (source_remove, source_num) = data_remove_ltzero(sourcedata[0], sourcelen)
    (source_fft_result, source_fft_len) = Data_fft(source_remove, source_num, windowflag)
    source_fft_abs = np.abs(source_fft_result)
    source_fft_abs_normal = data_normlize(source_fft_abs)

    # sink
    (sinkdata, sinklen) = DataRead_to_FloatChannel(sinkfilename, datatype, SinkChanNum, fs, 'sink', SinkQ)
    (sink_remove, sink_num) = data_remove_ltzero(sinkdata[0], sinklen)
    (sink_fft_result, sink_fft_len) = Data_fft(sink_remove, sink_num, windowflag)
    sink_fft_abs = np.abs(sink_fft_result)
    sink_fft_abs_normal = data_normlize(sink_fft_abs)

    print "source_num = " + str(source_num)
    print "sink_num = " + str(sink_num)

    # calculate freqency response
    final_num = source_fft_len
    if (source_fft_len > sink_fft_len):
        final_num = sink_fft_len

    result = sink_fft_result[0:final_num] / source_fft_result[0:final_num]
    result_abs = np.abs(result)
    result_normal = data_normlize(result_abs)

    # for plot
    freq_axe = np.linspace(0, 0.5, final_num) * fs
    plt.figure()
    plt.title("source spectrum")
    plt.plot(freq_axe, source_fft_abs_normal[0:final_num])
    plt.figure()
    plt.title("sink spectrum")
    plt.plot(freq_axe, sink_fft_abs_normal[0:final_num])

    plt.figure()
    plt.title("freqency reponse")
    # plt.plot(freq_axe, 20 * np.log(np.abs(result)))
    data_interest_start = int(final_num*freq_start/(0.5* fs))
    data_interest_stop = int(final_num*freq_stop/(0.5* fs))
    data_interest_len =  data_interest_stop - data_interest_start
    freq_axe_interest = np.linspace(freq_start, freq_stop, data_interest_len)
    data_interest = result_abs[data_interest_start:data_interest_stop]

    plt.plot(freq_axe_interest, data_interest)
    plt.yscale('log')
    plt.xlabel('Hz')
    plt.ylabel('log')

    # calculate time_duration
    time_after = time.time()
    time_duration = time_after - time_pre
    print "time_duration = "+str(time_duration)+" seconds"
    print "over"
    plt.show()
