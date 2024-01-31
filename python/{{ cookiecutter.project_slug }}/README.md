# {{ cookiecutter.project_name }} - Example readme

## Project links

- https://REPOSITORY/{{ cookiecutter.package_name }}.git


## External system usage

- Azure Blob Storage

## Quick Start

...

## Basic commands to manage project

General Commands:
- Install with Pip from package (recommended to do it in a virtual environment)
    1. Create a virtualenv: `python -m venv .venv`
    2. Activate virtualenv: `source .venv/Scripts/activate`
    3. Install: `python -m pip install {{ cookiecutter.package_name }}`

- Install with Poetry: `poetry install --without dev --sync`


## Example run

- Show command-line help: `poetry run python -m {{ cookiecutter.package_name }} -h`
- Example app run: `poetry run python -m {{ cookiecutter.package_name }} 5 3`


## For development

Install [poetry](https://python-poetry.org/docs/#installation) and [poetry dynamic versioning](https://github.com/mtkennerly/poetry-dynamic-versioning) package.

```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
poetry self add "poetry-dynamic-versioning[plugin]"
```

General Commands:
- Install: `poetry install --sync`
- Create package: `poetry build`
- Create offline-install package into 'release' directory: `./tools/create-offline-package.sh`
- Run test: `poetry run python -m pytest`
    - Run test and generate html coverage report: `poetry run python -m pytest --cov=src --cov-report term --cov-report html`
- Run mypy typecheck: `poetry run python -m mypy`
- Run flake8 style check: `poetry run python -m flake8 ./src`


## Troubleshooting

### `Poetry was unable to find a compatible python version.`

If you have one, you can explicitly use it via the "env use" command or install an appropriate python version and create a virtual environment:

```bash
py -{{ cookiecutter.python_version }} -m venv .venv
poetry install --sync
```


## Additional links

- https://www.python.org/
- https://python-poetry.org/
- https://github.com/mtkennerly/poetry-dynamic-versioning

## Glossary

A
: b

C
: D
