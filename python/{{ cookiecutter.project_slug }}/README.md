# {{ cookiecutter.project_name }} - Example readme

## Project links

- https://REPOSITORY/{{ cookiecutter.package_name }}.git


## External system usage

- Azure Blob Storage


## Basic commands to manage project

- Install for use: `poetry install --without dev --sync`
    - Install from package with pip: `python -m pip install <package-name.whl>`
- Install for development: `poetry install --sync`
    - Run test: `poetry run python -m pytest`
    - Run test and generate html coverage report: `poetry run python -m pytest --cov-report html`
    - Run typecheck: `poetry run python -m mypy`
    - Create package: `poetry build`
    - Create offline-install package: `./tools/create-offline-package.sh`


## Example run

- Example app run: `poetry run python -m {{ cookiecutter.package_name }} 5 3`


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

## Glossary

A
: b

C
: D
