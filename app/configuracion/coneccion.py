import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# mysqlclient

MYSQL_LOCAL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bd_remota_local',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '',

    }
}

MYSQL_REMOTO = {
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'admin_bd_remoto',
        'USER': 'admin_bd',
        'PASSWORD': 'vincul@cion2021*PREbd',
        'HOST': '3.15.198.138',
        'PORT': '3306'

    }
}