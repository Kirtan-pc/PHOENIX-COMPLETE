#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python phoenix_web/manage.py collectstatic --no-input
python phoenix_web/manage.py migrate
