#!/bin/bash
rm -rf venv
rm map_history.txt
rm server.log
pkill -9 python

python -m venv venv
source venv/Scripts/activate
pip3 install -r requirements.txt
python scraper.py & python server.py
