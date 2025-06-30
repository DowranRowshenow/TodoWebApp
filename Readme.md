# SETUP INSTRUCTIONS

## `PROJECT SETTINGS:`

`./todoproject/settings.py`

Set up an Email for email operations.

    EMAIL_HOST_USER = 'youremail@gmail.com'
    EMAIL_HOST_PASSWORD = 'yourpassword'

Don't forget to take a look at the `TIME_ZONE`, `ALLOWED_HOSTS` and `LANGUAGE_CODE` settings.

## `WINDOWS:`

INSTALL PYTHON 3 AND SETUP
`https://www.python.org/downloads`

INSTALL GIT AND SETUP 
`https://git-scm.com/downloads/win`

CLONE THE GIT REPOSITORY
    
    git clone 'repo_url'

GOTO THE PROJECT DIRECTORY

    cd repo_name

INSTALL AND RUN VIRTUAL ENVIRONMENT:
    
    py -m pip install venv
    py -m venv .venv

INSTALL REQUIREMENTS:

    py -m pip install -r requirements.txt

INSTALL GETTEXT FOR WINDOWS
`https://gnuwin32.sourceforge.net/packages/gettext.htm`

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


## `LINUX`

### Update sudo if needed
    
    sudo apt update

### Install Git if needed
    
    sudo apt install git

### Goto desired directory for project
    
    mkdir projects
    cd projects

### Clone Repository
    
    git clone 'repo_url'

### Go to project dir
    
    cd repo_project_name

### Install Required Python version if needed
    
    sudo apt install python3

### Install Pip
    
    sudo apt install pip

### Install Virtual Environment
    
    sudo apt install python3.12-venv

### Create Virtual Environment
    
    python3 -m venv .venv

### Activate Virtual Environment
    
    source .venv/bin/activate

### Configure mirror repository for pip if needed
    
    mkdir -p ~/.pip
    nano ~/.pip/pip.conf

### Write into `pip.conf`
    
    [global]
    index-url=https://mirrors.tencent.com/pypi/simple/
    extra-index-url=https://mirrors.tencent.com/pypi/simple/
    default=https://pypi.org/simple

### Install Requirements.txt
    
    python3 -m pip install -r requirements.txt

### Install Gettext
    
    sudo apt install gettext

### Install Gettext if needed
    
    sudo apt install gunicorn

### Setup project
    
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py createsuperuser
    python3 manage.py compilemessages
    python3 manage.py collectstatics

### And Finally Run the server
    
    python3 manage.py runserver


# ENJOY!