import RPi.GPIO as GPIO 
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.007, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def dec2bin(self, dec):
        return [int(bit) for bit in bin(dec)[2:].zfill(8)]

    def num2dac(self, value):
        signal = self.dec2bin(value)
        GPIO.output(self.bits_gpio, signal)
        return signal

    def seq_count_adc(self):
        for i in range (256):
            self.num2dac(i)
            time.sleep(self.compare_time)
            if (GPIO.input(self.comp_gpio) == 1) or (i == 255):
                return i * self.dynamic_range / 255

    def get_sc_voltage(self):
        vol = self.seq_count_adc()
        print("voltage", vol)
        return vol

    

if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.216)

        while True:
            adc.get_sc_voltage()
          

    finally:
        adc.deinit()
        

        