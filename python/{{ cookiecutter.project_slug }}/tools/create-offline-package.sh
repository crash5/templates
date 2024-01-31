#!/usr/bin/env bash

set -Eeuo pipefail

declare -r OUTPUT_DIR="./release"
declare -r SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd -P)

mkdir -p "${OUTPUT_DIR}"

poetry build --format=wheel
poetry export --only=main --without-hashes -o "${OUTPUT_DIR}"/requirements.txt
# FIXME(username): when using internal repo add username to the internal repo url in the requirements.txt file (https://username@pkgs...)
# read -p "Press enter to continue after added username to the internal url in requirements.txt eg: https://username@pkgs..."
poetry run python -m pip download --requirement "${OUTPUT_DIR}"/requirements.txt --only-binary=:all: --dest "${OUTPUT_DIR}"/packages
# running from CI maybe needs to specify platform and version: --platform win_amd64 --python-version 38

cp ./dist/{{ cookiecutter.package_name }}*.whl "${OUTPUT_DIR}"/

cat << EOF > "${OUTPUT_DIR}"/install-user.cmd
python -m pip install --user --no-index --find-links ./packages -r requirements.txt
python -m pip install --user --no-index --no-dependencies --force-reinstall --find-links . {{ cookiecutter.package_name }}

@echo off
pause
EOF

cat << EOF > "${OUTPUT_DIR}"/install-system.cmd
SET script_path=%~dp0
cd %script_path%

python -m pip install --no-index --find-links ./packages -r requirements.txt
python -m pip install --no-index --no-dependencies --force-reinstall --find-links . {{ cookiecutter.package_name }}

@echo off
pause
EOF

cat << EOF > "${OUTPUT_DIR}"/install-virtualenv.cmd
python -m venv .venv

.\.venv\Scripts\python.exe -m pip install --no-index --find-links ./packages -r requirements.txt
.\.venv\Scripts\python.exe -m pip install --no-index --no-dependencies --force-reinstall --find-links . {{ cookiecutter.package_name }}

@echo off
pause
EOF

cat << EOF > "${OUTPUT_DIR}"/start-virtualenv.cmd
start .\.venv\Scripts\activate.bat
EOF


cat << 'EOF' > "${OUTPUT_DIR}"/README.md.txt
# {{ cookiecutter.project_name }} OnDemand Desktop (ODD) install package

## Install

**The recommended installation method is the virtual environment.**

You can install it in different ways:
- **Install inside a new virtual environment** (virtual environment created automatically in the .venv/ directory): `install-virtualenv.cmd`
- Install system wide: `install-system.cmd`
- Install only for the current user: `install-user.cmd`


## Usage

### In virtual environment

If you installed the app into a virtual environment you can open a command prompt into the virtual environment with `start-virtualenv.cmd` and use the command from the [Other install methods](#other-install-methods) section. Or you can run directly with the command `.\.venv\Scripts\python.exe -m {{ cookiecutter.package_name }} -h` without opening command prompt to the virtual environment.


### Other install methods

After installation you can test it with the command `python -m {{ cookiecutter.package_name }} -h` which shows the command line help message.
EOF
