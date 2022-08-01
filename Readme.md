## SETUP INSTRUCTIONS

SETTINGS:

`./todoproject/settings.py`

Set up an Email for email operations.

    EMAIL_HOST_USER = 'youremail@gmail.com'
    EMAIL_HOST_PASSWORD = 'yourpassword'

Don't forget to take a look at the `TIME_ZONE`, `ALLOWED_HOSTS` and `LANGUAGE_CODE` settings.

INSTALL VIRTUAL ENVIRONMENT:

`https://realpython.com/python-virtual-environments-a-primer/`

INSTALL REQUIREMENTS:

`./todoproject.requirements.txt`

Requirements used for this project


    asgiref==3.5.2
    Django==4.0.6
    gunicorn==20.1.0
    python-gettext==4.0
    sqlparse==0.4.2
    tzdata==2022.1
    whitenoise==6.2.0

NOTE. Project uses `Whitenoise` to handle static files. And `gettext` for translations.

FINAL STEPS:

Open `commandline` where `manage.py` is located in the project folder and enter the following commands:

    py manage.py makemigrations
    py manage.py migrate
    py manage.py runserver

OPTIONAL:

Create a `superuser`. Enter the following commands:

    py manage.py createsuperuser

Sample:

    Email address: admin@example.com
    Password: **********
    Password (again): *********

## ENJOY!