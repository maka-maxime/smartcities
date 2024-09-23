from machine import Pin, Timer
import utime

reference_ticks = 0
event_ticks = 0
DELTA_T = 200

led = Pin(16, Pin.OUT)
led.value(0)

timer = Timer(-1)
periods = [2000, 200, 100, 50]
STATES = len(periods)+1

def update_animation(led, state):
    HALF_T = 200
    utime.sleep_ms(2*HALF_T)
    for i in range(state):
        led.toggle()
        utime.sleep_ms(HALF_T)
        led.toggle()
        utime.sleep_ms(HALF_T)
    utime.sleep_ms(2*HALF_T)

button_state = 0
def button_handler(pin):
    button.irq(handler=None)
    global button_state
    global reference_ticks
    global event_ticks
    global timer
    event_ticks = utime.ticks_ms()
    print(f"ref: {reference_ticks}, evt:{event_ticks}")
    if event_ticks - reference_ticks > DELTA_T:
        timer.deinit()
        led.value(0)
        reference_ticks = event_ticks
        event_ticks = utime.ticks_ms()
        button_state = (button_state + 1) % STATES
        if button_state is not 0:
            update_animation(led, button_state)
            timer.init(period=periods[button_state-1],mode=Timer.PERIODIC,callback=lambda t:led.toggle())
            led.value(1)
    button.irq(trigger=Pin.IRQ_RISING, handler=button_handler)

button = Pin(18, Pin.IN, Pin.PULL_DOWN)
button.irq(trigger=Pin.IRQ_RISING, handler=button_handler)

while True:
    utime.sleep_us(100)