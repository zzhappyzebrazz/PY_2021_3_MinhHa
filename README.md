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

7. Create Views function, settings URLS path to load templates files
```python
#in project_name/settings.py
STATIC_URL = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

#CKEDITOR
CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}

#in project_name/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('store.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#in app_name/urls.py
urlpatterns = [
    path('', index, name="index"),

]

#in app_name/views.py
def index(request):
    return render(request, 'store/index.html')
```
8. Templates Inheritance
Create a _Master.html file contain header and foot
```html
{% load static %}
<!DOCTYPE html>
<!--
    HEADER
-->

<!--Content-->
{% block main_content %}

{% endblock %}
<!--End Content-->

<!--
    FOOTER
-->
```
Inheritance from child template
```html
{% extends 'app_name/_Master.html' %}
{% load static %}
{% block title_tab %}index{% endblock %}
{% block main_content %}

<!--
    CONTENT
-->
<link href="{% static 'store/img/favicon.ico' %}" rel="icon">
<img src="{% static 'store/img/logo.png' %}" alt="Logo">

{% endblock %}

```

- Create and choose Hash algorthm for password
```bash
#Install hash algorthm
pip install bcrypt scrypt
pip install django[argon2]

#Insert this in project settings.py
#PASSWORD HASH ALGORITHMS
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.ScryptPasswordHasher',
]
```






* Thêm đường dẫn trong file HTML:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stories.urls')),
]
############################
urlpatterns = [
    path('', index, name="index"),
    path('category/', category, name="category"),
    path('contact/', contact, name="contact"),
    path('story/', story, name="story"),
]
############################
href="{% url 'index' %}">Home

- Tạo Views với tham số nhận vào:

def story(request, id):
    content = Story.objects.get(id=id) #get 1 object
    print(content.name)
    return render(request, 'stories/story.html',{
        'content' : content,
    })
############################
<a href="{% url 'story' story.id %}" class="text-white"> {{ story.name }} </a>
############################
urlpatterns = [
    path('', index, name="index"),
    path('category/<int:pk>/', category, name="category"),
    path('story/<int:id>/', story, name="story"),
    path('contact/', contact, name="contact"),

]

############################
<iframe width="560" height="315" src="https://www.youtube.com/embed/SXKlJuO07eM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
############################
```



















* Working with CKEditor
```bash
#install ckeditor to edit content inside the admin site
pip install django-ckeditor
pip install pillow
```
```python
#khai bao app ckeditor in INSTALLED_APPS settings.py
'ckeditor'
'ckeditor_uploader'

#khai bao cac duong dan settings.py
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}

#run command to copy static CKEditor in STATIC_ROOT
python manage.py collectstatic

#khai bao duong dan cho ckeditor in urls patterns /MyNews/MyNews/urls.py
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

#using RichTextUploadingField to using ckeditor feature for attributes
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
content = RichTextUploadingField(blank=True, null=True)

#after updating class in models.py run migrate to update database
python manage.py makemigrations
python manage.py migrate
```
