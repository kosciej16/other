COMPOSE_FLAGS=-f docker-compose.yml
LOCAL_COMPOSE_FLAGS = ${COMPOSE_FLAGS} -f docker-compose_x.yml

b:
	docker-compose ${LOCAL_COMPOSE_FLAGS} build playground

r:
	docker-compose ${LOCAL_COMPOSE_FLAGS} run playground env
