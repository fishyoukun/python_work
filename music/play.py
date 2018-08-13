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
import time
import pygame
file=r'1.mp3'
nextfile = r'11.mp3'
'read audio file different style,now mp3 style'
song = AudioSegment.from_mp3(file)
length = len(song)
dura_time = song.duration_seconds
samplefs = song.frame_rate
print 'length = ', (length)
print 'frame_rate = ', (samplefs)
# print 'time =', (length/samplefs)
print 'duration time =', (dura_time)
# play music
# pygame.init()
pygame.mixer.init()
print("play music start")
track = pygame.mixer.music.load(file)
repeatnum=10

pygame.mixer.music.play(repeatnum, 0)
time.sleep(dura_time*(repeatnum+1))
# time.sleep(dura_time*1)
pygame.mixer.music.stop()
# pygame.mixer.music.queue(nextfile)
# pygame.mixer.music.play(0, 0.0)
print "play over"