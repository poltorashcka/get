import numpy
import time

def get_sin_wave_amp(freq, time):
    amp = numpy.sin(2*numpy.pi*freq*time)
    amp += 1
    amp /= 2
    return amp

def wait_for_samp_per(samp_freq):
    time.sleep(1.0/samp_freq)

def get_tr_wave_amp(freq, time):
    amp = 2 / numpy.pi * numpy.arcsin(numpy.sin(2*numpy.pi*freq*time))
    amp += 1
    amp /= 2
    return amp
