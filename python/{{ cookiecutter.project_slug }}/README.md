# {{ cookiecutter.project_name }} _({{ cookiecutter.package_name }})_

TBD: Project brief descrioption


## Install

- From the repository with pip
```sh
python -m pip install {{ cookiecutter.package_name }}
```

- Locally from source with poetry
```sh
poetry install --without dev --sync
```


## Usage

- Show command-line help: `poetry run python -m {{ cookiecutter.package_name }} -h`

TBD: Other command-line and use-as-library example codes


## Contributing

Install [poetry](https://python-poetry.org/docs/#installation) and [poetry dynamic versioning](https://github.com/mtkennerly/poetry-dynamic-versioning) package.
```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
poetry self add "poetry-dynamic-versioning[plugin]"
```

General Commands:
- Install: `poetry install --sync`
- Create package: `poetry build`
- Create offline-install package into "release" directory: `./tools/create-offline-package.sh`
- Run test: `poetry run python -m pytest`
    - Run test and generate html coverage report: `poetry run python -m pytest --cov=src --cov-report term --cov-report html`
- Run mypy typecheck: `poetry run python -m mypy`
- Run flake8 style check: `poetry run python -m flake8 ./src`
- Run black code formatter: `poetry run black ./src`


## Additional links

TBD


## Definitions

TBD
