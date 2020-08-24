#!/bin/bash
pipenv run gunicorn --bind 0.0.0.0:5000 webapp.wsgi:app