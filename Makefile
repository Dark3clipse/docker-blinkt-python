bin/docker-blinkt-python: src/main.py
	docker build -t shadash/docker-blinkt:latest .
	mkdir -p bin
	echo "docker run shadash/docker-blinkt:latest" > bin/docker-blinkt-python
