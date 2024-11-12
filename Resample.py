import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
import scipy.signal as sg
import numpy.fft as fft

from math import pi as pi
from numpy import abs as abs
from numpy import exp as exp
from numpy import conj as conj
from numpy import real as real
from numpy import imag as imag
from numpy import log10 as log10
from numpy import argmax as argmax
from numpy import arange as arange
from numpy import correlate as correlate
from scipy.signal import resample as resample
from scipy.signal import resample_poly as resample_poly
from scipy.signal import decimate as decimate
from scipy.signal import upfirdn as upfirdn
from scipy.interpolate import interp1d as interp

def load (file):
    a = np.fromfile(file, np.int16)  # lee para a o ficheiro
    r = np.zeros(int(np.size(a) / 2), np.complex64)  # crea o array r de de 0 de forma a e tipo complex64
    r.real = a[::2]  # garda na parte real de r os compoñentes impares do array a
    r.imag = a[1::2]  # garda na parte imaxinaria de r os compoñentes pares de de a

    return r

file1="/home/jorge/Documentos/TFG/RF-5MHz.iq"

def resampling(iq_signal, fs_in, fs_out, signal_length):
    resampled_iq = sg.resample(iq_signal[0 : round(signal_length * fs_in / fs_out)], signal_length)
    resampled_iq = resampled_iq[0 : signal_length - 1]

    return resampled_iq

s1 = load(file1)

s1 = resampling(s1, 78125, 76300, s1.size)

print(str(s1.size))