# Makefile para StravaScraper

# Levanta el contenedor con FastAPI
up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

shell:
	docker exec -it strava_api bash

# Ejecuta el CLI desde dentro del contenedor
# Ejemplo: make cli NAME=juan EXPORT=true
cli:
	docker exec -it strava_api python -m cli $(if $(NAME),--name $(NAME)) $(if $(IDS),--ids $(IDS)) $(if $(EXPORT),--export)
