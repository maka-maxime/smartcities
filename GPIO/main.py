from machine import Pin, Timer

led = Pin(16, Pin.OUT)
led.value(0)

def toggle_led(t):
    global led
    global count
    led.toggle()
    count += 1

timer = Timer(-1)
periods = [2000, 500]
state = 0
count = 0

button_state = 0
mutex_button = 0
def button_handler(pin):
    button.irq(handler=None)
    global mutex_button
    global button_state
    if button.value() == 1 and mutex_button == 0:
        mutex_button = 1
        button_state = (button_state + 1) % 3
        print(f"{button_state}")
    elif button.value() == 0 and mutex_button == 1:
        mutex_button = 0
    button.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=button_handler)

button = Pin(18, Pin.IN, Pin.PULL_DOWN)
button.irq(trigger=Pin.IRQ_RISING, handler=button_handler)

timer.init(period=periods[state],mode=Timer.PERIODIC,callback=toggle_led)

while True:
    if count == 6:
        timer.deinit()
        count = 0
        state = (state + 1) % 2
        timer.init(period=periods[state],mode=Timer.PERIODIC,callback=toggle_led)
