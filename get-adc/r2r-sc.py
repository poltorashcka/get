import r2r_adc
import time
import adc_plot as plt

adc = r2r_adc.R2R_ADC(3.183, 0.0001)
vol_vals = []
t_vals = []
dur = 15.0

if __name__ == "__main__":
    try:
        begin = time.time()
        while time.time() - begin < dur:
            vol_vals.append(adc.get_sc_voltage())
            t_vals.append(time.time() - begin)
        plt.plt_vol_vs_time(t_vals, vol_vals, 3.183)
        plt.plot_samp_per_h(t_vals)
    
    finally:
        adc.deinit()