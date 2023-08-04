# {{ cookiecutter.project_name }} - Example readme

## Project links

- https://REPOSITORY/{{ cookiecutter.package_name }}.git


## External system usage

- Azure Blob Storage


## Basic commands to manage project

- Install for use
    - Poetry: `poetry install --without dev --sync`
    - Pip from package (recommended to do it in a virtual environment)
        1. Create a virtualenv: `python -m venv .venv`
        2. Activate virtualenv: `source .venv/Scripts/activate`
        3. Install: `python -m pip install <package-name.whl>`
- Install for development
    - Install: `poetry install --sync`
    - Create package: `poetry build`
    - Create offline-install package into 'release' directory: `./tools/create-offline-package.sh`
    - Run test: `poetry run python -m pytest`
        - Run test and generate html coverage report: `poetry run python -m pytest --cov=src --cov-report term --cov-report html`
    - Run mypy typecheck: `poetry run python -m mypy`
    - Run flake8 style check: `poetry run python -m flake8 ./src`


## Example run

- Example app run: `poetry run python -m {{ cookiecutter.package_name }} 5 3`


## Troubleshooting

### `Poetry was unable to find a compatible python version.`

If you have one, you can explicitly use it via the "env use" command or install an appropriate python version and create a virtual environment:

```bash
py -{{ cookiecutter.python_version }} -m venv .venv
poetry install --sync
```


### `The Poetry configuration is invalid: - [source.0] Additional properties are not allowed ('priority' was unexpected)`

Update poetry with one of these commands:
- `poetry self update`
- `(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -`
- `curl -sSL https://install.python-poetry.org | python -`


## Additional links

- https://www.python.org/
- https://python-poetry.org/

## Glossary

A
: b

C
: D
