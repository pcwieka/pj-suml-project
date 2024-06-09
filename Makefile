all: build up

build:
	docker-compose -f docker/docker-compose.yml build --no-cache

build-kedro:
	docker-compose -f docker/docker-compose.yml build --no-cache kedro

build-api:
	docker-compose -f docker/docker-compose.yml build --no-cache api

build-model:
	docker-compose -f docker/docker-compose.yml build --no-cache model

up:
	docker-compose -f docker/docker-compose.yml up -d

kedro-run:
	docker-compose -f docker/docker-compose.yml exec kedro kedro run

down:
	docker-compose -f docker/docker-compose.yml down

.PHONY: build up kedro-run down all
