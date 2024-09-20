from machine import Pin
import utime

led = Pin(16, Pin.OUT)
led.value(0)

def toggle_led(led):
    led.value(led.value() ^ 1)

while True:
    toggle_led(led)
    utime.sleep(1)
