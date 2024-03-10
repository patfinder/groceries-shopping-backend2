# REST framework tutorial

Source: https://github.com/wsvincent/rest-framework-tutorial

Source code for [Official Django REST Framework Tutorial - A Beginners Guide](https://learndjango.com/tutorials/official-django-rest-framework-tutorial-beginners).

Uses Django 4.1 and Django REST Framework 3.14.


[How can I enable CORS on Django REST Framework](https://stackoverflow.com/questions/35760943/how-can-i-enable-cors-on-django-rest-framework)
- python -m pip install django-cors-headers

INSTALLED_APPS = (
    ...
    'corsheaders',
    ...
)
MIDDLEWARE = [
    ...,
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...,
]
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3030',
]


<!-- Create DB -->
CREATE DATABASE groceries;

<!-- Run migration to updaate DB -->
python manage.py migrate

<!-- Start API server -->
python manage.py runserver

