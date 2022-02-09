#Plots ultrasonic waveform from ASCII file
#import select libraries
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

#computes the threshold value for the noise prior to P-arrival and after the signal
#impulse response
def get_threshold(detrended_signal,min_value,max_value,Post_impulse):
    threshold = 10*np.std(detrended_signal[min_value:max_value])
    Index = np.min(np.where(np.abs(detrended_signal[Post_impulse:])>threshold)[0])+Post_impulse
    return threshold,Index

#Converts an index to time (in microseconds)
def rec2time(index,fs):
    #returns time in seconds
    time = ((index)/(fs))*1e6
    return time

fs = 50000000.                   #Sampling frequency 50 MHz
min_value = 200
max_value = 300
Post_impulse = 300
cutoff_index = 6000

#Input stage number
stage  = int(input('Stage:'))
file = 'stage%drec4.txt' %stage

#load waveform
wf = np.loadtxt(file,skiprows = 0)

#Detrend waveform
wf = signal.detrend(wf[0:cutoff_index])

#Compute threshold and arrival index
threshold, arrival = get_threshold(wf, min_value,max_value,Post_impulse)
P_arrival_time = rec2time(arrival,fs)
print("P arrival index: %0.1f" %arrival)
print("P arrival time: %0.2f microseconds" %P_arrival_time)

#Set up x axis and time if necessary
x = np.linspace(0,wf.size-1,num=wf.size)
time = (x[:]/fs)*1e6

fig = plt.figure(figsize=(15,8))
ax = fig.add_subplot(1,1,1)
ax.plot(x[:],wf[:],color = 'b', linewidth = 2)
ax.axhline(y=threshold,xmin=0,xmax=500,c='k',linewidth=2,label = '+threshold')
ax.axhline(y=-threshold,xmin=0,xmax=500,c='k',linewidth=2,label = '-threshold')
ax.set_xlim(0,2000)

plt.grid()
plt.show()

#Editing test for github. 
#copyright Peter Miller
