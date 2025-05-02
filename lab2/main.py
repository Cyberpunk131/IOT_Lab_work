from machine import pin 
from time import sleep

btn = Pin(0, Pin.IN, Pin.PULL_UP)

while True:

    sleep(.4)
    print(btn.value())