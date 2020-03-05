bin/docker-blinkt-python: src/main.py
	docker build -t docker-blinkt:latest .
	mkdir -p bin
	"docker run docker-blinkt:latest" > bin/docker-blinkt-python
