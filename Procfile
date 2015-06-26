
web: gunicorn mysite.wsgi --config gunicorn_config.py --bind 0.0.0.0:${PORT:-5000} --log-level debug

myworker: celery -A records.tasks worker --loglevel=info
