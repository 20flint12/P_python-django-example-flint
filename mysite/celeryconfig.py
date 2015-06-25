# from __future__ import absolute_import
#
# import os
#
# from celery import Celery
#
# from django.conf import settings
#
# # set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
#
# app = Celery('mysite')
#
# # Using a string here means the worker will not have to
# # pickle the object when using Windows.
# app.config_from_object('django.conf:settings')
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
#
#
# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))



# BROKER_URL = 'amqp://'
# CELERY_RESULT_BACKEND = 'rpc://'
#
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_ACCEPT_CONTENT=['json']
# CELERY_TIMEZONE = 'Europe/Oslo'
# CELERY_ENABLE_UTC = True




# If you are using Ubuntu or Debian install RabbitMQ by executing this command:
# $ sudo apt-get install rabbitmq-server


# To verify that your configuration file works properly,
# $ python -m mysite.celeryconfig



# rabbitmqctl status


# pip install librabbitmq


# celery -A records.tasks worker -B --concurrency=1 --loglevel=info
# сelery -A records.tasks worker --loglevel=info

# python manage.py celery worker -B --concurrency=1 !!!!!!!!

# № Учфьзду
# https://github.com/celery/celery/tree/3.1/examples/django/