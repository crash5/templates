#!/usr/bin/env bash

set -Eeuo pipefail

poetry dynamic-versioning

declare -r OUTPUT_DIR="./dist-manual"

mkdir -p "${OUTPUT_DIR}"

cp -r "src/." "${OUTPUT_DIR}"

# TODO: add required packages manually

# Polars
# cp -r ".venv/Lib/site-packages/polars" "${OUTPUT_DIR}"
# cp -r ".venv/Lib/site-packages/_polars_runtime_32" "${OUTPUT_DIR}"
# cp -r ".venv/Lib/site-packages/openpyxl" "${OUTPUT_DIR}"

find "${OUTPUT_DIR}" -type d -name '__pycache__' -exec rm -rf {} +

echo "Files copied to: ${OUTPUT_DIR}"
