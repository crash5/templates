#!/usr/bin/env bash

set -Eeuo pipefail

poetry-dynamic-versioning

declare -r OUTPUT_DIR="./dist-manual"

mkdir -p "${OUTPUT_DIR}"

cp -r "src/." "${OUTPUT_DIR}"
# TODO: add required packages manually
# cp -r ".venv/Lib/site-packages/polars" "${OUTPUT_DIR}"

find "${OUTPUT_DIR}" -type d -name '__pycache__' -exec rm -rf {} +
