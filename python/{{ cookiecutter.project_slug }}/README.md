# {{ cookiecutter.project_name }} - Example readme

- Install for use: `poetry install --without dev --sync`
    - Install from package: `python -m pip install <package-name.whl>`
- Install for development: `poetry install --sync`
    - Run test: `poetry run python -m pytest`
    - Run typecheck: `poetry run python -m mypy`
    - Create package: `poetry build`
    - Create offline-install package: `./tools/create-offline-package.sh`


## Example run

- Example app run: `poetry run python -m {{ cookiecutter.package_name }} 5 3`


## Troubleshooting

### `Poetry was unable to find a compatible python version.`

If you have one, you can explicitly use it via the "env use" command or install an appropriate python version and create a virtual environment:

```bash
py -3 -m venv .venv
poetry install
```


## Glossary

A
: b

C
: D
