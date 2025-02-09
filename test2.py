import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

fsig = 35e6
fc = 1e9
wsig = 2*np.pi*fsig
wc = 2*np.pi*fc

fsamp = 2.5e9
t_stop = 0.2e-6
t = np.arange(0,t_stop,1/fsamp)

sig = np.cos(wsig*t + np.pi/8)*np.cos(wc*t)*np.cos(wc*t)
#sig = np.cos(wsig*t+ np.pi/8)*np.sin(wc*t)
#sig = np.e**(1j * wsig * t)
sig_fft = np.fft.fft(sig)
sig_fft_freq = np.arange(-fsamp/2, fsamp/2, fsamp/(len(t)))*1e-6
sig_fft_pos = sig_fft[0:int(len(t)/2)]
sig_fft_neg = sig_fft[int(len(t)/2):]

sig_fft = np.concatenate((sig_fft_neg, sig_fft_pos))

fig, (ax1, ax2) = plt.subplots(2,1)
ax1.plot(t, np.real(sig), label = "real", color = 'blue')
ax1.plot(t, np.imag(sig), label = "imaginary", color = 'orange')
ax2.plot(sig_fft_freq, np.real(sig_fft), label = "real", color = 'blue')
#ax2.plot(sig_fft_freq, np.imag(sig_fft), label = "imaginary", color = 'orange')

ax1.legend()
ax2.legend()

ax1.grid()
ax2.grid()

plt.show()

