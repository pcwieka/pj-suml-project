all: build up

build:
	docker-compose -f docker/docker-compose.yml build --no-cache

build-kedro:
	docker-compose -f docker/docker-compose.yml build --no-cache kedro

build-api:
	docker-compose -f docker/docker-compose.yml build --no-cache api

build-model:
	docker-compose -f docker/docker-compose.yml build --no-cache model

build-ui:
	docker-compose -f docker/docker-compose.yml build  --no-cache ui

up:
	docker-compose -f docker/docker-compose.yml up -d

kedro-run:
	docker-compose -f docker/docker-compose.yml exec kedro kedro run

down:
	docker-compose -f docker/docker-compose.yml down

clean-model:
	docker-compose -f docker/docker-compose.yml exec model rm -f /model/champion_model.pkl /model/champion_metrics.pkl

.PHONY: build build-kedro build-api build-model build-ui up kedro-run down clean-model all
