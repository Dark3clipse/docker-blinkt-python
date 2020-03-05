bin/docker-blinkt-python: src/main.py
	docker build -t shadash/docker-blinkt:latest .
	mkdir -p bin
	echo "#!/bin/bash\ndocker run shadash/docker-blinkt:latest --privileged -v /var/run/docker.sock:/var/run/docker.sock" > bin/docker-blinkt-python
