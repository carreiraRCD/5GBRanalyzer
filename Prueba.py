from scipy.signal import butter
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

t_duration = np.linspace(0,0.5,2000,False)

sign = np.sin(2*np.pi*20*t_duration) + np.sin(2*np.pi*40*t_duration)

fig, (ax1) = plt.subplots(1, 1, sharex=True)
ax1.plot(t_duration, sign)
ax1.set_title('20 and 40 Hz Sinusoid')
ax1.axis([0, 0.5, -2, 2.5])

sos = butter(15, 20, 'lp', fs=2000, output="sos")
filtd = signal.sosfilt(sos, sign)

fig, (ax2) = plt.subplots(1, 1, sharex=True)
ax2.plot(t_duration, filtd)
ax2.set_title('After applying 20 Hz high-pass filter')
ax2.axis([0, 0.5, -2, 2.5])
ax2.set_xlabel('Time (seconds)')
plt.tight_layout()


sos2 = butter(15, 20, 'hp', fs=2000, output="sos")
filtd2 = signal.sosfilt(sos2, sign)

fig, (ax3) = plt.subplots(1, 1, sharex=True)
ax3.plot(t_duration, filtd2)
ax3.set_title('After applying 20 Hz high-pass filter')
ax3.axis([0, 0.5, -2, 2.5])
ax3.set_xlabel('Time (seconds)')
plt.tight_layout()
plt.show()