SECRET_KEY = 'django-insecure-gq1g#+$awpts+6^5zrz(k#tc+-8l!*%z$3hyu6d-8t*a$3h!ur'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'Tomservo91!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }

    }
}
