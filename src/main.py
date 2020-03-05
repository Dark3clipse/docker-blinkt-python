from blinkt import set_pixel, set_brightness, show, clear
import time
import docker

# reset gpio
set_brightness(0.1)
clear()

# initialize docker-client
client = docker.from_env()

# visualize active containers
while(True):
    for container in client.containers.list():
        if container.attrs['Config']['Image']=="angelnu/glusterfs:latest":
            set_pixel(0, 255, 255, 255)
        elif container.attrs['Config']['Image']=="shadash/docker-multiarch-jenkins:latest":
            set_pixel(1, 255, 255, 255)
        elif container.attrs['Config']['Image']=="registry:2":
            set_pixel(2, 255, 255, 255)
        elif container.attrs['Config']['Image']=="shadash/docker-multiarch-visualizer:v1":
            set_pixel(3, 255, 255, 255)
        elif container.attrs['Config']['Image']=="nginx:latest":
            set_pixel(4, 255, 255, 255)
    set_pixel(5, 0, 255, 0)
    show()
    time.sleep(0.5)
