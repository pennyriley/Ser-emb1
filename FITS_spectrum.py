#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 13:53:30 2021

@author: penny
"""
import os
os.chdir('/Users/penny/Desktop/Research/CH3CN')


import numpy as np
from astropy.io import fits
import matplotlib
import matplotlib.pyplot as plt
from astropy.table import Table








file = fits.open('Ser-emb-1_USB-centralpix.fits')
file.info()

header= file[0].header
Nrpix = header['NAXIS1']
data = file[0].data-0.085

pixels = np.arange(3860)

#right_freq=[]
#left_freq=[]
freq = []

for i in range(len(pixels)):
    if i == 1310:
        #right_freq.append(header['RESTFREQ'])
        freq.append(header['RESTFREQ'])
        
    elif i > 1310:
        #right_freq.append(header['RESTFREQ'] + i * header['CDELT1'] )
        #freq.append(header['RESTFREQ'] + i * header['CDELT1'] )
        freq.append(header['RESTFREQ'] + (i -1310) * header['CDELT1'] )
    elif i < 1310:
        #left_freq.append(header['RESTFREQ'] -i * header['CDELT1'])
        #freq.append(header['RESTFREQ'] -i * header['CDELT1'])
        freq.append(header['RESTFREQ'] - (1310-i) * header['CDELT1'])

plt.axvline(x=257527.384*10**6, color='r', label='CH3CN ')
plt.axvline(x=257522.428*10**6, color='r', label='CH3CN ')
plt.axvline(x=257507.562*10**6, color='r', label='CH3CN ')
plt.axvline(x=257482.792*10**6, color='r', label='CH3CN ')
plt.axvline(x=257448.128*10**6, color='r', label='CH3CN ')
plt.axvline(x=257403.585*10**6, color='r', label='CH3CN ')
plt.axvline(x=257349.179*10**6, color='r', label='CH3CN ')
plt.axvline(x=257284.935*10**6, color='r', label='CH3CN ')
plt.axvline(x=257210.878*10**6, color='r', label='CH3CN ')
plt.axvline(x=257127.036*10**6, color='r', label='CH3CN ')
plt.axvline(x=257403.585*10**6, color='b', label='CH3OH')





#set certain x limits
#plt.xlim(257000*10**6, 259000*10**6)
#plt.xlim(257000*10**6, 258000*10**6)
#plt.xlim(257000*10**6, 257560*10**6)
#plt.xlim(257380*10**6, 257600*10**6)
plt.xlim(257100*10**6, 257600*10**6)

plt.ylim(0.0, 0.2)

plt.plot(freq, data[0,0,0,:])
plt.legend()
plt.show()

model_file = fits.open('Ser-emb-1_T250_N13_FWHM5.fits')
model_file.info()

model_data=model_file[0].data

plt.xlim(257350*10**6,257600*10**6 )
plt.ylim(0.0, 0.150)
plt.plot(freq, data[0,0,0,:], label='Observed')
plt.plot(freq, model_data[0,0,0,:], label='Model_T250_N13_FWHM5')
plt.legend()
plt.show()


