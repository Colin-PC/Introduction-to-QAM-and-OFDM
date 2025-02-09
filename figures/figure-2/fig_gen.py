import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

fsig = 35e6
wsig = 2*np.pi*fsig
fc = 500e6
wc = 2*np.pi*fc

fsamp = 100e9
t_stop = 2/fsig
t = np.arange(0,t_stop,1/fsamp)
sig = np.sin(wsig*t)
sig_c = np.sin(wc*t)
sig_total = sig * sig_c

fig, (ax1, ax2, ax3) = plt.subplots(3,1)
ax1.plot(t, sig)
ax2.plot(t, sig_c)
ax3.plot(t, sig_total)

ax1.legend()
ax2.legend()
ax3.legend()

ax1.grid()
ax2.grid()
ax3.grid()

plt.show()

