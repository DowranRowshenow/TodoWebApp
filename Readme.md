## SETUP INSTRUCTIONS

SETTINGS:

`./todoproject/settings.py`

First, set your own host and put the host to be used at the top of the list.
Because the host at the top of the list will be used for email transactions.
    
    ALLOWED_HOSTS = [
        'yourhost.com',
    ]

If you want to run the project locally then use the following settings.

    ALLOWED_HOSTS = [
        '127.0.0.1:8000',
        '127.0.0.1',
    ]

NOTE. Project uses `Whitenoise` to handle static files.

And don't forget to take a look at the `TIME_ZONE` and `LANGUAGE_CODE` settings.

Finally, set up an Email for email operations.

    EMAIL_HOST_USER = 'youremail@gmail.com'
    EMAIL_HOST_PASSWORD = 'yourpassword'

## ENJOY!