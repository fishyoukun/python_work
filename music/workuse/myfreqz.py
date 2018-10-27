# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 19:13:21 2018

@author: fish
"""

from __future__ import division
import numpy as np
from matplotlib import pyplot as plt
import scipy.signal as ss

# b=[1.0/(2.0+np.sqrt(2.0)),2.0/(2.0+np.sqrt(2.0)),1.0/(2+np.sqrt(2.0))]
# a=[1.0,0.0,-1*np.sqrt(2.0)/(2.0+np.sqrt(2.0))]
b=[4.52,0.52,0.0]
a=[1.0,0.0,0.0]
w,h = ss.freqz(b,a,1024,0)
#np.fft.fftshift(w)
plt.figure()
plt.plot(w/np.pi,np.abs(h))
plt.show()
#print h