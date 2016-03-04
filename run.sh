#!/bin/bash

bower install
virtualenv venv
pip install -r requirements.txt
. venv/bin/activate
python run.py
