INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
]

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'KrastyKrabDB',
        # 'USER': 'sa',  # Имя пользователя SQL Server
        # 'PASSWORD': 'your_password',  # Пароль
        'HOST': 'ASUS-VIVOBOOK\\SQLEXPRESS',  # Имя сервера
        'PORT': '',  # Порт (по умолчанию)
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}
