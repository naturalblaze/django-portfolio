@ECHO OFF
REM Makefile for project needs
REM Author: Ben Trachtenberg/Blaze Bryant
REM Version: 3.0.0
REM

SET option=%1
SET PROJECT=portfolio_project
SET APP=portfolio_app
SET DOCKER_HUB=naturalblaze


IF "%option%" == "" (
    GOTO BAD_OPTIONS
)

IF "%option%" == "all" (
    uv run black %PROJECT%/
    uv run black %APP%/
    uv run black tests/
    uv run black scripts/
    uv run pylint %PROJECT%\
    uv run pylint %APP%\
    uv run pytest --cov --cov-report=html -vvv
    uv run bandit -c pyproject.toml -r .
    uv export --no-dev --no-group prod --no-emit-project --no-editable > requirements.txt
    uv export --no-group prod --no-emit-project --no-editable > requirements-dev.txt
    uv export --no-dev --group prod --no-emit-project --no-editable > requirements-prod.txt
    uv run pip-audit -r requirements.txt
    uv run pip-audit -r requirements-dev.txt
    uv run pip-audit -r requirements-prod.txt
    GOTO END
)

IF "%option%" == "build" (
    uv build --wheel --sdist
    GOTO END
)

IF "%option%" == "check-security" (
    uv run bandit -c pyproject.toml -r .
    GOTO END
)

IF "%option%" == "check-vuln" (
    uv run pip-audit -r requirements.txt
    uv run pip-audit -r requirements-dev.txt
    uv run pip-audit -r requirements-prod.txt
    GOTO END
)

IF "%option%" == "coverage" (
    uv run pytest --cov --cov-report=html -vvv
    GOTO END
)

IF "%option%" == "format" (
    uv run black %PROJECT%/
    uv run black %APP%/
    uv run black tests/
    uv run black scripts/
    GOTO END
)

IF "%option%" == "gh-pages" (
    rmdir /s /q docs\source\code
    uv run sphinx-apidoc -o ./docs/source/code ./%PROJECT%
    uv run sphinx-apidoc -o ./docs/source/code ./%APP%
    uv run sphinx-build ./docs ./docs/gh-pages
    GOTO END
)

IF "%option%" == "pip-export" (
    uv export --no-dev --no-group prod --no-emit-project --no-editable > requirements.txt
    uv export --no-group prod --no-emit-project --no-editable > requirements-dev.txt
    uv export --no-dev --group prod --no-emit-project --no-editable > requirements-prod.txt
    GOTO END
)

IF "%option%" == "pylint" (
    uv run pylint %PROJECT%\
    uv run pylint %APP%\
    GOTO END
)

IF "%option%" == "pytest" (
    uv run pytest --cov -vvv
    GOTO END
)

IF "%option%" == "createsuperuser" (
    uv run python manage.py createsuperuser
    GOTO END
)

IF "%option%" == "dev-run" (
    uv run python manage.py runserver
    GOTO END
)

:OPTIONS
@ECHO make options
@ECHO     all             To run format, pylint, check-security, coverage, pip-export, check-vuln
@ECHO     build           To build a distribution
@ECHO     check-vuln      To check for vulnerabilities in the dependencies
@ECHO     check-security  To check for vulnerabilities in the code
@ECHO     coverage        To run coverage and display ASCII and output to htmlcov
@ECHO     format          To format the code with black
@ECHO     gh-pages        To create the GitHub pages
@ECHO     pip-export      To export the requirements.txt, requirements-dev.txt, and requirements-prod.txt
@ECHO     pylint          To run pylint
@ECHO     pytest          To run pytest with verbose option
@ECHO     createsuperuser To create superuser in django db
@ECHO     dev-run         To run the app
GOTO END

:BAD_OPTIONS
@ECHO Argument is missing
@ECHO Usage: make.bat option
@ECHO.
GOTO OPTIONS

:END
