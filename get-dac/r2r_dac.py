import RPi.GPIO as GPIO 

class R2R_DAC:
    def __init__(self, gpio_bits, dyn_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dyn_range = dyn_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()
    
    def set_num(self, num):
        GPIO.output(self.gpio_bits, [int(element) for element in bin(num)[2:].zfill(8)])

    def set_vol(self, vol):
        num = int(vol / self.dyn_range * 255)
        GPIO.output(self.gpio_bits, [int(element) for element in bin(num)[2:].zfill(8)])


if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)

        while True:
            try:
                vol = float(input("введите напряжение в вольтах: "))
                dac.set_vol(vol)

            except ValueError:
                print("вы ввели не число. трай эгэин\n")

    finally:
        dac.deinit()