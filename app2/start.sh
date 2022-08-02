#!/bin/bash
gunicorn --bind :8010 app2.wsgi --workers 1 --timeout 120 &
python consumer.py