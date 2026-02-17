#!/bin/bash

# boostrap project .venv with dependencies
# set -e prevents establishing a half-broken environment.
# deactivate 2>/dev/null || true exits current venv and handles state ambiguity.
# python3 -m venv .venv creates the python venv.
# source .venv/bin/activate enters a new venv.
# pip install -r requirements.txt reads the python dependencies into the venv.

set -e

deactivate 2>/dev/null || true
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

echo "BOOTSTRAP: finished"
