WANDB_API_KEY ?= 11c33fa7a54c9982602f7bd5f5ccdd66beb31ca6

all: build up

build:
	WANDB_API_KEY=$(WANDB_API_KEY) docker-compose -f docker/docker-compose.yml build --no-cache

build-kedro:
	WANDB_API_KEY=$(WANDB_API_KEY) docker-compose -f docker/docker-compose.yml build --no-cache kedro

build-api:
	WANDB_API_KEY=$(WANDB_API_KEY) docker-compose -f docker/docker-compose.yml build --no-cache api

build-model:
	WANDB_API_KEY=$(WANDB_API_KEY) docker-compose -f docker/docker-compose.yml build --no-cache model

up:
	WANDB_API_KEY=$(WANDB_API_KEY) docker-compose -f docker/docker-compose.yml up -d

kedro-run:
	docker-compose -f docker/docker-compose.yml exec kedro kedro run

down:
	docker-compose -f docker/docker-compose.yml down

.PHONY: build up kedro-run down all
