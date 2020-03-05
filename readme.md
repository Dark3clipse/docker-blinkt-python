# Blinkt for Docker servers

This package enables a Docker node running on a Raspberry Pi with Blinkt hardware to show it's status using the Blinkt LEDs.

## Installation

Just clone and build.

```
git clone https://github.com/SophiaHadash/docker-blinkt-python
make
```

## Usage

You can run the container manually using the generated binary.
```
bash bin/docker-blinkt-python
```

Or you can deploy the image as a service
```
docker-compose -f docker-compose.yml -p docker-blinkt up -d
```

## Authors

* **Sophia Hadash** - *Initial work* - [SophiaHadash](https://github.com/SophiaHadash)
