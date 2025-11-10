# Makefile for project needs
# Author: Ben Trachtenberg/Blaze Bryant
# Version: 3.0.0
#
PROJECT = portfolio_project
APP = portfolio_app
DOCKER_HUB = naturalblaze


.PHONY: all info build build-container coverage format pylint pytest gh-pages build dev-run start-container \
	stop-container remove-container check-vuln check-security pip-export

info:
	@echo "make options"
	@echo "  Build, Coverage, Test, and Security"
	@echo "    all                 To run format, pylint, check-security, coverage, pip-export, check-vuln"
	@echo "    build               To build a distribution"
	@echo "    check-security      To check for vulnerabilities in the code"
	@echo "    check-vuln          To check for vulnerabilities in the dependencies"
	@echo "    coverage            To run coverage and display ASCII and output to htmlcov"
	@echo "    format              To format the code with black"
	@echo "    gh-pages            To create the GitHub pages"
	@echo "    pip-export          To export the requirements to requirements.txt, requirements-dev.txt, and requirements-prod.txt"
	@echo "    pylint              To run pylint"
	@echo "    pytest              To run pytest with verbose option"
	@echo "    ruff-format         To run ruff formatter"
	@echo "    ruff-lint           To run ruff linter"
	@echo "  Django Commands and Dev Server"
	@echo "    createsuperuser     To create superuser in django db"
	@echo "    dev-run             To run the app dev server"
	@echo "  Docker Containers"
	@echo "    container-build     To build the containers"
	@echo "    container-start     To start the containers"
	@echo "    container-stop      To stop the containers"
	@echo "    container-remove    To remove the containers"
	@echo "    container-publish   To publish the django container to Docker Hub"


all: format pylint check-security coverage pip-export check-vuln

build:
	@uv build --wheel --sdist

check-security:
	@uv run bandit -c pyproject.toml -r .

check-vuln:
	@uv run pip-audit -r requirements.txt
	@uv run pip-audit -r requirements-dev.txt
	@uv run pip-audit -r requirements-prod.txt

coverage:
	@uv run pytest --cov --cov-report=html -vvv

format:
	@uv run black $(PROJECT)/
	@uv run black $(APP)/
	@uv run black tests/
	@uv run black scripts/

gh-pages:
	@rm -rf ./docs/source/code
	@uv run sphinx-apidoc -o ./docs/source/code ./$(PROJECT)
	@uv run sphinx-apidoc -o ./docs/source/code ./$(APP)
	@uv run sphinx-build ./docs ./docs/gh-pages

pip-export:
	@uv export --no-dev --no-group prod --no-emit-project --no-editable > requirements.txt
	@uv export --no-group prod --no-emit-project --no-editable > requirements-dev.txt
	@uv export --no-dev --group prod --no-emit-project --no-editable > requirements-prod.txt

pylint:
	@uv run pylint $(PROJECT)/
	@uv run pylint $(APP)/

pytest:
	@uv run pytest --cov -vvv

ruff-format:
	@uv run ruff format $(PROJECT)/
	@uv run ruff format $(APP)/
	@uv run ruff format tests/
	@uv run ruff format scripts/

ruff-lint:
	@uv run ruff check $(PROJECT)/
	@uv run ruff check $(APP)/

createsuperuser:
	@uv run python manage.py createsuperuser

dev-run:
	@uv run python manage.py runserver

container-build:
	@uv run docker compose --env-file .env.docker up -d --build

container-start:
	@uv run docker compose start

container-createsuperuser:
	@uv run docker exec -it django-portfolio python manage.py createsuperuser

container-stop:
	@uv run docker compose stop

container-remove:
	@uv run docker compose down -v

container-publish:
	@uv run docker tag django-portfolio ${DOCKER_HUB}/django-portfolio:latest
	@uv run docker push ${DOCKER_HUB}/django-portfolio
