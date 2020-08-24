sudo pipenv shell
flask db upgrade
flask translate compile
exec gunicorn -b :8000 --access-logfile - --error-logfile - microblog:app