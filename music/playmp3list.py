# -*- coding: utf-8 -*-
import playmp3 as pl
songlist=[
            r'1.mp3',
            r'11.mp3'
          ]
#loop time
N = 10
for j in range(0,N):
    for i in range(0,len(songlist)):
        pl.playmp3(songlist[i])


