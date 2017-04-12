#Plots ultrasonic waveform from ASCII file
#import select libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import signal

#Input stage number
stage  = int(input('Stage:'))
file = 'stage%drec5.txt' %stage

#load waveform
wf = np.loadtxt(file,skiprows = 0)
#wf1 = np.loadtxt('stage29rec5.txt',skiprows = 0)

#Detrend waveform
wf = signal.detrend(wf)
#wf1 = signal.detrend(wf1)

#Set up x axis and time if necessary
x = np.linspace(0,wf.size-1,num=wf.size)
time = (x[:] - 513)*0.02

fig = plt.figure(figsize=(15,8))
ax = fig.add_subplot(1,1,1)
ax.plot(x[:],wf[:],color = 'b', linewidth = 2)
#ax.plot(x[:],wf1[:],color = 'r', linewidth = 2)
plt.grid()
plt.show()
