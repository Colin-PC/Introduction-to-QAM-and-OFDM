import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

fsig = 35e6
wsig = 2*np.pi*fsig
fsamp = 200e6
t_stop = 0.2e-6
t = np.arange(0,t_stop,1/fsamp)
sig = np.sin(wsig*t)
#sig = np.e**(1j * wsig * t)
sig_fft = np.fft.fft(sig)
sig_fft_freq = np.arange(-fsamp/2, fsamp/2, fsamp/(len(t)))*1e-6
sig_fft_pos = sig_fft[0:int(len(t)/2)]
sig_fft_neg = sig_fft[int(len(t)/2):]

sig_fft = np.concatenate((sig_fft_neg, sig_fft_pos))

fig, (ax1, ax2) = plt.subplots(2,1)
ax1.stem(t, np.real(sig), label = "real", linefmt ='blue', markerfmt ='blue')
ax1.stem(t, np.imag(sig), label = "imaginary", linefmt ='orange', markerfmt ='orange')
ax2.stem(sig_fft_freq, np.real(sig_fft), label = "real", linefmt ='blue', markerfmt ='blue')
ax2.stem(sig_fft_freq, np.imag(sig_fft), label = "imaginary", linefmt ='orange', markerfmt ='orange')

ax1.legend()
ax2.legend()

ax1.grid()
ax2.grid()

plt.show()

