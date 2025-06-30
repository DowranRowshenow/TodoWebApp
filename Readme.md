# SETUP INSTRUCTIONS

## `PROJECT SETTINGS:`

Create `.env` file in project root directory and write:

    DEBUG=FALSE # Use FALSE for Production
    SECRET_KEY=key # Your Secure Key
    ALLOWED_HOSTS=localhost,127.0.0.1 # Allowed Hosts
    DATABASE_NAME=database # Your database name
    DATABASE_USER=user # Database user
    DATABASE_PASSWORD=password # Password for user
    DATABASE_PORT=5432 # Database Port
    DATABASE_HOST=localhost # Database Host
    EMAIL_HOST=example@gmail.com # Email address
    EMAIL_PASSWORD=password # App Password of that Email address
    EMAIL_PORT=587 # Email Port

### CREATING A SECURE KEY

Do this after installing `requirements.txt`

    python3 manage.py shell
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())

Copy generated key to the `SECRET_KEY` field in the `.venv` file

Don't forget to take a look at the `TIME_ZONE`, `ALLOWED_HOSTS` and `LANGUAGE_CODE` settings.

### SETUP EMAIL

Enable and set up 2-step verification on your gmail account and Add App Password 
`https://support.google.com/mail/answer/185833?hl=en`

Or use another service

## `WINDOWS:`

### INSTALLATIONS

Install `Python` and setup if you haven't

`https://www.python.org/downloads`

Install `Git` and Setup if you haven't

`https://git-scm.com/downloads/win`

Install `PostgreSQL` and Setup if you haven't

`https://www.postgresql.org/download/windows/`

Write initial User and Password in setup process

Open `SQL Shell` and create database

Clone the git repository
    
    git clone 'https://github.com/DowranRowshenow/TodoWebApp.git'

Go to the project directory

    cd TodoWebApp

Install and run virtual environment:
    
    py -m pip install venv
    py -m venv .venv

Install requirements:

    py -m pip install -r requirements.txt

Install gettext for `Windows` if you haven't

`https://gnuwin32.sourceforge.net/packages/gettext.htm`

Requirements used for this project

    asgiref==3.8.1
    Django==5.2.3
    gunicorn==23.0.0
    packaging==25.0
    psycopg2-binary==2.9.10
    python-dotenv==1.1.1
    python-gettext==5.0
    sqlparse==0.5.3
    typing_extensions==4.14.0
    tzdata==2025.2
    whitenoise==6.9.0

### FINAL STEPS:

Open `commandline` where `manage.py` is located in the project folder and enter the following commands:

    py manage.py makemigrations accounts
    py manage.py makemigrations main
    py manage.py makemigrations
    py manage.py migrate
    py manage.py compilemessages
    py manage.py collectstatics
    py manage.py runserver

### OPTIONAL:

Create a `superuser`. Enter the following commands:

    py manage.py createsuperuser


## `LINUX`

### INSTALLATIONS

Update sudo if needed
    
    sudo apt update

Install Git if haven't
    
    sudo apt install git

Clone Repository
    
    git clone 'https://github.com/DowranRowshenow/TodoWebApp.git'

Go to project directory
    
    cd TodoWebApp

Install `3.13.5` Python version if needed
    
    sudo apt install python3-3.13.5

Install Pip if you haven't
    
    sudo apt install pip

Install Virtual Environment if you haven't 
    
    sudo apt install python3.X-venv

Create Virtual Environment
    
    python3 -m venv .venv

Activate Virtual Environment
    
    source .venv/bin/activate

Configure mirror repository for pip if needed
    
    mkdir -p ~/.pip
    nano ~/.pip/pip.conf

Write into `pip.conf`
    
    [global]
    index-url=https://mirrors.tencent.com/pypi/simple/
    extra-index-url=https://mirrors.tencent.com/pypi/simple/
    default=https://pypi.org/simple

Install Requirements.txt
    
    python3 -m pip install -r requirements.txt

Install Gettext if you haven't
    
    sudo apt install gettext

Install gunicorn if you haven't
    
    sudo apt install gunicorn

### SETUP DATABASE

Install `PostgresSQL`:



Setup `PostgreSQL` and configure `.env` with credentials:

    sudo -u postgres psql
    CREATE USER myuser WITH PASSWORD 'mypassword';
    CREATE DATABASE mydb OWNER myuser;
    ALTER USER myuser CREATEDB;
    ALTER USER myuser SUPERUSER;
    \q

### FINAL STEPS

Setup project
    
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py compilemessages
    python3 manage.py collectstatics
    python3 manage.py createsuperuser

And Finally Run the server
    
    python3 manage.py runserver

Or for Production

    gunicorn todoproject.wsgi:application --bind 0.0.0.0:8000


# ENJOY!