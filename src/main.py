from blinkt import set_pixel, set_brightness, show, clear
import time
import docker
import psutil

# reset gpio
set_brightness(0.1)
clear()

# initialize docker-client
client = docker.from_env()

# visualize active containers
while(True):
    for container in client.containers.list():
        if container.attrs['Config']['Image']=="angelnu/glusterfs:latest":
            set_pixel(0, 0, 0, 255)
        if container.attrs['Config']['Image']=="shadash/docker-multiarch-jenkins:latest":
            set_pixel(1, 255, 255, 0)
        if container.attrs['Config']['Image']=="registry:2":
            set_pixel(2, 255, 255, 255)
        if container.attrs['Config']['Image']=="shadash/docker-multiarch-visualizer:v1":
            set_pixel(3, 128, 0, 255)
        if container.attrs['Config']['Image']=="nginx:latest":
            set_pixel(4, 255, 0, 255)

    # green on LED 5 (debug)
    set_pixel(5, 0, 255, 0)

    # cpu usage green (0%) to red (100%) on LED 7
    cpu=int(psutil.cpu_percent()*255)
    set_pixel(7, cpu, 255-cpu, 0)

    show()
    time.sleep(0.5)
