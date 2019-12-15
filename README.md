# Cryptocurrency-REST-API-Django
API built with Django REST Framework

## Getting Started

This tutorial works on **Python 3+** and Django 2+.

Install dependencies:

```
python3 -m pip3 install -r requirements.txt
```

run following commands:

```
python3 manage.py makemigrations trackingAPI
python3 manage.py migrate
python3 manage.py runserver
```
and start Celery worker:

```
celery -A cryptocurrencytracking worker -l info
```
