from mcp4725_driver import *
from signal_generator import *
import time

amp = 3.2
sig_freq = 10
samp_freq = 1000

if __name__ == "__main__":
    try:
        
        dac = MCP4725(5.0)

        while True:
            voltage = float(3.2 * get_sin_wave_amp(sig_freq, time.time()))
            dac.set_voltage(voltage)
            wait_for_samp_per(samp_freq)
               

    finally:
        dac.deinit()