########################## virtualenv ENV_H ##########################
cd /home/flint/Projects/Py_projects/P_virtualenv/ENV_H/
source bin/activate
source ../bin/activate
deactivate


python manage.py makemigrations

python manage.py migrate
python manage.py runserver
python manage.py celery worker --loglevel=info
http://docs.celeryproject.org/en/2.5/django/first-steps-with-django.html
python manage.py shell


python manage.py migrate --fake

python manage.py shell

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


Creating an admin user:
python manage.py createsuperuser
            sergey  20flint12@gmail.com     flint   1234
ENV_H       flint   20flint12@gmail.com     flint   1234
ENV_ACER    acer    20flint12@gmail.com     acer    acer


##########################################################
http://127.0.0.1:8000/hello/
http://127.0.0.1:8000/astro
http://127.0.0.1:8000/time
http://127.0.0.1:8000/meta
http://127.0.0.1:8000/search-form
http://127.0.0.1:8000/json
http://127.0.0.1:8000/polls/
http://127.0.0.1:8000/admin
http://127.0.0.1:8000/email


testastroflint.cloudcontrolled.com/polls
testastroflint.cloudcontrolled.com/astro
testastroflint.cloudcontrolled.com/time
testastroflint.cloudcontrolled.com/meta
testastroflint.cloudcontrolled.com/search-form

testastroflint2.cloudcontrolled.com/json
testastroflint2.cloudcontrolled.com/charts/



python manage.py inspectdb > somefile.txt

pm-suspend 
