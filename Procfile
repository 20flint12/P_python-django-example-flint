web: gunicorn mysite.wsgi --config gunicorn_config.py --bind 0.0.0.0:${PORT:-5000}

web: celery flower --port=$PORT --broker=$CLOUDAMQP_URL --auth=$FLOWER_AUTH_EMAIL
worker: celery -A tasks worker --loglevel=info
