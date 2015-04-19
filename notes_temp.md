https://www.howtoforge.com/tutorial/django-install-ubuntu-14.04/


python -c "import django; print(django.get_version())"

Creating a project
django-admin.py startproject mysite

cd ~/Projects/Py_projects/P_test_django/django-user/mysite

The development server
python manage.py runserver


python manage.py makemigrations polls

python manage.py sqlmigrate polls 0001

python manage.py migrate



Playing with the API
python manage.py shell



Creating an admin user
python manage.py createsuperuser
20flint14@gmai.com  flint  1234



########################## virtualenv ENV_H ##########################
cd ENV_H/
source bin/activate
deactivate




python manage.py startapp records

python manage.py validate
python manage.py sqlall records она просто выводит на экран команды,
которые Django выполнит, если вы попросите.

python manage.py syncdb синхронизирует модели с базой данных. безопасна, ее запуск
ничего не испортит.

python manage.py dbshell    посмотрите, какие таблицы создал Django.



python manage.py shell

from records.models import Publisher
p1 = Publisher(name='Apress', address='2855 Telegraph Avenue',
    city='Berkeley', state_province='CA', country='U.S.A,',
    website='http://www.apress.com/')
p1.save()
p2 = Publisher(name="0'Reilly", address='10 Fawcett St.',
    city='Cambridge', state_province='MA', country='U.S.A.',
    website='http://www.oreilly.com/')
p2.save()
publisher_list = Publisher.objects.all()
publisher_list

===================================== !!!
python manage.py makemigrations records
python manage.py sqlmigrate records 0001
python manage.py migrate

python manage.py inspectdb


b = Book.objects.get(id=1)
b.title