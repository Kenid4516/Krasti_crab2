INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'orders',
]

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'KrastyKrabDB',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'ASUS-VIVOBOOK\\SQLEXPRESS',
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}
