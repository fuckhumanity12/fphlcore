#!/bin/bash
cd ~/fphlcore
source env/bin/activate
sudo killall gunicorn
gunicorn -c config/prod.py
sudo systemctl restart nginx