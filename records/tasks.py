# from __future__ import absolute_import
#
# from celery import shared_task
#
#
# @shared_task
# def add(x, y):
#     print "1" * 40
#     return x + y
#
#
# @shared_task
# def mul(x, y):
#     print "2" * 40
#     return x * y
#
#
# @shared_task
# def xsum(numbers):
#     print "3" * 40
#     return sum(numbers)



# from celery import Celery
#
# app = Celery('tasks', broker='amqp://guest@localhost//')

# @app.task
# def add(x, y):
#     print "***" * 9
#     return x + y

#
# import json
from os import getenv

from celery import Celery

# read credentials from runtime environment
amqp_url = getenv('CLOUDAMQP_URL')
# amqp_url = 'amqp://guest@localhost//'
# amqp_url = 'amqp://guest:guest@localhost:15711//'

celery = Celery('tasks', broker=amqp_url)


@celery.task
def add(x, y):
    print "***" * 9
    return x + y




# from celery import Celery
#
# app = Celery('tasks')
#
# @app.task
# def add(x, y):
#     print ".'.'" * 10
#     print getenv('CLOUDAMQP_URL')
#     print "***" * 19
#     return x + y
#
#

