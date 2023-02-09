#!/bin/bash

. venv/bin/activate
source .env

python3 -m pip install -qq *.whl
python3 -m chatterbox.examples.academic_example "Just sending you this message to make sure the installation works..."
