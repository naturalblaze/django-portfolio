# django-portfolio

| Branch | Tests |
| ------ | ----- |
| develop | [![Unit-Testing, Coverage, Linting](https://github.com/naturalblaze/django-portfolio/actions/workflows/test-coverage-lint-uv.yml/badge.svg?branch=develop)](https://github.com/naturalblaze/django-portfolio/actions/workflows/test-coverage-lint-uv.yml) |
| main | [![Unit-Testing, Coverage, Linting](https://github.com/naturalblaze/django-portfolio/actions/workflows/test-coverage-lint-uv.yml/badge.svg)](https://github.com/naturalblaze/django-portfolio/actions/workflows/test-coverage-lint-uv.yml) |

## Description

Python project that uses the Django framework to create a portfolio website. 

**Features:**

* A custom Wordcloud image built for your profession using the `DJANGO_WORDCLOUD` environment variable and your Resume skills.

* Resume, Projects, and About Me pages built from models in the Django database. Models support Markdown formatting and emojis and raw html to add some style.

* Fully customizable for different users and professions.

* Static files (`static` directory)

    * css/main.css: CSS formatting for website templates

    * fonts/: Custom font files

    * portfolio_app/about/: About webpage default images

    * portfolio_app/projects/: Project webpage default images

    * portfolio_app/favicon.png: Favorite, shortcut, website default icon

    * portfolio_app/icon.png: Navbar icon

* Easy to setup for local development and deployable to Docker containers or the cloud environment of your choosing.

### Django Portfolio Models

| Models | Keys | Description |
| ------ | ---- | ----------- |
| Portfolio | <ul><li>First Name</li><li>Last Name</li><li>Email `Optional`</li><li>Linkedin url `Optional`</li><li>Github url `Optional`</li><li>Portfolio img `Optional`</li><li>Introduction</li><li>Professional experience</li><li>Total visits `Default=0`</li></ul> | Portfolio personal information. Introduction and Professional experience accept regular text, markdown, and raw html formatting. |
| Projects | <ul><li>Title</li><li>Subtitle</li><li>Slug</li><li>Author</li><li>Content</li><li>Project img `Optional`</li><li>Status `Options:draft\|published`</li><li>Tags `Comma-separated`</li></ul> | Projects highlighting professional experience and accomplishments. Content  accept regular text, markdown, and raw html formatting. |
| Resume Certifications | <ul><li>Name</li><li>Issuing Organization</li><li>Issue date</li><li>Credential id `Optional`</li><li>Credential url `Optional`</li><li>Credential img `Optional`</li></ul> | Professional certifications for Resume page. |
| Resume Education | <ul><li>Institution</li><li>Degree</li><li>Field of study</li><li>Start date</li><li>End date `Date or Current`</li></ul> | Educational experience for Resume page. |
| Resume Jobs | <ul><li>Company</li><li>Role</li><li>Description</li><li>Projects</li><li>Start date</li><li>End date `Date or Current`</li></ul> | Professional work experience for Resume page. Description and Projects accept regular text, markdown, and raw html formatting. |
| Resume Skills | <ul><li>Name</li><li>Proficiency `Options:1 to 10`</li><li>Skill img `Optional`</li><li>Tags `Comma-separated`</li></ul> | Professional skills for Resume page. |

## Setup Project and test server with `UV`

* [Install uv](https://docs.astral.sh/uv/getting-started/installation/)

* Create Python Virtual Environment

```bash
uv venv
```

* Activate `venv`

```bash
source .venv/bin/activate
```

* Install requirement libraries

```bash
uv sync
```

* Environment variables `.env.local`

```text
# Development environment variables
DJANGO_ENV=local
DJANGO_DEBUG=True
DJANGO_WORDCLOUD=DEVOPS
DJANGO_SECRET_KEY=super-secret-dev-key
DJANGO_ALLOWED_HOSTS=localhost,0.0.0.0,127.0.0.1
DJANGO_DATABASE_URL=sqlite:///db.sqlite3
```

* Create a superuser account

```bash
make create-superuser
```

* Test starting the server

```bash
make dev-run
```

* Test server is running: [Django Local Server](http://127.0.0.1:8000/)

> [!NOTE]
> You will need to create `Portfolio` model before the `About Me` page will load because it relies on the `Total visits` attribute to exist
> [Django Local Admin Server](http://127.0.0.1:8000/admin/)

## Environment Variables

Two environment variables files are supported for local development `.env.local` and production deployment `.env.prod`

| Name | Environments | Default Value | Description |
| ---- | ------------ | ------------- | ----------- |
| DJANGO_ENV | All | local | Django Environment `local` or `prod` |
| DJANGO_SECRET_KEY | All | None | Django Secret Key used for cryptographic signing|
| DJANGO_DEBUG | All | False | Django debug mode |
| DJANGO_WORDCLOUD | All | DEVOPS | Text for Wordcloud image |
| DJANGO_ALLOWED_HOSTS | All | [] | A list of strings representing the host/domain names that this Django site can serve. |
| DJANGO_DATABASE_URL | All | sqlite:///db.sqlite3 | Database URL |
| DJANGO_CSRF_TRUSTED_ORIGINS | Prod | [http://localhost:8000] | A list of trusted origins for unsafe requests |
| POSTGRES_DB | Prod | None | Postgres database name that is used to to craft `DJANGO_DATABASE_URL` in docker-compose.yaml |
| POSTGRES_USER | Prod | None | Postgres database username that is used to to craft `DJANGO_DATABASE_URL` in docker-compose.yaml |
| POSTGRES_PASSWORD | Prod | None | Postgres database password that is used to to craft `DJANGO_DATABASE_URL` in docker-compose.yaml |
| POSTGRES_HOST | Prod | None | Postgres database hostname that is used to to craft `DJANGO_DATABASE_URL` in docker-compose.yaml |
| POSTGRES_PORT | Prod | None | Postgres database port that is used to to craft `DJANGO_DATABASE_URL` in docker-compose.yaml |

> [!NOTE]
> Depending on the database used for the backend you can either provide the `DJANGO_DATABASE_URL` in the environment file or use variables in your `docker-compose.yml` to build the URL if you were to need those variables for the database container. 
> ```
> Postgres Example: DJANGO_DATABASE_URL=postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}
> ```

## Populate data with projects (defaults to 20 with no `script-args`)

```bash
python manage.py runscript populate_projects --script-args="100"
```

## GitHub Actions

* `test-coverage-lint-uv.yaml`
    * Runs on push and pull requests to the `main\|develop\|feature\|bug` branches
    * Python matrix testing on versions 3.11 thru 3.13 with `uv` package manager on Linux, Windows, and Mac OS.
    * Jobs: linting, unit-tests and coverage, security scanning, and application build

---

### Generated by CookieCutter

* Repository: [GitHub](https://github.com/naturalblaze/cookiecutter-python-django)
* Version: 1.0.0
