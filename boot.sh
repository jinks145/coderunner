#!/bin/sh
flask db upgrade
# to deal with the concurrent requests, run gunicorn with 3 workers as the current server instances have a single-core,
# making it a optimal number of threads 
exec gunicorn --workers=3 -b :5000 --access-logfile - --error-logfile - coderunner:coderunner
exec ash