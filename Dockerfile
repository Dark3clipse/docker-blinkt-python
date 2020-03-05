FROM python:3.8.2-buster
MAINTAINER Sophia Hadash

# copy contents
WORKDIR /usr/src/app
ADD src ./src
ADD requirements.txt .

# add user
RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 111 ubuntu
USER ubuntu

# install packages
#RUN sudo pip3 install blinkt
RUN pip3 install -r requirements.txt

CMD ["python3", "src/main.py"]
