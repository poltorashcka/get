import RPi.GPIO as GPIO 
#import time
GPIO.setmode(GPIO.BCM)

#leds = [22, 27, 17, 26, 25, 21, 20, 16]
leds = [16, 20, 21, 25, 26, 17, 27, 22]

GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
dyn_range = 3.3

def vol2num(vol):
    if not (0.0  <= vol <= dyn_range):
        print(f"напряжение выходит за динамиеский диапазон ЦАП (0.00 - {dyn_range:.2f} В)")
        print("Устанавливаем 0.0 В") 
        return 0
    return int(vol / dyn_range * 255)

def num2dac(num):
    GPIO.output(leds, [int(element) for element in bin(num)[2:].zfill(8)])


try:
    while True:
        try:
            vol = float(input("введите напряжение в вольтах: "))
            num = vol2num(vol)
            num2dac(num)
        except ValueError:
            print("вы ввели не число. трай эгэин")


except KeyboardInterrupt:
    print("key pressed, finished working")

finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()

    #ограничить подачу питания погасить сетодиоды

    #gpio cleanup
    print("sth important")
