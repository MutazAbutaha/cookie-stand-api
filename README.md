# Lab: Putting it All Together


# Author: Almutaz Abutaha

# note : Husam Obeidat Helped Me




## This is the env file :
SECRET_KEY=F37NvfH-vAvNG3g45XxN06-xTvtGTjBsRu6KvAvj9Jc

DEBUG=True

ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
ALLOW_ALL_ORIGINS=True

DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=poomihcg
DATABASE_USER=poomihcg
DATABASE_PASSWORD=RoypgjD0JclLdT3OZOvHLqUEswz1Ns_K
DATABASE_HOST=peanut.db.elephantsql.com
DATABASE_PORT=5432

## username and password : mutaz mutaz

## to run the app:
* pip install Django
* python manage.py runserver
* pip freeze > requirements.txt
* docker-compose up





# api-quick-start

Template Project for starting up CRUD API with Django Rest Framework

## Customization Steps

- DO NOT migrate yet
- add additional dependencies as needed
  - Re-export requirements.txt as needed
- change `cookie_stands` folder to the app name of your choice
- Search through entire code base for `cookie_stands`,`cookie_stands` and `cookie_stands` to modify code to use your resource
  - `project/settings.py`
  - `project/urls.py`
  - App's files
    - `views.py`
    - `urls.py`
    - `admin.py`
    - `serializers.py`
    - `permissions.py`
  - "Front" files
    - if including a customer facing portion of the site then update/recreate:
      - `urls_front.py`
      - `views_front.py`
      - template files
      - Make sure to update project `urls.py` to add routes to the "front".
- Update cookie_standsModel with fields you need
  - Make sure to update other modules that would be affected by Model customizations. E.g. serializers, tests, etc.
- Rename `project/.env.sample` to `.env` and update as needed
  - To generate secret key use `python3 -c "import secrets; print(secrets.token_urlsafe())"`
- Run makemigrations and migrate commands when ready.
- Run `python manage.py collectstatic`
  - This repository includes static assets in repository. If you are using a Content Delivery Network then remove `staticfiles` from repository.
- Optional: Update `api_tester.py`

## Database

**NOTE:** If you are using Postgres instead of SQLite then make sure to install `psycopg2-binary` and include in `requirements.txt`
