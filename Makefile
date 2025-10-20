# Makefile for project needs
# Author: Ben Trachtenberg/Blaze Bryant
# Version: 3.0.0
#
PROJECT = portfolio_project
APP = portfolio_blog

.PHONY: all info build build-container coverage format pylint pytest gh-pages build dev-run start-container \
	stop-container remove-container check-vuln check-security pip-export

info:
	@echo "make options"
	@echo "    all                 To run coverage, format, pylint, and check-vuln"
	@echo "    build               To build a distribution"
	@echo "    build-container     To build a container image"
	@echo "    check-vuln          To check for vulnerabilities in the dependencies"
	@echo "    check-security      To check for vulnerabilities in the code"
	@echo "    coverage            To run coverage and display ASCII and output to htmlcov"
	@echo "    dev-run             To run the app"
	@echo "    format              To format the code with black"
	@echo "    pylint              To run pylint"
	@echo "    pytest              To run pytest with verbose option"
	@echo "    ruff-format         To run ruff formatter"
	@echo "    ruff-lint           To run ruff linter"
	@echo "    start-container     To start the container"
	@echo "    stop-container      To stop the container"
	@echo "    remove-container    To remove the container"
	@echo "    pip-export          To export the requirements to requirements.txt and requirements-dev.txt"
	@echo "    gh-pages           To create the GitHub pages"


all: format pylint coverage check-security pip-export

build:
	@uv build --wheel --sdist

coverage:
	@uv run pytest --cov --cov-report=html -vvv

format:
	@uv run black $(PROJECT)/
	@uv run black $(APP)/
	@uv run black tests/
	@uv run black scripts/

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

check-security:
	@uv run bandit -c pyproject.toml -r .

pip-export:
	@uv export --no-dev --no-group prod --no-emit-project --no-editable > requirements.txt
	@uv export --no-group prod --no-emit-project --no-editable > requirements-dev.txt
	@uv export --no-dev --group prod --no-emit-project --no-editable > requirements-prod.txt

gh-pages:
	@rm -rf ./docs/source/code
	@uv run sphinx-apidoc -o ./docs/source/code ./$(PROJECT)
	@uv run sphinx-apidoc -o ./docs/source/code ./$(APP)
	@uv run sphinx-build ./docs ./docs/gh-pages

create-superuser:
	@uv run python manage.py createsuperuser

dev-run:
	@uv run python manage.py runserver

build-container:
	@uv run docker compose --env-file .env.prod up -d --build

start-container:
	@uv run docker compose start

superuser-container:
	@uv run docker exec -it django-portfolio python manage.py createsuperuser

stop-container:
	@uv run docker compose stop

remove-container:
	@uv run docker compose down -v
