from machine import Pin, Timer

led = Pin(16, Pin.OUT)
led.value(0)

def toggle_led(t):
    global led
    global count
    led.value(led.value() ^ 1)
    count += 1

timer = Timer(-1)
periods = [2000, 500]
state = 0
count = 0
    
timer.init(period=periods[state],mode=Timer.PERIODIC,callback=toggle_led)

while True:
    if count == 6:
        timer.deinit()
        count = 0
        state = (state + 1) % 2
        timer.init(period=periods[state],mode=Timer.PERIODIC,callback=toggle_led)
