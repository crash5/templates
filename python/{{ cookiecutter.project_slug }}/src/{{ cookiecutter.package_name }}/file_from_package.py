import importlib.resources as pkg_resources
from importlib import import_module


def _read_text(package: str, filename: str) -> str:
    pkg = import_module(package)
    try:
        # from python 3.9
        in_file = pkg_resources.files(pkg).joinpath(filename)
        with in_file.open("r") as f:
            template = f.read()
    except AttributeError:
        # Python < PY3.9, fall back to method deprecated in PY3.11.
        template = pkg_resources.read_text(pkg, filename)
    return template


def read_text(name: str) -> str:
    return _read_text("{{ cookiecutter.package_name }}.fix_input", name)
