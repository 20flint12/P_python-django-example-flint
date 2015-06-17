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


# from celery import task
#
# @task()
# def add(x, y):
#     print "my_add" * 5
#     return x + y



# -*- coding: utf-8 -*-
from celery.task import task

@task(ignore_result=True, max_retries=1, default_retry_delay=10)
def just_print():
    print "Print from celery task"


# from celery import Celery
#
# app = Celery('tasks', broker='amqp://guest@localhost//')

# @app.task
# def add(x, y):
#     print "***" * 9
#     return x + y