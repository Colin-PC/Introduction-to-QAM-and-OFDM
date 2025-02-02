import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

fsig = 20e6
wsig = np.pi*fsig
fsamp = 200e6
t_stop = 0.2e-6
t = np.arange(0,t_stop,1/fsamp)
sig = 1j*np.sin(wsig*t)
#sig = np.e**(1j * wsig * t)
sig_fft = np.fft.fft(sig)

fig, (ax1, ax2) = plt.subplots(2,1)
ax1.plot(t, np.real(sig), label = "real", color = 'blue')
ax1.plot(t, np.imag(sig), label = "imaginary", color = 'orange')
ax2.stem(np.real(sig_fft), label = "real", linefmt ='blue', markerfmt ='blue')
ax2.stem(np.imag(sig_fft), label = "imaginary", linefmt ='orange', markerfmt ='orange')

ax1.legend()
ax2.legend()

ax1.grid()
ax2.grid()

plt.show()

