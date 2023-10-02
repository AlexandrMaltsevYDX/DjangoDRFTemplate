# ============================================VARIABLES===========================================
docker_dir = docker
docker_v2 = docker compose



main_container = -f docker-compose.dev.yml
backend_container = -f $(docker_dir)/backend/dockercompose_file/back.dev.yml
postgres_container = -f $(docker_dir)/postgres/dockercompose_file/postgres.dev.yml
nginx_container = -f $(docker_dir)/nginx/dockercompose_file/nginx.dev.yml
frontend_container = -f $(docker_dir)/frontend/dockercompose_file/front.dev.yml

compose_application := $(docker_v2) $(main_container) $(postgres_container) $(backend_container) $(nginx_container) $(frontend_container)


# ===================================DOCKER(MANAGE APPLICATION)===================================

.PHONY: build
build:
	$(compose_application) build

.PHONY: up
up:
	$(compose_application) up

.PHONY: down
down:
	$(compose_application) down

.PHONY: prune
prune:
	docker system prune --all --force --volumes
