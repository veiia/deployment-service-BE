.SILENT:

pythonpath := $(PWD)
pythonpath := $(pythonpath):$(PWD)/tests
pythonpath := $(pythonpath):$(PWD)/app

run:
	docker-compose up -d deployment-service

run-build:
	 docker-compose up --build -d deployment-service

build:
	docker-compose build deployment-service

test:
	PYTHONPATH=$(pythonpath) pytest tests

test-coverage:
	...

stop:
	...

install-dev:
	pip3 install -r ./requirements/dev.txt

install-test:
	pip3 install -r ./requirements/test.txt