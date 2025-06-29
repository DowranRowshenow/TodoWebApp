## SETUP INSTRUCTIONS

SETTINGS:

`./todoproject/settings.py`

Set up an Email for email operations.

    EMAIL_HOST_USER = 'youremail@gmail.com'
    EMAIL_HOST_PASSWORD = 'yourpassword'

Don't forget to take a look at the `TIME_ZONE`, `ALLOWED_HOSTS` and `LANGUAGE_CODE` settings.

INSTALL AND RUN VIRTUAL ENVIRONMENT:

`https://realpython.com/python-virtual-environments-a-primer/`

INSTALL REQUIREMENTS:

`py -m pip install -r requirements.txt`

Requirements used for this project


    asgiref==3.8.1
    Django==5.2.3
    gunicorn==23.0.0
    packaging==25.0
    python-gettext==5.0
    sqlparse==0.5.3
    typing_extensions==4.14.0
    tzdata==2025.2
    whitenoise==6.9.0

NOTE. Project uses `Whitenoise` to handle static files. And `gettext` for translations.

FINAL STEPS:

Open `commandline` where `manage.py` is located in the project folder and enter the following commands:

    py manage.py makemigrations accounts
    py manage.py makemigrations main
    py manage.py makemigrations
    py manage.py migrate
    py manage.py compilemessages
    py manage.py collectstatics
    py manage.py runserver

OPTIONAL:

Create a `superuser`. Enter the following commands:

    py manage.py createsuperuser

Sample:

    Email address: admin@example.com
    Password: **********
    Password (again): *********

## ENJOY!