#!/bin/bash

. venv/bin/activate
source .env

python3 -m pip install openai
python3 -m pip install -qq dist/*.whl
python3 -m chatterbox.examples.academic_example "Just sending you this message to make sure the installation works..."
