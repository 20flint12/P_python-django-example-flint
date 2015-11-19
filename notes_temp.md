https://www.howtoforge.com/tutorial/django-install-ubuntu-14.04/


python -c "import django; print(django.get_version())"

Creating a project
django-admin.py startproject mysite

cd ~/Projects/Py_projects/P_test_django/django-user/mysite

The development server
python manage.py runserver


python manage.py makemigrations polls
python manage.py makemigrations records

python manage.py sqlmigrate polls 0001

python manage.py migrate



Playing with the API
python manage.py shell





python manage.py startapp records

python manage.py validate
python manage.py sqlall records она просто выводит на экран команды,
которые Django выполнит, если вы попросите.

python manage.py syncdb синхронизирует модели с базой данных. безопасна, ее запуск
ничего не испортит.

python manage.py dbshell    посмотрите, какие таблицы создал Django.



python manage.py shell


===================================== !!!
python manage.py makemigrations records
python manage.py sqlmigrate records 0001
python manage.py migrate

python manage.py inspectdb



http://wiki.scipy.org/Cookbook/Matplotlib/Django


Django celery setup with REDIS
http://www.lexev.org/en/2014/django-celery-setup/


Deploying Celery on cloudControl
https://www.cloudcontrol.com/dev-center/guides/python/celery#
https://github.com/cloudControl/documentation/blob/master/Guides/Python/Celery.md

sudo apt-get install rabbitmq-server

http://simondlr.com/post/24479818721/basic-django-celery-and-rabbitmq-example
2) Run rabbitmq: “
    rabbitmq-server
3) Syncdb: 
    python manage.py syncdb
4) Run django-celery:
    //python manage.py celeryd --log-level=info
    python manage.py celery worker --loglevel=info
5) Run the django server: 
    python manage.py runserver (or gunicorn, whatever you are using).
    

Astro Reminder
13 january 2000
astroreminder
0661395414
95dd2d30    


380688845064@sms.kyivstar.net
380688845064@mms.kyivstar.net