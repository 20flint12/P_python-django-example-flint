########################## virtualenv ENV_H ##########################
cd /home/flint/Projects/Py_projects/P_virtualenv/ENV_H/
source bin/activate
deactivate

cd P_python-django-example-flint/

python manage.py migrate
python manage.py runserver

python manage.py shell