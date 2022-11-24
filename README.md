# PY_2021_3_MinhHa
Things to-do when develop web application using Django FrameWork

1. Start project
django-admin startproject <project_name>

2. Start app
python manage.py startapp <app_name>

3. Register app into settings.py -> INSTALLED_APPS
[
    'app_name',
]

4. First run
python manage.py runserver

5. Database related command
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

