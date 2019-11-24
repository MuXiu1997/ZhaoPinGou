#!/usr/bin/env sh

set -e

export PYTHONPATH=$(pwd)

python /app/manage.py
