# PY_2021_3_MinhHa
## Things to-do when develop a web application using Django FrameWork

1. Start project

```bash
django-admin startproject <project_name>
```

2. Start app

```bash
python manage.py startapp <app_name>
```

3. Register app into settings.py -> INSTALLED_APPS

```python
[
    'app_name',
]
```

4. First run
```bash
python manage.py runserver
```
5. Database related command
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py shell
```

6. Project folder tree
```bash
<project_folder>
    ├── db.sqlite3
    ├── manage.py
    ├── media
    │   ├── <app_name>
    │   │   └── images
    │   └── uploads
    │       └── 2022
    ├── <project_name>
    │   ├── asgi.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── static
    │   ├── admin
    │   │   ├── css
    │   │   ├── fonts
    │   │   ├── img
    │   │   └── js
    │   ├── ckeditor
    │   │   ├── ckeditor
    │   │   ├── ckeditor_uploader
    │   └── <app_name>
    │       ├── css
    │       ├── images
    │       ├── js
    │       └── sass
    │
    ├── <app_name>
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   ├── models.py
    │   ├── static
    │   │   └── <app_name>
    │   │       ├── css
    │   │       ├── images
    │   │       ├── js
    │   │       └── sass
    │   ├── templates
    │   │   └── <app_name>
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py

```



