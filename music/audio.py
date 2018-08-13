# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 19:13:21 2018

@author: fish
"""

from __future__ import division
import numpy as np
from matplotlib import pyplot as plt
from pydub import AudioSegment
import os
from scipy.io import wavfile


'read audio file different style,now mp3 style'
song = AudioSegment.from_mp3("11.mp3")
# song = AudioSegment.from_wav("3.wav")
# ogg_version = AudioSegment.from_ogg("never_gonna_give_you_up.ogg")
# flv_version = AudioSegment.from_flv("never_gonna_give_you_up.flv")
#
# mp4_version = AudioSegment.from_file("never_gonna_give_you_up.mp4", "mp4")
# wma_version = AudioSegment.from_file("never_gonna_give_you_up.wma", "wma")
# aac_version = AudioSegment.from_file("never_gonna_give_you_up.aiff", "aac")


# song is not modified
# AudioSegments are immutable
# split to mono channel
single = song.split_to_mono()
# single[0].export("single_l.mp3", format="mp3") 'l channel'
# single[1].export("single_r.mp3", format="mp3") 'right channel'
# backwards = song.reverse()  '反序'
# backwards.export("2.mp3", format="mp3")
length = len(song)

print song
print length
sample=single[0][:4096]
print sample
sample.export("sample.wav", format="wav")
samplefs,snd = wavfile.read('sample.wav')
print snd
length =len(snd)
print length
snd=snd/(2.**15)
print 'time =', (length/samplefs)
time_axe= np.array(range(0,length))/samplefs
z = np.fft.fft(snd)
z = np.fft.fftshift(z)


# plot
plt.figure(1)
plt.subplot(231)
plt.plot(time_axe, snd, color='k')
plt.xlabel('time')
plt.ylabel('amp')
plt.title('time domain')
plt.grid('true')

# plt.show()
# plt.figure(2)
plt.subplot(232)
freq_axe=np.array(range(0, length))/length - 0.5
plt.plot(freq_axe,np.abs(z), color='g')
plt.grid('true')
plt.xlabel('fs')
plt.title('freq domain amp')

plt.subplot(233)
freq_axe_hz=(np.array(range(0, length))/length - 0.5)*samplefs
plt.plot(freq_axe_hz,np.abs(z), color='g')
plt.grid('true')
plt.xlabel('hz')
plt.title('freq domain amp')


plt.subplot(224)
plt.plot(np.array(range(0,length)),snd,color='y')
plt.xlabel('sample dot')
plt.ylabel('amp')
plt.grid('true')
plt.title('dot domain amp')


plt.subplot(235)
m = np.angle(z)
plt.plot(freq_axe, np.angle(z),'bo')
plt.grid('true')
plt.xlabel('fs')
plt.title('freq domain pha')

plt.show()



