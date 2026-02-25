from r2r_dac import *
from signal_generator import *

amp = 3.2
sig_freq = 10
samp_freq = 1000

if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)

        while True:
            vol = float(3.183 * get_sin_wave_amp(sig_freq, time.time()))
            dac.set_vol(vol)
            wait_for_samp_per(samp_freq)


    finally:
        dac.deinit()