import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

plt.rcParams['text.usetex'] = True

figure_width = 13.8
figure_ratio = 2.19

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

title_font = 30
axis_font = 16
num_font = 14

t = t * 1e9

fig, (ax1, ax2, ax3) = plt.subplots(3,1)
title = 'Amplitude Modulation - Time Domain Example'
plt.suptitle(title, fontsize = title_font)

ax3.set_xlabel("Time (ns)", fontsize = axis_font)
ax1.set_ylabel("Voltage (V)", fontsize = axis_font)
ax2.set_ylabel("Voltage (V)", fontsize = axis_font)
ax3.set_ylabel("Voltage (V)", fontsize = axis_font)

ax1.plot(t, sig)
ax2.plot(t, sig_c)
ax3.plot(t, sig_total)

ax1.legend()
ax2.legend()
ax3.legend()

ax1.grid()
ax2.grid()
ax3.grid()

fig.set_size_inches(figure_width, figure_width/figure_ratio, forward=True)
plt.tight_layout(pad=1.08, h_pad=None, w_pad=None, rect=None)
fig.savefig("figure.png")

