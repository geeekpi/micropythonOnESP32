import time
from machine import Pin

p0 = Pin(0, Pin.OUT)
state = 0
for i in range(0, 15):
    p0.value(state)
    state = 1 - state
    time.sleep(1)
