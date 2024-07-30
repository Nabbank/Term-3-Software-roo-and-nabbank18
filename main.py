from machine import *
from time import time

LED = Pin(25, Pin.OUT)

servos = []

for i in range(6):
    servos.append(PWM(Pin(i)))

while True:
    sysTime = time()
    if sysTime % 2:
        LED.on()
    else:
        LED.off()
    for i in servos:
        
        i.freq(50)
        i.duty_ns(1500000)
