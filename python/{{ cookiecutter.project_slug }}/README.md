# {{ cookiecutter.project_name }} - Example readme

- Install for use: `poetry install --without dev --sync`
- Run app: `poetry run python -m {{ cookiecutter.package_name }} 5 3`
- Install for development: `poetry install --sync`
    - Run test: `poetry run python -m pytest`
    - Run typecheck: `poetry run python -m mypy src/ --pretty`


## Troubleshooting

### `Poetry was unable to find a compatible python version.`

If you have one, you can explicitly use it via the "env use" command or install an appropriate python version and create a virtual environment:

```bash
py -3 -m venv .venv
poetry install
```
