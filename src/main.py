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

    # create list of running containers
    a = []
    for container in client.containers.list():
        a.append(container.attrs['Config']['Image'].split('@')[0])

    # link LEDS 0 to 4 to docker images
    if "angelnu/glusterfs:latest" in a:
        set_pixel(0, 0, 0, 255)
    else:
        set_pixel(0, 0, 0, 0)

    if "shadash/docker-multiarch-jenkins:latest" in a:
        set_pixel(1, 255, 255, 0)
    else:
        set_pixel(1, 0, 0, 0)

    if "registry:2" in a:
        set_pixel(2, 255, 255, 255)
    else:
        set_pixel(2, 0, 0, 0)

    if "shadash/docker-multiarch-visualizer:v1" in a:
        set_pixel(3, 128, 0, 255)
    else:
        set_pixel(3, 0, 0, 0)

    if "nginx:latest" in a:
        set_pixel(4, 255, 0, 255)
    else:
        set_pixel(4, 0, 0, 0)

    # disk usage green (0%) to red (100%) on LED 5
    disku = int((psutil.disk_usage('/dev/sda1').percent/100)*255)
    set_pixel(5, disku, 255 - disku, 0)

    # RAM usage green (0%) to red (100%) on LED 6
    mem = psutil.virtual_memory()
    memu = int((mem.percent/100)*255)
    set_pixel(6, memu, 255 - memu, 0)

    # cpu usage green (0%) to red (100%) on LED 7
    cpu=int(psutil.cpu_percent()*255)
    set_pixel(7, cpu, 255-cpu, 0)

    show()
    time.sleep(0.33)
