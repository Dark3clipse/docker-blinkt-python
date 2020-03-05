from blinkt import set_pixel, set_brightness, show, clear
import time

set_brightness(0.1)
clear()
set_pixel(1, 255, 255, 255)
show()

while(True):
    time.sleep(1);
