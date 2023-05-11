#!/bin/sh
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt