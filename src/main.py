from blinkt import set_pixel, set_brightness, show, clear
import time
import docker

# reset gpio
set_brightness(0.1)
clear()

# initialize docker-client
client = docker.from_env()
print(client.containers.list())


set_pixel(1, 255, 255, 255)
show()

while(True):
    time.sleep(1)
