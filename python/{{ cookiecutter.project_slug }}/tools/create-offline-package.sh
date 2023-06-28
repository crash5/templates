#!/usr/bin/env bash

set -Eeuo pipefail

declare -r OUTPUT_DIR="./release"
declare -r SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd -P)

mkdir -p "${OUTPUT_DIR}"

poetry build --format=wheel
poetry export --only=main --without-hashes --without-urls -o "${OUTPUT_DIR}"/requirements.txt
poetry run python -m pip download --requirement "${OUTPUT_DIR}"/requirements.txt --only-binary=:all: --dest "${OUTPUT_DIR}"/packages
# running from CI maybe needs to specify platform and version
# poetry run python -m pip download --requirement "${OUTPUT_DIR}"/requirements.txt --only-binary=:all: --platform win_amd64 --python-version 38 --dest "${OUTPUT_DIR}"/packages

cp ./dist/{{ cookiecutter.package_name }}*.whl "${OUTPUT_DIR}"/

cat << EOF > "${OUTPUT_DIR}"/install-user.cmd
python -m pip install --user --no-index --find-links ./packages -r requirements.txt
python -m pip install --user --no-index --no-dependencies --force-reinstall --find-links . {{ cookiecutter.package_name }}

@echo off

if %ERRORLEVEL% EQU 0 (
   echo Package installed successfully: {{ cookiecutter.package_name }}
) else (
   echo Could not properly install the package: {{ cookiecutter.package_name }}
   exit /b %errorlevel%
)
EOF
