web: gunicorn mysite.wsgi --log-file - --log-level debug

#clock: python mysite/clock.py

###w#eb: gunicorn mysite.wsgi --config gunicorn_config.py --bind 0.0.0.0:${PORT:-5000} --log-level debug
###m#yworker: celery -A records.tasks worker -E -B -c 1 -l info
